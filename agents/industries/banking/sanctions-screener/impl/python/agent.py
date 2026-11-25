from __future__ import annotations
from difflib import SequenceMatcher
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if input_data.get("confirm"):
            runner.require_approval("compliance_officer_clearance", f"Clear sanctions screening for {input_data['name']}")
        target = str(input_data["name"]).lower().strip()
        hits = []
        for w in input_data.get("watchlist", []):
            ratio = SequenceMatcher(None, target, str(w).lower().strip()).ratio()
            if ratio >= 0.78:
                hits.append(str(w))
        return {"hit": bool(hits), "matched_entries": hits, "explanation": f"Fuzzy similarity matched {len(hits)} list entries for human review."}
