#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo "usage: $0 input.mp4 output.jpg" >&2
  exit 2
fi
ffmpeg -hide_banner -loglevel error -i "$1" -vf "fps=1/2.5,scale=360:-1,tile=4x3" -frames:v 1 -q:v 2 "$2"
