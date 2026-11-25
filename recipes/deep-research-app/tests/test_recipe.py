"""Integration test for recipes/deep-research-app."""

import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_deep_research_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)
run_research = _app.run_research


class DeepResearchRecipeTest(unittest.TestCase):
    def test_deep_research_pipeline(self) -> None:
        out = run_research("Model Context Protocol adoption", provider_name="mock")
        self.assertIn("# Model Context Protocol adoption", out["report_markdown"])
        self.assertGreaterEqual(len(out["citations"]), 1)
        self.assertGreaterEqual(out["verified_claims"], 1)
        self.assertTrue(out["grounded"])


if __name__ == "__main__":
    unittest.main()
