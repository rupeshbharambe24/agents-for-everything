import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_ai_qa_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class AIQAEngineerTest(unittest.TestCase):
    def test_staging_qa_pipeline(self) -> None:
        out = _app.inspect_staging_app("https://staging.example.org", "<main><h1>App</h1></main>", provider_name="mock")
        self.assertTrue(out["navigation"]["injection_safe"])
        self.assertIn("web-tester", out["tests"])
        self.assertIn("accessibility-auditor", out["accessibility"])


if __name__ == "__main__":
    unittest.main()
