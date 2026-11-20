#!/usr/bin/env python3
"""Create a paged reference contact sheet or extract the final decoded video frame."""
import argparse
import csv
import math
import shutil
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CELL_WIDTH, CELL_HEIGHT, IMAGE_HEIGHT = 320, 202, 180
COLS, ROWS = 4, 3
# Small timestamp font. Needs neither a system font nor FFmpeg's optional drawtext filter.
GLYPHS = dict(zip("0123456789:.", (
    "111101101101111", "010110010010111", "111001111100111", "111001111001111",
    "101101111001001", "111100111001111", "111100111101111", "111001010010010",
    "111101111101111", "111101111001111", "000010000010000", "000000000000010",
)))


def frame_count(source):
    value = subprocess.check_output(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "V:0",
        "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(source)], text=True).strip()
    if not value.isdigit() or int(value) < 1:
        raise ValueError("source has no countable video frames")
    return int(value)


def ffmpeg(*args, **kwargs):
    return subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-nostats", *map(str, args)],
                          check=True, **kwargs)


def stamp(seconds):
    millis = round(seconds * 1000)
    hours, rem = divmod(millis, 3600000)
    minutes, rem = divmod(rem, 60000)
    sec, ms = divmod(rem, 1000)
    return f"{hours:02}:{minutes:02}:{sec:02}.{ms:03}"


def stamp_cell(pixels, cell, text):
    x = (cell % COLS) * CELL_WIDTH + 8
    y = (cell // COLS) * CELL_HEIGHT + IMAGE_HEIGHT + 3
    width = COLS * CELL_WIDTH
    for char in text:
        for index, bit in enumerate(GLYPHS[char]):
            if bit == "1":
                for dy in range(3):
                    offset = ((y + (index // 3) * 3 + dy) * width + x + (index % 3) * 3) * 3
                    pixels[offset:offset + 9] = b"\xff" * 9
        x += 12


def make_sheets(source, output, tmp, count, interval):
    if output.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise ValueError("use a .jpg or .png output")
    # Short clips still deserve an interior observation when no interval lands
    # near the middle. Do not duplicate that frame when it is already sampled.
    middle = f"+eq(n,{count // 2})*lt(t,{interval})" if count > 2 else ""
    select = f"select='isnan(prev_selected_t)+gte(t-prev_selected_t,{interval})+eq(n,{count-1}){middle}'"
    filters = (f"settb=AVTB,setpts=PTS-STARTPTS,{select},showinfo=checksum=0,"
               f"scale='min({CELL_WIDTH},{IMAGE_HEIGHT}*dar)':'min({IMAGE_HEIGHT},{CELL_WIDTH}/dar)',setsar=1,"
               f"pad={CELL_WIDTH}:{IMAGE_HEIGHT}:(ow-iw)/2:(oh-ih)/2,setsar=1,"
               f"pad={CELL_WIDTH}:{CELL_HEIGHT}:0:0,tile={COLS}x{ROWS}")
    log = tmp / "frames.log"
    with log.open("wb") as diagnostics:
        try:
            ffmpeg("-i", source, "-map", "0:V:0", "-vf", filters, "-fps_mode", "passthrough",
                   tmp / "%08d.ppm", stderr=diagnostics)
        except subprocess.CalledProcessError as exc:
            raise ValueError(log.read_text(errors="replace")[-1600:]) from exc
    times = []
    with log.open(errors="replace") as lines:
        for line in lines:
            match = re.search(r"Parsed_showinfo.*?\bn:\s*\d+\s+pts:\s*(-?\d+)\s+pts_time:", line)
            if match:
                times.append(int(match[1]) / 1_000_000)
    pages = sorted(tmp.glob("*.ppm"))
    per_page = COLS * ROWS
    if not times or len(pages) != math.ceil(len(times) / per_page):
        raise ValueError("FFmpeg returned incomplete contact sheets or timestamps")
    generated = []
    manifest = tmp / f"{output.stem}.csv"
    with manifest.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["source_file", "page_file", "cell", "source_time_s", "timecode"])
        for index, ppm in enumerate(pages):
            name = output.name if index == 0 else f"{output.stem}-{index+1:03d}{output.suffix}"
            header = f"P6\n{CELL_WIDTH*COLS} {CELL_HEIGHT*ROWS}\n255\n".encode()
            data = ppm.read_bytes()
            if not data.startswith(header) or len(data) != len(header) + CELL_WIDTH*COLS*CELL_HEIGHT*ROWS*3:
                raise ValueError("incomplete FFmpeg page raster")
            pixels = bytearray(data[len(header):])
            for cell, seconds in enumerate(times[index*per_page:(index+1)*per_page]):
                label = stamp(seconds)
                stamp_cell(pixels, cell, label)
                writer.writerow([source.name, name, cell+1, f"{seconds:.6f}", label])
            page = tmp / name
            ffmpeg("-v", "error", "-f", "image2pipe", "-c:v", "ppm", "-i", "pipe:0", "-frames:v", "1",
                   "-q:v", "2", page, input=header + pixels)
            generated.append(page)
    return generated + [manifest]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    sheets = sub.add_parser("sheets", help="write pages and a timecode CSV")
    sheets.add_argument("--interval", type=float, default=2.5)
    tail = sub.add_parser("tail", help="write the last decoded frame")
    for cmd in (sheets, tail):
        cmd.add_argument("source", type=Path)
        cmd.add_argument("output", type=Path)
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    try:
        if source == output:
            raise ValueError("source and output must be different files")
        count = frame_count(source)
        with tempfile.TemporaryDirectory(dir=output.parent) as directory:
            tmp = Path(directory)
            if args.action == "sheets":
                if not math.isfinite(args.interval) or args.interval <= 0:
                    raise ValueError("interval must be positive and finite")
                files = make_sheets(source, output, tmp, count, args.interval)
            else:
                if output.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
                    raise ValueError("use a .png or .jpg output")
                frame = tmp / output.name
                ffmpeg("-v", "error", "-i", source, "-map", "0:V:0", "-vf", f"select='eq(n,{count-1})'",
                       "-fps_mode", "passthrough", "-frames:v", "1", frame)
                check = ffmpeg("-v", "error", "-i", frame, "-vf", "scale=1:1", "-frames:v", "1",
                               "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1", stdout=subprocess.PIPE)
                if len(check.stdout) != 3:
                    raise ValueError("tail frame failed decode verification")
                files = [frame]
            # Publish the manifest last. Exclusive creation prevents two runs from
            # replacing each other's pages, even on a filesystem without hard links.
            created = []
            try:
                for artifact in files:
                    target = output.parent / artifact.name
                    with target.open("xb") as destination:
                        created.append(target)
                        with artifact.open("rb") as staged:
                            shutil.copyfileobj(staged, destination)
            except BaseException:
                for target in created:
                    target.unlink(missing_ok=True)
                raise
        print(f"Wrote {len(files)} file(s) in {output.parent}")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Reference extraction failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
