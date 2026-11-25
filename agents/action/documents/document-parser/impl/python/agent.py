from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class DocumentParserAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_tool("afe/documents", {"document": input_data["document"]})
        md = str(res.get("markdown", ""))
        sections = [line.lstrip("# ").strip() for line in md.splitlines() if line.strip().startswith("#")]
        return {"markdown": md, "sections": sections or ["Body"], "char_count": len(md)}
