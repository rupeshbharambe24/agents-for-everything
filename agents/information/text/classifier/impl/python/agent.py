from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TextClassifierAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        txt = set(re.findall(r"[a-z0-9]+", str(input_data["text"]).lower()))
        labels = [str(l) for l in input_data["labels"]]
        best, best_score = labels[0], -1
        for lbl in labels:
            ltoks = set(re.findall(r"[a-z0-9]+", lbl.lower()))
            score = len(txt & ltoks)
            if score > best_score:
                best, best_score = lbl, score
        return {"label": best, "confidence": 0.9 if best_score > 0 else 0.55}
