import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_chief_of_staff_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class PersonalChiefOfStaffTest(unittest.TestCase):
    def test_morning_brief_pipeline(self) -> None:
        out = _app.build_morning_brief(
            [{"id": "1", "subject": "URGENT signoff", "body": "Need reply ASAP"}],
            "TODO: Prepare weekly release checklist",
            ["User prefers concise bullets and English/Hindi priorities"],
            provider_name="mock",
        )
        self.assertEqual(out["urgent_emails"], 1)
        self.assertIn("release checklist", out["top_focus"])
        self.assertGreaterEqual(len(out["memories"]), 1)


if __name__ == "__main__":
    unittest.main()
