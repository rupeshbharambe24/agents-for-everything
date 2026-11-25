from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        recs = []
        savings = 0.0
        for r in input_data["resources"]:
            cpu = float(r.get("avg_cpu_pct", 50))
            cost = float(r.get("monthly_usd", 0))
            if cpu < 10 and cost > 0:
                save = round(cost * 0.5, 2)
                savings += save
                recs.append({"id": r.get("id", "res"), "action": "downsize_or_stop", "savings_usd": save})
        return {"recommendations": recs, "estimated_monthly_savings_usd": round(savings, 2)}
