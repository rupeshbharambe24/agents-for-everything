from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ChatSummarizerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        msgs = input_data.get("messages", [])
        decisions, asks = [], []
        for m in msgs:
            txt = str(m.get("text", "")).strip()
            if any(k in txt.lower() for k in ("decided", "agreed", "approved", "ship")):
                decisions.append(txt)
            if "?" in txt or "please" in txt.lower():
                asks.append(txt)
        return {"summary": f"Summarized {len(msgs)} messages ({len(decisions)} decisions, {len(asks)} asks).", "decisions": decisions, "asks": asks}
