from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TicketTriagerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["ticket_text"]).lower()
        if "refund" in low or "invoice" in low or "charged" in low:
            cat, queue = "billing", "billing-ops"
        elif "crash" in low or "500" in low or "error" in low:
            cat, queue = "technical", "eng-support"
        else:
            cat, queue = "general", "tier1-support"
        prio = "urgent" if any(w in low for w in ("outage", "urgent", "fraud", "down")) else "medium"
        return {"category": cat, "priority": prio, "queue": queue}
