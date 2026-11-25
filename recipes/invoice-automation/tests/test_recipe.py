import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_invoice_auto_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class InvoiceAutomationTest(unittest.TestCase):
    def test_invoice_pipeline_and_s4_gate(self) -> None:
        sample = "Vendor: Acme Supplies\nInvoice #901\nSubtotal: INR 1000\nGST: INR 180\nTotal: INR 1180"
        res = _app.process_invoice_email("URGENT Invoice #901", sample, 1180.0, approve=False, provider_name="mock")
        self.assertTrue(res["invoice"]["math_valid"])
        self.assertTrue(res["accounts_payable"]["matched"])
        self.assertEqual(res["accounts_payable"]["status"], "queued_for_review")

        approved = _app.process_invoice_email("Invoice #901", sample, 1180.0, approve=True, provider_name="mock")
        self.assertEqual(approved["accounts_payable"]["status"], "approved_for_payment")


if __name__ == "__main__":
    unittest.main()
