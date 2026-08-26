#!/usr/bin/env python3
"""Validate Dramake production manifests without calling generation services."""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from pathlib import Path


CONTINUITY_REQUIRED = {
    "block_id", "scene_id", "status", "accepted_parent_clip", "character_identity",
    "wardrobe_or_surface", "phone_or_prop_orientation", "voice_ids", "audio_in",
    "audio_out", "open_motion_vectors", "physical_contact_points", "entry_state",
    "exit_state", "observed_exit_state", "tail_frame", "reanchor_source",
    "canonical_prop_ids", "prop_state_ids", "text_plate_ids",
}
BLOCK_REQUIRED = {
    "block_id", "scene_id", "parent_block_id", "aspect_ratio", "generated_duration_s",
    "edit_beats", "internal_shots", "arc_position", "directorial_intention",
    "value_before", "value_after", "entry_state", "exit_state", "reference_authority",
    "voice_ids", "audio_in", "audio_out", "physical_contact_points", "camera_start",
    "camera_path", "camera_motivation", "camera_end", "subject_endpoint",
    "transition_in", "transition_out", "reanchor_required", "candidate_status",
    "observed_exit_state", "tail_frame", "canonical_prop_ids", "text_plate_ids",
    "physical_event_contract", "impact_role",
}
SHOT_REQUIRED = {
    "shot_id", "scene_id", "block_id", "start_s", "end_s", "narrative_job",
    "directorial_intention", "value_before", "value_after", "subject_action",
    "listener_or_world_reaction", "camera_start", "camera_path", "camera_motivation",
    "camera_end", "subject_endpoint", "screen_direction", "reference_authority",
    "audio_in", "audio_out", "physical_contact_points", "transition_in", "transition_out",
    "canonical_prop_ids", "prop_state_ids", "text_plate_ids", "physical_start_state",
    "control_input", "world_motion_vector", "screen_motion_vector",
    "physical_phase_sequence", "physical_end_state", "impact_role", "impact_pattern",
}
VOICE_REQUIRED = {
    "voice_id", "character_id", "language", "pronunciation_list", "timbre",
    "pitch_center_range", "speaking_rate", "emotional_baseline", "reference_asset",
    "rights_status", "forbidden_cross_bindings",
}
AUDIO_REQUIRED = {
    "scene_id", "block_id", "active_speaker", "voice_id", "dialogue_status",
    "ambience_in", "ambience_out", "bgm_phrase_in", "bgm_phrase_out", "sfx_sync_cue",
    "reverb_tail", "loudness_target", "reference_audio_owner", "post_action", "qa_status",
}
COST_REQUIRED = {
    "route_id", "provider", "model", "quality_mode", "authorization_mode", "blocks",
    "candidates", "unit_price", "currency", "retry_factor", "cap_requests",
    "price_checked_at",
}

ACCEPTED = {"accepted", "accepted_with_deviation"}
CONTINUITY_STATUSES = {
    "planned", "ready", "generated", "reviewed", "accepted",
    "accepted_with_deviation", "repair", "rejected",
}
BLOCK_STATUSES = CONTINUITY_STATUSES | {"candidate"}
AUTHORIZATION_MODES = {"plan-only", "single-test", "approved-batch", "autopilot-with-cap"}
QUALITY_MODES = {"sketch", "economy", "balanced", "premium", "hero-insert", "final-polish"}
ASPECT_RE = re.compile(r"^(?:[1-9]\d*:[1-9]\d*|custom)$")


def read_csv(path: Path, required: set[str]) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = required - headers
        if missing:
            errors.append(f"{path}: missing columns {sorted(missing)}")
        rows = []
        for line, raw in enumerate(reader, start=2):
            if None in raw:
                errors.append(f"{path}:{line}: too many CSV values")
                continue
            row = {key: (value or "").strip() for key, value in raw.items()}
            if any(row.values()):
                row["__line__"] = str(line)
                rows.append(row)
    return rows, errors


def normalize_value(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).casefold()
    return "".join(ch for ch in text if ch.isalnum())


