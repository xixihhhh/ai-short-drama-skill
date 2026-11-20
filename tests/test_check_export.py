import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "skills/dramake/scripts/check_export.py"
spec = importlib.util.spec_from_file_location("check_export", SCRIPT)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class ExportTests(unittest.TestCase):
    def check_video(self, streams, layout=None, audio=False, srt=None):
        data = json.dumps({"streams": streams, "format": {"duration": "10"}})
        response = subprocess.CompletedProcess([], 0, stdout=data, stderr="")
        with patch.object(check.subprocess, "run", return_value=response):
            return check.inspect_export(Path("sample.mp4"), layout, audio, srt)

    def test_rotation_and_sample_aspect(self):
        video = {"codec_type": "video", "width": 720, "height": 720, "sample_aspect_ratio": "2:1",
                 "side_data_list": [{"rotation": -90}]}
        self.assertIn("portrait (1/2)", self.check_video([video, {"codec_type": "audio"}], "portrait", True))
        with self.assertRaisesRegex(ValueError, "expected landscape"):
            self.check_video([video], "landscape")
        with self.assertRaisesRegex(ValueError, "audio track"):
            self.check_video([video], audio=True)

    def test_audio_album_cover_is_not_a_movie(self):
        with self.assertRaisesRegex(ValueError, "no video"):
            self.check_video([{"codec_type": "audio"}, {"codec_type": "video", "disposition": {"attached_pic": 1}}])

    def test_cues_match_video_duration_even_with_longer_audio(self):
        video = {"codec_type": "video", "width": 10, "height": 10, "duration": "2.0"}
        with tempfile.TemporaryDirectory() as tmp:
            srt = Path(tmp) / "subs.srt"
            srt.write_bytes("\ufeff1\r\n00:00:00,000 --> 00:00:02,000\r\n你好\r\n第二行\r\n".encode())
            self.assertIn("1 SRT cue", self.check_video([video], srt=srt))
            srt.write_text("1\n00:00:01,000 --> 00:00:02,001\nCena", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "cue 1"):
                self.check_video([video], srt=srt)

    def test_malformed_subtitles(self):
        with tempfile.TemporaryDirectory() as tmp:
            srt = Path(tmp) / "sub.srt"
            for source in ("", "1\n00:00:02,000 --> 00:00:01,000\ntext", "00:00:00,000 --> 00:00:01,000",
                           "00:00:00,000 --> 00:00:01,000\none\n2\n00:00:01,000 --> 00:00:02,000\ntwo"):
                with self.subTest(source=source):
                    srt.write_text(source, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        check.check_subtitles(srt, 3000)
