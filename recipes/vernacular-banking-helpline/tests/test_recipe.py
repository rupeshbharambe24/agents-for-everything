import importlib.util
import unittest
from pathlib import Path

from agents_for_everything.safety import ApprovalRequiredError

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_vbh_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class VernacularBankingHelplineTest(unittest.TestCase):
    def test_helpline_and_approval_gate(self) -> None:
        res = _app.handle_banking_call(
            "Mera UPI PIN scam SMS aya hai",
            locale="hi-IN",
            suspicious_message="Verify KYC now at http://example.invalid",
            file_grievance=False,
            provider_name="mock",
        )
        self.assertTrue(res["ai_disclosed"])
        self.assertEqual(res["locale"], "hi-IN")
        self.assertIn("banking/banking-voice-assistant", res["banking_reply"]["result"])
        self.assertIsNotNone(res["scam_check"])

        with self.assertRaises(ApprovalRequiredError):
            _app.handle_banking_call(
                "Escalate unauthorized charge grievance",
                locale="te-IN",
                file_grievance=True,
                auto_approve=False,
                provider_name="mock",
            )

        approved = _app.handle_banking_call(
            "Escalate unauthorized charge grievance",
            locale="te-IN",
            file_grievance=True,
            auto_approve=True,
            provider_name="mock",
        )
        self.assertEqual(approved["grievance"]["status"], "approved")


if __name__ == "__main__":
    unittest.main()
