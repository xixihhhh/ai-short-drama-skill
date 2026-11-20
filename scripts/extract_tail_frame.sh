#!/usr/bin/env bash
set -euo pipefail
exec python3 "$(dirname "$0")/../skills/dramake/scripts/reference_frames.py" tail "$@"
