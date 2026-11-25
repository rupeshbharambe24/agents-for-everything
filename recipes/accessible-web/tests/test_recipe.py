import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_a11y_web_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class AccessibleWebTest(unittest.TestCase):
    def test_screen_narration_and_voice_fill(self) -> None:
        form = {
            "id": "civic-form",
            "title": "Citizen Support",
            "fields": [
                {"id": "full_name", "label": "Full Name", "type": "string", "required": True},
                {"id": "city", "label": "City", "type": "string", "required": True},
                {"id": "pincode", "label": "PIN Code", "type": "string", "required": True},
            ],
        }
        res = _app.assist_web_session(
            "Page title: Citizen Portal; Submit button requires confirmation",
            form,
            "My name is Sneha Kulkarni, city Nashik, pincode 422001",
            locale="en-IN",
            confirm_submit=False,
            provider_name="mock",
        )
        self.assertIn("accessibility/accessibility-auditor", res["a11y_audit"]["result"])
        self.assertIn("accessibility/screen-narrator", res["narration"]["result"])
        self.assertEqual(res["form_state"]["status"], "awaiting_confirmation")
        self.assertEqual(res["form_state"]["values"]["full_name"], "Sneha Kulkarni")
        self.assertEqual(res["form_state"]["values"]["pincode"], "422001")

        submitted = _app.assist_web_session(
            "Page title: Citizen Portal",
            form,
            "My name is Sneha Kulkarni, city Nashik, pincode 422001",
            locale="en-IN",
            confirm_submit=True,
            provider_name="mock",
        )
        self.assertEqual(submitted["form_state"]["status"], "submitted")


if __name__ == "__main__":
    unittest.main()
