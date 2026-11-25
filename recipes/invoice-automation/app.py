"""End-to-end Invoice Automation recipe."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

RECIPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = RECIPE_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import AgentRunner, RunContext  # noqa: E402


def process_invoice_email(
    email_subject: str,
    invoice_text: str,
    po_total: float,
    approve: bool = False,
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, auto_approve=approve)

    triage = runner.run(
        "communication/inbox-triager",
        {"emails": [{"id": "mail-1", "subject": email_subject, "body": invoice_text}]},
        context=ctx,
    ).output
    parsed = runner.run("documents/invoice-receipt-parser", {"text": invoice_text}, context=ctx).output
    ap = runner.run(
        "finance/accounts-payable",
        {
            "invoice_total": parsed["total"],
            "po_total": po_total,
            "vendor": parsed["vendor"],
            "approve": approve,
        },
        context=ctx,
    ).output
    return {"triage": triage["triaged"][0], "invoice": parsed, "accounts_payable": ap}


if __name__ == "__main__":
    sample = "Vendor: Acme Supplies\nInvoice #901\nSubtotal: INR 1000\nGST: INR 180\nTotal: INR 1180"
    print(json.dumps(process_invoice_email("URGENT Invoice #901", sample, 1180.0), indent=2))
