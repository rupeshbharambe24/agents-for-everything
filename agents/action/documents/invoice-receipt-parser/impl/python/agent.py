from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class InvoiceReceiptParserAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        txt = str(input_data["text"])
        vendor_m = re.search(r"Vendor:\s*(.+)", txt, re.I)
        inv_m = re.search(r"Invoice\s*#?:?\s*([A-Za-z0-9-]+)", txt, re.I)
        sub_m = re.search(r"\bSubtotal:\s*(?:INR|USD|\$|₹)?\s*([0-9]+(?:\.[0-9]+)?)", txt, re.I)
        tax_m = re.search(r"\b(?:Tax|GST|VAT):\s*(?:INR|USD|\$|₹)?\s*([0-9]+(?:\.[0-9]+)?)", txt, re.I)
        tot_m = re.search(r"\bTotal:\s*(?:INR|USD|\$|₹)?\s*([0-9]+(?:\.[0-9]+)?)", txt, re.I)

        sub = float(sub_m.group(1)) if sub_m else 0.0
        tax = float(tax_m.group(1)) if tax_m else 0.0
        tot = float(tot_m.group(1)) if tot_m else sub + tax
        math_ok = abs((sub + tax) - tot) < 0.01 if (sub_m and tot_m) else True
        return {"vendor": vendor_m.group(1).strip() if vendor_m else "Unknown Vendor", "invoice_number": inv_m.group(1) if inv_m else "N/A", "subtotal": sub, "tax": tax, "total": tot, "math_valid": math_ok}
