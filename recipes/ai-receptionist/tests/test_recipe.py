import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_ai_receptionist_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class AIReceptionistTest(unittest.TestCase):
    def test_faq_and_booking_proposal(self) -> None:
        res = _app.handle_inbound_inquiry(
            "What are your clinic hours?",
            [{"title": "Hours", "content": "Open 9 AM to 6 PM Mon-Sat."}],
            "guest@example.org",
            ["2026-11-26T10:00Z"],
            confirm_booking=False,
            provider_name="mock",
        )
        self.assertTrue(res["ai_disclosed"])
        self.assertIn("9 AM", res["faq_answer"])
        self.assertEqual(res["booking"]["status"], "slots_proposed")


if __name__ == "__main__":
    unittest.main()
