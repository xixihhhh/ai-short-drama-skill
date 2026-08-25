import csv
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    @staticmethod
    def write_template_rows(destination: Path, template: Path, rows: list[dict[str, str]]) -> None:
        with template.open(newline="", encoding="utf-8") as handle:
            headers = next(csv.reader(handle))
        with destination.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def test_evals_are_valid_and_sufficient(self):
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "dramake")
        self.assertGreaterEqual(len(data["evals"]), 16)
        self.assertEqual(len({item["id"] for item in data["evals"]}), len(data["evals"]))
        for item in data["evals"]:
            self.assertTrue(item.get("prompt"))
            self.assertTrue(item.get("expected_output"))

    def test_skill_is_concise(self):
        lines = (ROOT / "skills/dramake/SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lines), 500)

    def test_high_density_douyin_pacing_preset(self):
        chinese = (ROOT / "skills/dramake/references/story-and-pacing.md").read_text(encoding="utf-8")
        english = (ROOT / "skills/dramake/references/en/story-and-pacing.md").read_text(encoding="utf-8")
        for marker in ("3 秒", "10 秒", "18–24", "15–25", "4–7", "固定宏观目标", "不等于一句台词、一次切镜或一个生成请求"):
            self.assertIn(marker, chinese)
        for marker in ("3 seconds", "10 seconds", "18–24", "15–25", "4–7", "macro goal", "does not equal one line, one cut, or one generation request"):
            self.assertIn(marker, english)

    def test_wan3_reference_dialogue_route_has_real_constraints(self):
        chinese = (ROOT / "skills/dramake/references/model-router.md").read_text(encoding="utf-8")
        english = (ROOT / "skills/dramake/references/en/model-router.md").read_text(encoding="utf-8")
        for marker in ("Wan 3 参考驱动对白长段", "Audio 1 → 角色 A", "无非叙事背景音乐", "互斥", "输入视频总时长 + 输出时长 ≤ 30 秒", "参考素材表达的是控制意图，不是保证"):
            self.assertIn(marker, chinese)
        for marker in ("Wan 3 reference-driven long dialogue blocks", "Audio 1 → Character A", "no non-diegetic background music", "mutually exclusive", "input-video duration plus output duration", "References express control intent, not a guarantee"):
            self.assertIn(marker, english)

    def test_template_columns(self):
        path = ROOT / "skills/dramake/assets/templates/continuity-ledger.csv"
        with path.open(newline="", encoding="utf-8") as handle:
            headers = next(csv.reader(handle))
        for required in ("block_id", "accepted_parent_clip", "character_identity", "entry_state", "exit_state", "physical_contact_points"):
            self.assertIn(required, headers)

    def test_directing_voice_and_audio_templates(self):
        templates = ROOT / "skills/dramake/assets/templates"
        required_by_file = {
            "block-manifest.csv": (
                "scene_id", "parent_block_id", "aspect_ratio", "directorial_intention",
                "internal_shots", "camera_motivation", "reference_authority", "voice_ids",
            ),
            "shot-plan.csv": (
                "shot_id", "value_before", "value_after", "camera_start", "camera_end",
                "subject_endpoint", "audio_in", "audio_out",
            ),
            "voice-bible.csv": (
                "voice_id", "character_id", "pitch_center_range", "speaking_rate",
                "reference_asset", "forbidden_cross_bindings",
            ),
            "audio-continuity.csv": (
                "voice_id", "ambience_in", "ambience_out", "bgm_phrase_in",
                "bgm_phrase_out", "reverb_tail", "loudness_target",
            ),
        }
        for filename, required in required_by_file.items():
            with (templates / filename).open(newline="", encoding="utf-8") as handle:
                headers = next(csv.reader(handle))
            for column in required:
                self.assertIn(column, headers, f"{filename} missing {column}")

    def test_execution_platform_is_user_selectable(self):
        text = (ROOT / "skills/dramake/SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("不绑定单一平台", text)
        self.assertIn("执行平台由用户选择", text)

    def test_skill_frontmatter_and_general_scope(self):
        text = (ROOT / "skills/dramake/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: dramake\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertIn("description:", frontmatter)
        for scope in ("真人", "动画/漫剧", "品牌剧情"):
            self.assertIn(scope, frontmatter)

    def test_required_general_profiles_exist(self):
        text = (ROOT / "skills/dramake/references/content-profiles.md").read_text(encoding="utf-8")
        for profile in ("真人剧情", "宠物/动物主角", "动画/漫剧", "品牌/产品剧情"):
            self.assertIn(profile, text)

    def test_chinese_default_and_english_mirror_exist(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")
        for phrase in ("文字", "抖音", "红果短剧", "横屏", "竖屏", "Dramake"):
            self.assertIn(phrase, readme)
        for phrase in ("From Text to Final Cut", "Douyin", "Hongguo Short Drama", "Dramake"):
            self.assertIn(phrase, english)
        self.assertTrue((ROOT / "skills/dramake/SKILL.en.md").is_file())

    def test_no_removed_platform_or_acknowledgement_copy(self):
        forbidden = ("atlas" + " cloud", "third-party" + " notices", "workflow" + " landscape")
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "dist" in path.parts or "tests" in path.parts:
                continue
            if path.suffix.lower() not in {".md", ".json", ".py", ".yaml", ".yml", ".csv", ".cff"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for phrase in forbidden:
                self.assertNotIn(phrase, text, f"{phrase!r} found in {path}")

    def test_bilingual_docs_and_versions_are_synchronized(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts/check_bilingual.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_empty_templates_pass_full_validator(self):
        templates = ROOT / "skills/dramake/assets/templates"
        command = [
            "python3", str(ROOT / "scripts/validate_plan.py"),
            "--continuity", str(templates / "continuity-ledger.csv"),
            "--block-manifest", str(templates / "block-manifest.csv"),
            "--shot-plan", str(templates / "shot-plan.csv"),
            "--voice-bible", str(templates / "voice-bible.csv"),
            "--audio-continuity", str(templates / "audio-continuity.csv"),
            "--cost", str(templates / "cost-plan.csv"),
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_complete_valid_plan_passes_cross_file_validator(self):
        templates = ROOT / "skills/dramake/assets/templates"
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            paths = {name: tmp_path / name for name in (
                "continuity-ledger.csv", "block-manifest.csv", "shot-plan.csv",
                "voice-bible.csv", "audio-continuity.csv", "cost-plan.csv",
            )}
            base_state = {
                "scene_id": "S1", "character_identity": "HERO", "wardrobe_or_surface": "blue coat",
                "phone_or_prop_orientation": "front", "voice_ids": "V1", "audio_in": "room tone",
                "audio_out": "room tone", "open_motion_vectors": "walking right",
                "physical_contact_points": "hand-door", "reanchor_source": "hero-master.png",
            }
            self.write_template_rows(paths["continuity-ledger.csv"], templates / "continuity-ledger.csv", [
                {**base_state, "block_id": "B01", "status": "accepted", "entry_state": "hero outside",
                 "exit_state": "hero inside", "observed_exit_state": "hero inside", "tail_frame": "B01_tail.png"},
                {**base_state, "block_id": "B02", "status": "planned", "accepted_parent_clip": "B01",
                 "entry_state": "hero inside", "exit_state": "hero seated"},
            ])
            block_base = {
                "scene_id": "S1", "aspect_ratio": "9:16", "location_time": "room-day",
                "generated_duration_s": "10", "edit_beats": "2", "internal_shots": "2",
                "arc_position": "rising", "directorial_intention": "turn caution into trust",
                "capability_needs": "native-dialogue", "selected_route": "runtime-choice",
                "reference_authority": "identity=hero-master.png", "dialogue_route": "native",
                "voice_ids": "V1", "audio_in": "room tone", "audio_out": "room tone",
                "physical_contact_points": "hand-door", "camera_start": "medium", "camera_path": "push",
                "camera_motivation": "reveal decision", "camera_end": "close", "subject_endpoint": "stable look",
                "transition_in": "action", "transition_out": "eyeline", "reanchor_required": "false",
            }
            self.write_template_rows(paths["block-manifest.csv"], templates / "block-manifest.csv", [
                {**block_base, "block_id": "B01", "purpose": "hook", "value_before": "safe",
                 "value_after": "concerned", "entry_state": "hero outside", "exit_state": "hero inside",
                 "candidate_status": "accepted", "observed_exit_state": "hero inside", "tail_frame": "B01_tail.png"},
                {**block_base, "block_id": "B02", "parent_block_id": "B01", "purpose": "turn",
                 "value_before": "concerned", "value_after": "trusting", "entry_state": "hero inside",
                 "exit_state": "hero seated", "candidate_status": "planned"},
            ])
            shot_base = {
                "scene_id": "S1", "directorial_intention": "turn caution into trust",
                "narrative_job": "advance choice", "subject_action": "opens door",
                "listener_or_world_reaction": "room quiets", "camera_start": "medium", "camera_path": "push",
                "camera_motivation": "reveal decision", "camera_end": "close", "subject_endpoint": "stable look",
                "screen_direction": "left-to-right", "reference_authority": "identity=hero-master.png",
                "dialogue_or_sound": "short line", "audio_in": "room tone", "audio_out": "room tone",
                "physical_contact_points": "hand-door", "transition_in": "action", "transition_out": "eyeline",
                "status": "planned",
            }
            self.write_template_rows(paths["shot-plan.csv"], templates / "shot-plan.csv", [
                {**shot_base, "shot_id": "SH01", "block_id": "B01", "edit_beat": "1", "start_s": "0", "end_s": "5", "value_before": "safe", "value_after": "alert"},
                {**shot_base, "shot_id": "SH02", "block_id": "B01", "edit_beat": "2", "start_s": "5", "end_s": "10", "value_before": "alert", "value_after": "concerned"},
                {**shot_base, "shot_id": "SH03", "block_id": "B02", "edit_beat": "1", "start_s": "0", "end_s": "5", "value_before": "concerned", "value_after": "hopeful"},
                {**shot_base, "shot_id": "SH04", "block_id": "B02", "edit_beat": "2", "start_s": "5", "end_s": "10", "value_before": "hopeful", "value_after": "trusting"},
            ])
            self.write_template_rows(paths["voice-bible.csv"], templates / "voice-bible.csv", [{
                "voice_id": "V1", "character_id": "HERO", "language": "zh-CN", "accent": "standard",
                "timbre": "warm", "pitch_center_range": "mid", "speaking_rate": "fast",
                "emotional_baseline": "restrained", "rights_status": "owned", "forbidden_cross_bindings": "none",
            }])
            audio_base = {
                "scene_id": "S1", "active_speaker": "HERO", "voice_id": "V1", "dialogue_status": "planned",
                "ambience_in": "room tone", "ambience_out": "room tone", "bgm_phrase_in": "cue-a",
                "bgm_phrase_out": "cue-a", "sfx_sync_cue": "door latch", "reverb_tail": "small room",
                "loudness_target": "-16 LUFS", "reference_audio_owner": "V1", "post_action": "mix",
                "qa_status": "planned",
            }
            self.write_template_rows(paths["audio-continuity.csv"], templates / "audio-continuity.csv", [
                {**audio_base, "block_id": "B01"}, {**audio_base, "block_id": "B02"},
            ])
            self.write_template_rows(paths["cost-plan.csv"], templates / "cost-plan.csv", [{
                "route_id": "R1", "provider": "runtime-choice", "model": "capability-route",
                "quality_mode": "balanced", "authorization_mode": "approved-batch", "duration_s": "10",
                "resolution": "720p", "blocks": "2", "candidates": "1", "unit_price": "0.05",
                "currency": "USD", "retry_factor": "1.5", "cap_requests": "3", "price_checked_at": "2026-08-25",
            }])
            command = ["python3", str(ROOT / "scripts/validate_plan.py")]
            for flag, filename in (
                ("--continuity", "continuity-ledger.csv"), ("--block-manifest", "block-manifest.csv"),
                ("--shot-plan", "shot-plan.csv"), ("--voice-bible", "voice-bible.csv"),
                ("--audio-continuity", "audio-continuity.csv"), ("--cost", "cost-plan.csv"),
            ):
                command.extend((flag, str(paths[filename])))
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validator_rejects_unaccepted_parent_and_sparse_long_block(self):
        continuity_headers = (ROOT / "skills/dramake/assets/templates/continuity-ledger.csv").read_text(encoding="utf-8").strip()
        block_headers = (ROOT / "skills/dramake/assets/templates/block-manifest.csv").read_text(encoding="utf-8").strip()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            continuity = tmp_path / "continuity.csv"
            blocks = tmp_path / "blocks.csv"
            continuity.write_text(
                continuity_headers + "\n"
                "B01,S1,generated,,room,day,left-to-right,hero,blue coat,standing,phone,front,dry,left,V1,room,room,,hand to phone,start,end,,,,\n"
                "B02,S1,ready,B01,room,day,left-to-right,hero,blue coat,standing,phone,front,dry,left,V1,room,room,,hand to phone,start,end,,,,\n",
                encoding="utf-8",
            )
            blocks.write_text(
                block_headers + "\n"
                "B01,S1,,hook,,9:16,room,30,1,1,open,create tension,safe,threatened,start,end,long,route,identity=image1,native,V1,room,room,hand-phone,wide,push,reveal,close,phone raised,cut,match,false,planned,,,,\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                ["python3", str(ROOT / "scripts/validate_plan.py"), "--continuity", str(continuity), "--block-manifest", str(blocks)],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("requires accepted parent", result.stdout)
            self.assertIn("at least 4 edit beats", result.stdout)

    def test_validator_rejects_cross_file_voice_and_shot_errors(self):
        templates = ROOT / "skills/dramake/assets/templates"
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            blocks = tmp_path / "blocks.csv"
            shots = tmp_path / "shots.csv"
            voices = tmp_path / "voices.csv"
            blocks.write_text(
                (templates / "block-manifest.csv").read_text(encoding="utf-8").strip() + "\n"
                "B01,S1,,hook,,9:16,room,10,2,1,open,reveal fear,safe,unsafe,start,end,long,route,identity=hero,native,V_MISSING,room,room,hand-phone,wide,push,reveal,close,phone raised,cut,match,false,planned,,,,\n",
                encoding="utf-8",
            )
            shots.write_text(
                (templates / "shot-plan.csv").read_text(encoding="utf-8").strip() + "\n"
                "SH01,S1,B01,beat1,0,12,reveal,reveal fear,safe,unsafe,raise phone,listener reacts,medium,wide,push,reveal,close,phone raised,left,identity=hero,line,room,room,hand-phone,cut,match,planned,\n",
                encoding="utf-8",
            )
            voices.write_text(
                (templates / "voice-bible.csv").read_text(encoding="utf-8").strip() + "\n"
                "V1,HERO,zh-CN,standard,,adult female,warm,mid,fast,low,calm,urgent,close mic,,,none,\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    "python3", str(ROOT / "scripts/validate_plan.py"),
                    "--block-manifest", str(blocks),
                    "--shot-plan", str(shots),
                    "--voice-bible", str(voices),
                ],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("unknown voice_id", result.stdout)
            self.assertIn("shot exceeds parent block duration", result.stdout)


if __name__ == "__main__":
    unittest.main()
