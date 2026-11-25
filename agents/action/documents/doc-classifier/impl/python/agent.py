from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["text"]).lower()
        if any(k in low for k in ("invoice", "gst", "subtotal")):
            dt = "invoice"
        elif any(k in low for k in ("agreement", "indemnity", "nda", "clause")):
            dt = "contract"
        elif any(k in low for k in ("opening balance", "debit", "credit", "bank statement")):
            dt = "bank_statement"
        elif any(k in low for k in ("passport", "aadhaar", "driver license")):
            dt = "id_document"
        elif any(k in low for k in ("experience", "education", "skills", "curriculum vitae")):
            dt = "resume"
        else:
            dt = "other"
        return {"doc_type": dt, "confidence": 0.92}
