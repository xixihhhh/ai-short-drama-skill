import csv
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/dramake"
EXAMPLE = SKILL / "assets/examples/edit-handoff"


def command(*args):
    return subprocess.run(list(map(str, args)), capture_output=True, text=True)


def read_rows(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def change_csv(path, row, **edits):
    records = read_rows(path)
    records[row].update(edits)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def validate(script, directory, delivery=True):
    return command(sys.executable, script, *(["--delivery"] if delivery else []),
                   "--jobs", directory / "generation-jobs.csv", "--candidates", directory / "candidate-scorecard.csv",
                   "--timeline", directory / "edit-timeline.csv")


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg required")
class RealHandoffTests(unittest.TestCase):
    def test_review_and_geometry(self):
        cases = [
            ("candidate-scorecard.csv", 0, {"decision": "rejected"}, "accepted candidate"),
            ("edit-timeline.csv", 1, {"accepted_range_id": "R01:unknown"}, "accepted range"),
            ("edit-timeline.csv", 1, {"source_in_s": "29", "source_out_s": "34"}, "accepted range"),
            ("edit-timeline.csv", 0, {"source_out_s": "100", "speed": "33.333333333"}, "media duration"),
            ("candidate-scorecard.csv", 0, {"accepted_ranges": "opening=0-40;ending=30-35.75"}, "media duration"),
            ("edit-timeline.csv", 0, {"speed": "1"}, "timeline duration"),
            ("edit-timeline.csv", 0, {"speed": "nan"}, "finite"),
            ("edit-timeline.csv", 0, {"source_out_s": "inf"}, "finite"),
            ("edit-timeline.csv", 1, {"transition_in": "cut"}, "overlap"),
            ("edit-timeline.csv", 1, {"transition_in": "dissolve:2"}, "overlap"),
            ("edit-timeline.csv", 1, {"timeline_in_s": "3.5", "timeline_out_s": "8.5"}, "gap"),
            ("edit-timeline.csv", 1, {"source_uri": "missing.mp4"}, "missing media"),
            ("generation-jobs.csv", 0, {"output_sha256": "0"*64}, "SHA-256"),
            ("generation-jobs.csv", 0, {"output_uri": "other.mp4"}, "job output"),
            ("generation-jobs.csv", 0, {"accepted_ranges": "0-1"}, "job's accepted ranges"),
        ]
        for name, row, changes, reason in cases:
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as tmp:
                project = Path(tmp) / "project"
                shutil.copytree(EXAMPLE, project)
                change_csv(project / name, row, **changes)
                result = validate(ROOT / "scripts/validate_plan.py", project)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stdout + result.stderr)

    def test_legacy_ranges_and_draft_without_media(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            shutil.copytree(EXAMPLE, project)
            change_csv(project / "candidate-scorecard.csv", 0, accepted_ranges="0-6;30-35.75")
            for idx in range(2):
                change_csv(project / "edit-timeline.csv", idx, accepted_range_id=f"R01:{idx+1}")
            result = validate(SKILL / "scripts/validate_plan.py", project)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            (project / "reference.mp4").unlink()
            result = validate(SKILL / "scripts/validate_plan.py", project, delivery=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            result = validate(SKILL / "scripts/validate_plan.py", project)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing media", result.stdout)

    def test_installed_package_and_low_rate_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ROOT / "dist/dramake.skill") as package:
                package.extractall(tmp)
            installed = Path(tmp) / "dramake"
            example = installed / "assets/examples/edit-handoff"
            result = validate(installed / "scripts/validate_plan.py", example)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            helper = installed / "scripts/reference_frames.py"
            video = example / "reference.mp4"
            sheet = Path(tmp) / "review.jpg"
            result = command(sys.executable, helper, "sheets", video, sheet)
            self.assertEqual(result.returncode, 0, result.stderr)
            cells = read_rows(sheet.with_suffix(".csv"))
            self.assertEqual(len(cells), 16)
            self.assertEqual(cells[0]["timecode"], "00:00:00.000")
            self.assertEqual(cells[-1]["timecode"], "00:00:35.750")
            self.assertEqual(cells[-1]["page_file"], "review-002.jpg")
            # First page, first cell is blue; page two, cell four is the real red tail.
            for image, x, channel in [(sheet, 50, 2), (sheet.with_name("review-002.jpg"), 1010, 0)]:
                data = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(image), "-vf",
                    f"crop=4:4:{x}:50,scale=1:1", "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1"])
                self.assertGreater(data[channel], 220)
            tail = Path(tmp) / "tail.png"
            result = command(sys.executable, helper, "tail", video, tail)
            self.assertEqual(result.returncode, 0, result.stderr)
            pixel = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(tail), "-vf", "scale=1:1",
                                             "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1"])
            self.assertGreater(pixel[0], 220)

    def test_vfr_final_timestamp(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            video = directory / "irregular.mp4"
            result = command("ffmpeg", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=64x64:r=24:d=2",
                             "-vf", "select='eq(n,0)+eq(n,1)+eq(n,16)+eq(n,47)'", "-fps_mode", "vfr", video)
            self.assertEqual(result.returncode, 0, result.stderr)
            frames = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_frames", "-show_entries",
                "frame=best_effort_timestamp_time", "-of", "json", str(video)]))["frames"]
            times = [float(f["best_effort_timestamp_time"]) for f in frames]
            self.assertEqual(len(times), 4)
            self.assertGreater(times[-1] - times[-2], 1)
            helper = SKILL / "scripts/reference_frames.py"
            result = command(sys.executable, helper, "sheets", video, directory / "s.png")
            self.assertEqual(result.returncode, 0, result.stderr)
            cells = read_rows(directory / "s.csv")
            self.assertGreaterEqual(len(cells), 3)
            self.assertAlmostEqual(float(cells[-1]["source_time_s"]), times[-1] - times[0], places=5)
            result = command(sys.executable, helper, "tail", video, directory / "t.png")
            self.assertEqual(result.returncode, 0, result.stderr)
            def pixels(*args):
                return subprocess.check_output(["ffmpeg","-v","error",*map(str,args),
                    "-frames:v","1","-pix_fmt","rgb24","-f","rawvideo","pipe:1"])
            self.assertEqual(pixels("-i", directory/"t.png"), pixels("-i",video,"-vf","select='eq(n,3)'"))

if __name__ == "__main__":
    unittest.main()
