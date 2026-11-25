from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        buf: list[str] = []
        for u in input_data["utterances"]:
            s = str(u).strip()
            if "delete last" in s.lower() and buf:
                buf.pop()
            else:
                buf.append(s)
        return {"text": " ".join(buf)}
