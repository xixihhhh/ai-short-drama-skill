#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo "usage: $0 input.mp4 tail.png" >&2
  exit 2
fi
duration="$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$1")"
timestamp="$(awk -v d="$duration" 'BEGIN { t=d-0.20; if (t<0) t=0; printf "%.3f", t }')"
ffmpeg -hide_banner -loglevel error -ss "$timestamp" -i "$1" -frames:v 1 "$2"
