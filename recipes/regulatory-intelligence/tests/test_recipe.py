import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_reg_intel_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class RegulatoryIntelligenceTest(unittest.TestCase):
    def test_circular_impact_pipeline(self) -> None:
        res = _app.assess_circular(
            "Updated Digital Lending Disclosure Circular",
            "Mandates Key Fact Statement in borrower language.",
            provider_name="mock",
        )
        self.assertIn("banking/regulatory-circular-tracker", res["tracked"]["result"])
        self.assertIn("legal/compliance-monitor", res["compliance"]["result"])
        self.assertIn("research/policy-analyst", res["analysis"]["result"])
        self.assertTrue(len(res["briefing_report"]["report_markdown"]) > 10)
        self.assertGreaterEqual(res["briefing_report"]["section_count"], 1)


if __name__ == "__main__":
    unittest.main()
