#!/usr/bin/env python3
"""Validate basic PawDirector continuity and cost artifacts without provider APIs."""

import argparse
import csv
from pathlib import Path


CONTINUITY_REQUIRED = {
    "block_id", "status", "location", "axis_screen_direction", "pet_identity",
    "wardrobe_structure", "prop_state", "physical_contact_points", "entry_state", "exit_state"
}
COST_REQUIRED = {
    "route_id", "provider", "model", "blocks", "candidates", "unit_price",
    "currency", "retry_factor", "price_checked_at"
}


def validate_csv(path: Path, required: set[str]) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            errors.append(f"{path}: missing columns {sorted(missing)}")
        for line, row in enumerate(reader, start=2):
            if not row.get(next(iter(required)), "").strip():
                errors.append(f"{path}:{line}: empty primary identifier")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--continuity", type=Path)
    parser.add_argument("--cost", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    if args.continuity:
        errors += validate_csv(args.continuity, CONTINUITY_REQUIRED)
    if args.cost:
        errors += validate_csv(args.cost, COST_REQUIRED)
    if not args.continuity and not args.cost:
        parser.error("provide --continuity and/or --cost")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("PawDirector plan validation passed")


if __name__ == "__main__":
    main()
