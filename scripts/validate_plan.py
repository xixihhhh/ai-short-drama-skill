#!/usr/bin/env python3
"""Run the same plan validator shipped in the installable skill."""
import runpy
import sys
from pathlib import Path

if __name__ == "__main__":
    directory = Path(__file__).resolve().parents[1] / "skills/dramake/scripts"
    sys.path.insert(0, str(directory))
    runpy.run_path(str(directory / "validate_plan.py"), run_name="__main__")
