from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class VoiceCommandAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        txt = str(input_data["transcript"]).lower()
        actions = [str(a) for a in input_data.get("actions", [])]
        tokens = set(re.findall(r"[a-z0-9]+", txt))
        best, best_score = (actions[0] if actions else "unknown"), 0.0
        for act in actions:
            a_toks = set(re.findall(r"[a-z0-9]+", act.lower()))
            score = len(tokens & a_toks) / max(1, len(a_toks))
            if score > best_score:
                best, best_score = act, score
        return {"action": best, "arguments": {"raw": input_data["transcript"]}, "confidence": round(max(0.4, best_score), 2)}
