#!/usr/bin/env python3
"""Verify that Dramake's Chinese-default documentation has English mirrors."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def frontmatter_value(path: Path, key: str) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1) if match else ""


def main() -> None:
    pairs: list[tuple[Path, Path]] = [
        (ROOT / "README.md", ROOT / "README.en.md"),
        (ROOT / "CHANGELOG.md", ROOT / "CHANGELOG.en.md"),
        (ROOT / "CONTRIBUTING.md", ROOT / "CONTRIBUTING.en.md"),
        (ROOT / "benchmarks/tested-observations.md", ROOT / "benchmarks/tested-observations.en.md"),
        (ROOT / "skills/dramake/SKILL.md", ROOT / "skills/dramake/SKILL.en.md"),
    ]

    for path in sorted((ROOT / "skills/dramake/references").glob("*.md")):
        pairs.append((path, path.parent / "en" / path.name))
    for path in sorted((ROOT / "skills/dramake/assets/templates").glob("*.md")):
        pairs.append((path, path.parent / "en" / path.name))
    for path in sorted((ROOT / "examples").glob("*/README.md")):
        pairs.append((path, path.with_name("README.en.md")))
    for path in sorted((ROOT / ".github/ISSUE_TEMPLATE").glob("*.md")):
        if not path.name.endswith(".en.md"):
            pairs.append((path, path.with_name(path.stem + ".en.md")))

    errors: list[str] = []
    for chinese, english in pairs:
        if not chinese.is_file():
            errors.append(f"missing Chinese default: {chinese.relative_to(ROOT)}")
        if not english.is_file():
            errors.append(f"missing English mirror: {english.relative_to(ROOT)}")
        if chinese.is_file() and chinese.stat().st_size == 0:
            errors.append(f"empty Chinese default: {chinese.relative_to(ROOT)}")
        if english.is_file() and english.stat().st_size == 0:
            errors.append(f"empty English mirror: {english.relative_to(ROOT)}")

    zh_skill = ROOT / "skills/dramake/SKILL.md"
    en_skill = ROOT / "skills/dramake/SKILL.en.md"
    for key in ("name", "version"):
        if frontmatter_value(zh_skill, key) != frontmatter_value(en_skill, key):
            errors.append(f"SKILL frontmatter mismatch: {key}")

    version = frontmatter_value(zh_skill, "version")
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if not re.search(rf"(?m)^version:\s*{re.escape(version)}\s*$", citation):
        errors.append(f"CITATION.cff version does not match SKILL {version}")
    for readme in (ROOT / "README.md", ROOT / "README.en.md"):
        if f"Skill-v{version}" not in readme.read_text(encoding="utf-8"):
            errors.append(f"README badge version mismatch: {readme.name}")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"Dramake bilingual check passed: {len(pairs)} document pairs, version {version}")


if __name__ == "__main__":
    main()