def split_ids(value: str) -> set[str]:
    """Split semicolon/pipe/whitespace-delimited IDs used inside one CSV cell."""
    return {item for item in re.split(r"[;|\s]+", value.strip()) if item and item.lower() != "none"}


def require_unique(rows: list[dict[str, str]], key: str, path: Path) -> list[str]:
    errors: list[str] = []
    seen: dict[str, str] = {}
    for row in rows:
        value = row.get(key, "")
        line = row["__line__"]
        if not value:
            errors.append(f"{path}:{line}: empty {key}")
        elif value in seen:
            errors.append(f"{path}:{line}: duplicate {key} {value!r}; first at line {seen[value]}")
        else:
            seen[value] = line
    return errors


def find_cycles(parent_of: dict[str, str], path: Path, relation: str) -> list[str]:
    errors: list[str] = []
    done: set[str] = set()
    for start in parent_of:
        if start in done:
            continue
        chain: list[str] = []
        positions: dict[str, int] = {}
        node = start
        while node and node in parent_of:
            if node in positions:
                cycle = chain[positions[node]:] + [node]
                errors.append(f"{path}: {relation} cycle {' -> '.join(cycle)}")
                break
            if node in done:
                break
            positions[node] = len(chain)
            chain.append(node)
            node = parent_of.get(node, "")
        done.update(chain)
    return errors


def validate_continuity(path: Path) -> list[str]:
    rows, errors = read_csv(path, CONTINUITY_REQUIRED)
    errors += require_unique(rows, "block_id", path)
    by_id = {row["block_id"]: row for row in rows if row.get("block_id")}
    parents: dict[str, str] = {}

    for row in rows:
        line = row["__line__"]
        block_id = row.get("block_id", "")
        status = row.get("status", "")
        parent = row.get("accepted_parent_clip", "")
        if status and status not in CONTINUITY_STATUSES:
            errors.append(f"{path}:{line}: unknown status {status!r}")
        if status in ACCEPTED:
            for field in ("observed_exit_state", "tail_frame"):
                if not row.get(field):
                    errors.append(f"{path}:{line}: accepted block requires {field}")
        if status == "rejected" and row.get("observed_exit_state"):
            errors.append(f"{path}:{line}: rejected block cannot define observed_exit_state")
        if parent:
            parents[block_id] = parent
            if parent == block_id:
                errors.append(f"{path}:{line}: block cannot parent itself")
            parent_row = by_id.get(parent)
            if parent_row is None:
                errors.append(f"{path}:{line}: parent {parent!r} not found")
            elif status not in {"planned"}:
                if parent_row.get("status") not in ACCEPTED:
                    errors.append(f"{path}:{line}: executable child requires accepted parent {parent!r}")
                if not parent_row.get("observed_exit_state"):
                    errors.append(f"{path}:{line}: parent {parent!r} lacks observed_exit_state")
        for field in ("scene_id", "character_identity", "entry_state", "exit_state"):
            if not row.get(field):
                errors.append(f"{path}:{line}: empty {field}")

    errors += find_cycles(parents, path, "continuity parent")
    return errors


