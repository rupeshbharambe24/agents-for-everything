from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        hist = list(input_data["history"])
        limit = int(input_data.get("max_items", 5))
        kept = hist[-limit:] if limit > 0 else []
        return {"compact_context": kept, "dropped_count": max(0, len(hist) - len(kept))}
