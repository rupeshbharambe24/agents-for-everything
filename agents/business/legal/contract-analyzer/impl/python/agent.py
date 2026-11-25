from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["contract_text"]).lower()
        flags = []
        if "unlimited liability" in low:
            flags.append("unlimited_liability")
        if "auto-renew" in low or "automatic renewal" in low:
            flags.append("auto_renewal")
        if "uncapped indemnity" in low or "indemnify" in low:
            flags.append("indemnity_review")
        risk = "high" if "unlimited_liability" in flags else ("medium" if flags else "low")
        return {"flagged_clauses": flags, "risk_level": risk}
