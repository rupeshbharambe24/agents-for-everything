from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class RewriterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        txt = " ".join(str(input_data["text"]).split())
        tone = str(input_data["tone"])
        return {"rewritten_text": txt, "tone": tone}
