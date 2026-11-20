#!/usr/bin/env python3
"""Inspect final video layout, audio tracks, and optional UTF-8 SubRip cues."""

import argparse
import json
import re
import subprocess
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path


TIME = r"(\d{2,}):([0-5]\d):([0-5]\d)[,.](\d{3})"
TIMING = re.compile(TIME + r"\s*-->\s*" + TIME + r"(?:\s+X1:\d+ X2:\d+ Y1:\d+ Y2:\d+)?")


def milliseconds(parts):
    hours, minutes, seconds, millis = map(int, parts)
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis


def check_subtitles(path, end_ms):
    contents = path.read_text(encoding="utf-8-sig").strip()
    if not contents:
        raise ValueError("SRT file has no cues")
    blocks = re.split(r"\n[ \t]*\n+", contents)
    for number, block in enumerate(blocks, 1):
        lines = block.strip().splitlines()
        if lines[0].strip().isdigit():
            lines = lines[1:]
        timing = TIMING.fullmatch(lines[0].strip()) if lines else None
        if not timing or not any(line.strip() for line in lines[1:]):
            raise ValueError(f"SRT cue {number}: expected a timestamp range and caption text")
        if any(TIMING.fullmatch(line.strip()) for line in lines[1:]):
            raise ValueError(f"SRT cue {number}: missing blank line between cues")
        start, end = milliseconds(timing.groups()[:4]), milliseconds(timing.groups()[4:])
        if start >= end or end > end_ms:
            raise ValueError(f"SRT cue {number}: {start}–{end} ms falls outside a valid interval in 0–{end_ms} ms")
    return len(blocks)


def inspect_export(path, layout, require_audio, subtitles):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path.resolve())],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or "ffprobe could not read the media")
    media = json.loads(result.stdout)
    streams = media.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"
                  and not s.get("disposition", {}).get("attached_pic")), None)
    if not video:
        raise ValueError("no video track")
    duration = video.get("duration")
    if duration in (None, "N/A"):
        duration = media.get("format", {}).get("duration")
    seconds = Decimal(str(duration))
    if not seconds.is_finite() or seconds <= 0:
        raise ValueError("video has no positive duration")
    width, height = video["width"], video["height"]
    sar = video.get("sample_aspect_ratio")
    ratio = Fraction(width, height)
    if sar and sar not in ("N/A", "0:1"):
        ratio *= Fraction(sar.replace(":", "/"))
    rotation = next((s["rotation"] for s in video.get("side_data_list", []) if "rotation" in s),
                    video.get("tags", {}).get("rotate", 0))
    angle = float(rotation) % 360
    if angle in (90, 270):
        ratio = 1 / ratio
    elif angle not in (0, 180):
        raise ValueError(f"unsupported display rotation {rotation} degrees")
    actual_layout = "square" if ratio == 1 else "landscape" if ratio > 1 else "portrait"
    if layout and layout != actual_layout:
        raise ValueError(f"expected {layout}, found {actual_layout} (display aspect {ratio})")
    audio = sum(s.get("codec_type") == "audio" for s in streams)
    if require_audio and not audio:
        raise ValueError("expected an audio track, found none")
    cues = check_subtitles(subtitles, round(seconds * 1000)) if subtitles else None
    report = f"{actual_layout} ({ratio}), {seconds} s, {audio} audio track(s)"
    return f"{report}, {cues} SRT cue(s)" if cues is not None else report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--layout", choices=["portrait", "landscape", "square"])
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--srt", type=Path, help="optional UTF-8 subtitle file timed to this export")
    args = parser.parse_args()
    try:
        print(inspect_export(args.video, args.layout, args.require_audio, args.srt))
    except (OSError, ValueError, InvalidOperation, ZeroDivisionError) as error:
        print(f"Export check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
