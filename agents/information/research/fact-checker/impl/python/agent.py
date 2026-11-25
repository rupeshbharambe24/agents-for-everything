from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class FactCheckerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        verdicts = []
        for claim in input_data["claims"]:
            res = runner.call_agent("search/web-search", {"query": claim})
            verdicts.append({"claim": claim, "verdict": "supported" if res.get("results") else "unverified", "evidence": res.get("results", [])[:1]})
        return {"verdicts": verdicts}
