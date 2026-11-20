"""Validate a local edit handoff against review decisions, media and edit geometry."""
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess

MEDIA_TRACKS = {"video", "dialogue", "ambience", "music", "sfx"}
EPSILON = 0.001  # CSV timestamps rounded to milliseconds
RANGE = re.compile(r"(?:(?P<label>[\w.-]+)=)?(?P<start>\d+(?:\.\d+)?)-(?P<end>\d+(?:\.\d+)?)")
TRANSITION = re.compile(r"(dissolve|crossfade):(\d+(?:\.\d+)?)")


def positive_duration(value):
    try:
        seconds = float(value)
    except (ValueError, TypeError):
        return None
    return seconds if math.isfinite(seconds) and seconds > 0 else None


@lru_cache(maxsize=512)
def media_duration(path, kind):
    if not path.is_file():
        raise ValueError(f"missing media: {path}")
    cmd = ["ffprobe", "-v", "error", "-protocol_whitelist", "file,pipe",
           "-select_streams", "V:0" if kind == "video" else "a:0"]
    def probe(entries, *opts):
        result = subprocess.run([*cmd, *opts, "-show_entries", entries, "-of", "json", str(path)],
                                capture_output=True, text=True, check=False)
        if result.returncode:
            raise ValueError(result.stderr.strip() or f"ffprobe failed: {path}")
        return json.loads(result.stdout)
    streams = probe("stream=duration")["streams"]
    if not streams:
        raise ValueError(f"media has no {kind} stream: {path}")
    length = positive_duration(streams[0].get("duration"))
    if length:
        return length
    # Some formats omit stream duration. A longer music track or container
    # duration must not extend the last usable video frame.
    packets = probe("packet=pts_time,duration_time", "-show_packets").get("packets", [])
    spans = [(float(pkt["pts_time"]), float(pkt["duration_time"])) for pkt in packets
             if pkt.get("pts_time") not in (None, "N/A") and positive_duration(pkt.get("duration_time"))]
    if len(spans) != len(packets) or not spans:
        raise ValueError(f"cannot determine {kind} stream duration: {path}")
    length = max(at + duration for at, duration in spans) - min(at for at, _ in spans)
    if not positive_duration(length):
        raise ValueError(f"invalid stream duration: {path}")
    return length


@lru_cache(maxsize=512)
def file_digest(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def accepted_ranges(review):
    spans = {}
    for ordinal, token in enumerate(review["accepted_ranges"].split(";"), 1):
        match = RANGE.fullmatch(token.strip())
        if not match:
            raise ValueError("use accepted_ranges such as intro=0-4;ending=5-8")
        name = match["label"] or str(ordinal)
        start, end = float(match["start"]), float(match["end"])
        if name in spans or not math.isfinite(end) or not 0 <= start < end:
            raise ValueError("invalid or duplicate accepted range")
        spans[name] = (start, end)
    return spans


def validate_tracks(tracks):
    errors = []
    for (kind, track), rows in tracks.items():
        rows.sort(key=lambda item: item[0])
        for idx, (start, end, row) in enumerate(rows):
            prev = rows[idx - 1] if idx else None
            following = rows[idx + 1] if idx + 1 < len(rows) else None
            label = f"{row['event_id']} ({kind}/{track})"
            overlap = prev[1] - start if prev else 0
            incoming = row.get("transition_in", "").lower()
            outgoing = row.get("transition_out", "").lower()
            for transition in (incoming, outgoing):
                if transition not in {"", "none", "cut"} and not TRANSITION.fullmatch(transition):
                    errors.append(f"{label}: unsupported transition {transition!r}")
            if overlap > EPSILON:
                left = TRANSITION.fullmatch(prev[2].get("transition_out", "").lower())
                right = TRANSITION.fullmatch(incoming)
                if (not left or not right or left[1] != right[1] or
                        any(abs(float(m[2]) - overlap) > EPSILON for m in (left, right)) or
                        prev[0] >= start or prev[1] >= end or (idx > 1 and rows[idx - 2][1] > start + EPSILON)):
                    errors.append(f"{label}: overlap requires a matching two-event transition and duration")
            elif TRANSITION.fullmatch(incoming):
                errors.append(f"{label}: incoming transition has no matching overlap")
            if TRANSITION.fullmatch(outgoing) and (not following or end - following[0] <= EPSILON):
                errors.append(f"{label}: outgoing transition has no matching overlap")
            if kind == "video" and track == "main" and (start if not prev else -overlap) > EPSILON:
                errors.append(f"{label}: gap in primary video track")
    return errors


def validate_delivery(events, jobs, reviews, root):
    errors = []
    tracks = defaultdict(list)
    if not any(r["track_type"] == "video" and (r.get("track_id") or "main") == "main" for r in events):
        errors.append("delivery requires a primary video event (track_id main or empty)")
    job_map = {r["job_id"]: r for r in jobs}
    review_map = {r["review_id"]: r for r in reviews}
    for row in events:
        event = row["event_id"]
        kind = row["track_type"]
        try:
            src_in, src_out, start, end, speed = [float(row[key]) for key in
                ("source_in_s", "source_out_s", "timeline_in_s", "timeline_out_s", "speed")]
            if not all(map(math.isfinite, (src_in, src_out, start, end, speed))) or speed <= 0:
                raise ValueError("expected finite edit times and positive speed")
            if abs((src_out - src_in) / speed - (end - start)) > EPSILON:
                raise ValueError("source range / speed does not match timeline duration")
            tracks[(kind, row.get("track_id") or "main")].append((start, end, row))
            source = (root / row["source_uri"]).resolve()
            duration = None
            if kind in MEDIA_TRACKS:
                duration = media_duration(source, "video" if kind == "video" else "audio")
                if src_out > duration + EPSILON:
                    raise ValueError(f"source range exceeds {duration:.3f}s media duration")
            if kind == "video" or row["job_id"] or row["accepted_range_id"]:
                job = job_map.get(row["job_id"])
                if not job or job["status"] not in {"completed", "recovered", "reviewed", "accepted"}:
                    raise ValueError("missing completed source job")
                if job["block_id"] != row["block_id"] or not job["output_uri"] or (root / job["output_uri"]).resolve() != source:
                    raise ValueError("source file or block does not match job output")
                expected_hash = job.get("output_sha256", "").lower()
                if expected_hash and (not re.fullmatch(r"[0-9a-f]{64}", expected_hash) or file_digest(source) != expected_hash):
                    raise ValueError("media SHA-256 does not match reviewed job output")
                review_id, _, range_id = row["accepted_range_id"].rpartition(":")
                review = review_map.get(review_id)
                if (not review or review["decision"] not in {"accepted", "accepted_with_deviation"}
                        or review["must_hit_result"] != "pass" or review["job_id"] != job["job_id"]
                        or review["block_id"] != job["block_id"]):
                    raise ValueError("missing accepted candidate review matching this job and block")
                bounds = accepted_ranges(review).get(range_id)
                if bounds and duration is not None and bounds[1] > duration + EPSILON:
                    raise ValueError("accepted range exceeds local media duration")
                if job.get("accepted_ranges") and not any(a - EPSILON <= src_in and src_out <= b + EPSILON
                                                           for a, b in accepted_ranges(job).values()):
                    raise ValueError("cut falls outside the source job's accepted ranges")
                if not bounds or src_in < bounds[0] - EPSILON or src_out > bounds[1] + EPSILON:
                    raise ValueError("source range outside the cited accepted range")
        except (ValueError, KeyError, OSError, OverflowError) as exc:
            errors.append(f"{event}: {exc}")
    return errors + validate_tracks(tracks)
