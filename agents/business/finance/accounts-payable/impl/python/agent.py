from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        inv = float(input_data["invoice_total"])
        po = float(input_data["po_total"])
        var = round(inv - po, 2)
        matched = abs(var) < 0.01
        if input_data.get("approve"):
            runner.require_approval("approve_payment_batch", f"Approve AP bill for {input_data['vendor']} ({inv})")
            return {"matched": matched, "variance": var, "status": "approved_for_payment"}
        return {"matched": matched, "variance": var, "status": "queued_for_review"}