def validate_blocks(path: Path) -> list[str]:
    rows, errors = read_csv(path, BLOCK_REQUIRED)
    errors += require_unique(rows, "block_id", path)
    ids = {row.get("block_id", "") for row in rows}
    parents: dict[str, str] = {}
    for row in rows:
        line = row["__line__"]
        block_id = row.get("block_id", "")
        parent = row.get("parent_block_id", "")
        if parent:
            parents[block_id] = parent
            if parent == block_id:
                errors.append(f"{path}:{line}: block cannot parent itself")
            elif parent not in ids:
                errors.append(f"{path}:{line}: parent {parent!r} not found")
        if not ASPECT_RE.fullmatch(row.get("aspect_ratio", "")):
            errors.append(f"{path}:{line}: invalid aspect_ratio {row.get('aspect_ratio')!r}")
        if row.get("candidate_status") and row["candidate_status"] not in BLOCK_STATUSES:
            errors.append(f"{path}:{line}: unknown candidate_status {row['candidate_status']!r}")
        if row.get("reanchor_required").lower() not in {"true", "false"}:
            errors.append(f"{path}:{line}: reanchor_required must be true or false")
        try:
            duration = float(row.get("generated_duration_s", ""))
            beats = int(row.get("edit_beats", ""))
            shots = int(row.get("internal_shots", ""))
            if duration <= 0 or beats <= 0 or shots <= 0:
                raise ValueError
            if duration >= 20 and beats < 4:
                errors.append(f"{path}:{line}: >=20s block requires at least 4 edit beats")
            elif duration >= 10 and beats < 2:
                errors.append(f"{path}:{line}: >=10s block requires at least 2 edit beats")
            if shots > max(1, int(duration // 3)):
                errors.append(f"{path}:{line}: internal_shots exceed conservative duration capacity")
        except ValueError:
            errors.append(f"{path}:{line}: duration, edit_beats, and internal_shots must be positive numbers")
        if normalize_value(row.get("value_before", "")) == normalize_value(row.get("value_after", "")):
            errors.append(f"{path}:{line}: value_before and value_after must differ")
        for field in (
            "scene_id", "directorial_intention", "entry_state", "exit_state",
            "reference_authority", "camera_start", "camera_path", "camera_motivation",
            "camera_end", "subject_endpoint", "audio_in", "audio_out",
        ):
            if not row.get(field):
                errors.append(f"{path}:{line}: empty {field}")
        if row.get("physical_contact_points") and not row.get("physical_event_contract"):
            errors.append(f"{path}:{line}: contact block requires physical_event_contract")
        impact_role = row.get("impact_role", "")
        if impact_role not in {"none", "hook", "collision", "reveal", "climax"}:
            errors.append(f"{path}:{line}: invalid impact_role {impact_role!r}")
    errors += find_cycles(parents, path, "block parent")
    return errors


def validate_shots(path: Path) -> list[str]:
    rows, errors = read_csv(path, SHOT_REQUIRED)
    errors += require_unique(rows, "shot_id", path)
    for row in rows:
        line = row["__line__"]
        try:
            start = float(row.get("start_s", ""))
            end = float(row.get("end_s", ""))
            if start < 0 or end <= start:
                raise ValueError
        except ValueError:
            errors.append(f"{path}:{line}: require 0 <= start_s < end_s")
        if normalize_value(row.get("value_before", "")) == normalize_value(row.get("value_after", "")):
            errors.append(f"{path}:{line}: value_before and value_after must differ")
        for field in (
            "scene_id", "block_id", "narrative_job", "directorial_intention",
            "subject_action", "camera_start", "camera_path", "camera_motivation",
            "camera_end", "subject_endpoint", "reference_authority",
        ):
            if not row.get(field):
                errors.append(f"{path}:{line}: empty {field}")
        if row.get("physical_contact_points"):
            for field in (
                "physical_start_state", "control_input", "world_motion_vector",
                "screen_motion_vector", "physical_phase_sequence", "physical_end_state",
            ):
                if not row.get(field):
                    errors.append(f"{path}:{line}: contact shot requires {field}")
        impact_role = row.get("impact_role", "")
        if impact_role not in {"none", "hook", "collision", "reveal", "climax"}:
            errors.append(f"{path}:{line}: invalid impact_role {impact_role!r}")
        elif impact_role != "none" and not row.get("impact_pattern"):
            errors.append(f"{path}:{line}: impact shot requires impact_pattern")
    return errors


def validate_voice_bible(path: Path) -> list[str]:
    rows, errors = read_csv(path, VOICE_REQUIRED)
    errors += require_unique(rows, "voice_id", path)
    for row in rows:
        line = row["__line__"]
        for field in ("character_id", "language", "timbre", "pitch_center_range", "speaking_rate"):
            if not row.get(field):
                errors.append(f"{path}:{line}: empty {field}")
        if row.get("reference_asset") and normalize_value(row.get("rights_status", "")) not in {
            "cleared", "approved", "licensed", "owned", "publicdomain", "用户已授权",
        }:
            errors.append(f"{path}:{line}: reference_asset requires explicit cleared rights_status")
    return errors


def validate_audio(path: Path) -> list[str]:
    rows, errors = read_csv(path, AUDIO_REQUIRED)
    seen: dict[tuple[str, str, str], str] = {}
    for row in rows:
        line = row["__line__"]
        key = (row.get("scene_id", ""), row.get("block_id", ""), row.get("voice_id", ""))
        if not all(key[:2]):
            errors.append(f"{path}:{line}: scene_id and block_id are required")
        elif key in seen:
            errors.append(f"{path}:{line}: duplicate scene/block/voice row {key}; first at line {seen[key]}")
        else:
            seen[key] = line
        for field in ("ambience_in", "ambience_out", "loudness_target", "post_action", "qa_status"):
            if not row.get(field):
                errors.append(f"{path}:{line}: empty {field}")
        if row.get("reference_audio_owner") and not row.get("voice_id"):
            errors.append(f"{path}:{line}: reference_audio_owner requires voice_id")
    return errors


def validate_cost(path: Path) -> list[str]:
    rows, errors = read_csv(path, COST_REQUIRED)
    errors += require_unique(rows, "route_id", path)
    for row in rows:
        line = row["__line__"]
        auth = row.get("authorization_mode", "")
        quality = row.get("quality_mode", "")
        if auth not in AUTHORIZATION_MODES:
            errors.append(f"{path}:{line}: unknown authorization_mode {auth!r}")
        if quality not in QUALITY_MODES:
            errors.append(f"{path}:{line}: unknown quality_mode {quality!r}")
        try:
            blocks = int(row.get("blocks", ""))
            candidates = int(row.get("candidates", ""))
            unit_price = float(row.get("unit_price", ""))
            retry_factor = float(row.get("retry_factor", ""))
            cap_requests = int(row.get("cap_requests", ""))
            if blocks <= 0 or candidates <= 0 or unit_price < 0 or retry_factor < 1 or cap_requests <= 0:
                raise ValueError
            minimum_requests = blocks * candidates
            if cap_requests < minimum_requests:
                errors.append(f"{path}:{line}: cap_requests cannot be below blocks*candidates")
        except ValueError:
            errors.append(f"{path}:{line}: invalid blocks/candidates/price/retry/cap values")
        if not row.get("currency"):
            errors.append(f"{path}:{line}: empty currency")
        if row.get("price_checked_at") in {"", "YYYY-MM-DD"} and row.get("unit_price") not in {"", "0", "0.0"}:
            errors.append(f"{path}:{line}: paid route requires dated price_checked_at")
    return errors


def validate_cross_files(args: argparse.Namespace) -> list[str]:
    """Validate IDs, durations, state, voices, and audio across supplied manifests."""
    errors: list[str] = []
    tables: dict[str, tuple[Path, list[dict[str, str]]]] = {}
    specs = {
        "continuity": (args.continuity, CONTINUITY_REQUIRED),
        "blocks": (args.block_manifest, BLOCK_REQUIRED),
        "shots": (args.shot_plan, SHOT_REQUIRED),
        "voices": (args.voice_bible, VOICE_REQUIRED),
        "audio": (args.audio_continuity, AUDIO_REQUIRED),
    }
    for name, (path, required) in specs.items():
        if path:
            rows, _ = read_csv(path, required)
            tables[name] = (path, rows)

    block_rows = tables.get("blocks", (Path(), []))[1]
    block_by_id = {row.get("block_id", ""): row for row in block_rows if row.get("block_id")}
    if "shots" in tables and block_rows:
        shot_path, shot_rows = tables["shots"]
        shots_by_block: dict[str, list[dict[str, str]]] = {}
        for shot in shot_rows:
            block_id = shot.get("block_id", "")
            if block_id not in block_by_id:
                errors.append(f"{shot_path}:{shot['__line__']}: unknown block_id {block_id!r}")
                continue
            shots_by_block.setdefault(block_id, []).append(shot)
            try:
                if float(shot.get("end_s", "")) > float(block_by_id[block_id].get("generated_duration_s", "")):
                    errors.append(f"{shot_path}:{shot['__line__']}: shot exceeds parent block duration")
            except ValueError:
                pass
        for block_id, block in block_by_id.items():
            planned = int(block.get("internal_shots", "0") or 0)
            actual = len(shots_by_block.get(block_id, []))
            if shot_rows and actual != planned:
                errors.append(f"{shot_path}: block {block_id!r} plans {planned} internal_shots but defines {actual}")

    voice_rows = tables.get("voices", (Path(), []))[1]
    known_voices = {row.get("voice_id", "") for row in voice_rows if row.get("voice_id")}
    if known_voices:
        for block in block_rows:
            for voice_id in split_ids(block.get("voice_ids", "")):
                if voice_id not in known_voices:
                    errors.append(f"{tables['blocks'][0]}:{block['__line__']}: unknown voice_id {voice_id!r}")
        if "audio" in tables:
            audio_path, audio_rows = tables["audio"]
            for row in audio_rows:
                voice_id = row.get("voice_id", "")
                if voice_id and voice_id not in known_voices:
                    errors.append(f"{audio_path}:{row['__line__']}: unknown voice_id {voice_id!r}")

    if "audio" in tables and block_rows:
        audio_path, audio_rows = tables["audio"]
        for row in audio_rows:
            block_id = row.get("block_id", "")
            if block_id not in block_by_id:
                errors.append(f"{audio_path}:{row['__line__']}: unknown block_id {block_id!r}")
            elif row.get("scene_id") != block_by_id[block_id].get("scene_id"):
                errors.append(f"{audio_path}:{row['__line__']}: scene_id disagrees with block manifest")

    if "continuity" in tables and block_rows:
        continuity_path, continuity_rows = tables["continuity"]
        continuity_by_id = {row.get("block_id", ""): row for row in continuity_rows if row.get("block_id")}
        for block_id, block in block_by_id.items():
            state = continuity_by_id.get(block_id)
            if state is None:
                errors.append(f"{continuity_path}: missing continuity row for block {block_id!r}")
                continue
            parent = block.get("parent_block_id", "")
            if parent != state.get("accepted_parent_clip", ""):
                errors.append(f"{continuity_path}:{state['__line__']}: parent disagrees with block manifest")
            if parent and parent in continuity_by_id and block.get("scene_id") == block_by_id.get(parent, {}).get("scene_id"):
                parent_exit = continuity_by_id[parent].get("observed_exit_state", "")
                child_entry = state.get("entry_state", "")
                if parent_exit and normalize_value(parent_exit) != normalize_value(child_entry):
                    errors.append(f"{continuity_path}:{state['__line__']}: child entry_state does not match accepted parent observed_exit_state")
    return errors
    rows, errors = read_csv(path, required)
    errors += require_unique(rows, primary, path)
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--continuity", type=Path)
    parser.add_argument("--block-manifest", type=Path)
    parser.add_argument("--shot-plan", type=Path)
    parser.add_argument("--voice-bible", type=Path)
    parser.add_argument("--audio-continuity", type=Path)
    parser.add_argument("--cost", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    if args.continuity:
        errors += validate_continuity(args.continuity)
    if args.block_manifest:
        errors += validate_blocks(args.block_manifest)
    if args.shot_plan:
        errors += validate_shots(args.shot_plan)
    if args.voice_bible:
        errors += validate_voice_bible(args.voice_bible)
    if args.audio_continuity:
        errors += validate_audio(args.audio_continuity)
    if args.cost:
        errors += validate_cost(args.cost)
    if not any(vars(args).values()):
        parser.error("provide at least one manifest path")
    errors += validate_cross_files(args)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("Dramake plan validation passed")


if __name__ == "__main__":
    main()
