from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["text"]).lower()
        pos = sum(1 for w in ("great", "love", "fast", "excellent", "good", "helpful") if w in low)
        neg = sum(1 for w in ("broken", "bad", "slow", "terrible", "angry", "failed") if w in low)
        if pos > neg:
            return {"sentiment": "positive", "score": 0.85}
        if neg > pos:
            return {"sentiment": "negative", "score": -0.8}
        if pos and neg:
            return {"sentiment": "mixed", "score": 0.0}
        return {"sentiment": "neutral", "score": 0.0}
