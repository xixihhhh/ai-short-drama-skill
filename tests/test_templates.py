import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_evals_are_valid_and_sufficient(self):
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "continuity-director")
        self.assertGreaterEqual(len(data["evals"]), 3)
        self.assertEqual(len({item["id"] for item in data["evals"]}), len(data["evals"]))

    def test_skill_is_concise(self):
        lines = (ROOT / "skills/continuity-director/SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lines), 500)

    def test_template_columns(self):
        path = ROOT / "skills/continuity-director/assets/templates/continuity-ledger.csv"
        with path.open(newline="", encoding="utf-8") as handle:
            headers = next(csv.reader(handle))
        for required in ("block_id", "accepted_parent_clip", "character_identity", "entry_state", "exit_state", "physical_contact_points"):
            self.assertIn(required, headers)

    def test_provider_neutrality_is_explicit(self):
        text = (ROOT / "skills/continuity-director/SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("provider-neutral", text)
        self.assertIn("do not require atlas cloud", text)

    def test_skill_frontmatter_and_general_scope(self):
        text = (ROOT / "skills/continuity-director/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: continuity-director\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertIn("description:", frontmatter)
        for scope in ("live-action", "animated dramas", "branded narrative"):
            self.assertIn(scope, frontmatter)

    def test_required_general_profiles_exist(self):
        text = (ROOT / "skills/continuity-director/references/content-profiles.md").read_text(encoding="utf-8")
        for profile in ("Live-action human drama", "Pet or animal-led story", "Animation or motion comic", "Branded narrative"):
            self.assertIn(profile, text)


if __name__ == "__main__":
    unittest.main()
