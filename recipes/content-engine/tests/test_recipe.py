import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_content_engine_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class ContentEngineTest(unittest.TestCase):
    def test_content_repurposing_pipeline(self) -> None:
        out = _app.repurpose_episode("Composable Agents", "Atomic agents snap together cleanly via JSON Schemas.", provider_name="mock")
        self.assertIn("podcast-producer", out["podcast"])
        self.assertIn("editor", out["blog_edited"])
        self.assertIn("social-post-writer", out["social_post"])
        self.assertIn("clip-generator", out["clips"])


if __name__ == "__main__":
    unittest.main()
