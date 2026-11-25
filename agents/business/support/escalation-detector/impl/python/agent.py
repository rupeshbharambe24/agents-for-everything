from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["message"]).lower()
        reasons = []
        if any(w in low for w in ("lawyer", "sue", "legal", "regulator")):
            reasons.append("legal_threat")
        if any(w in low for w in ("cancel", "churn", "unacceptable", "fraud")):
            reasons.append("high_churn_or_risk")
        return {"escalate": bool(reasons), "reasons": reasons}
