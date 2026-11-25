from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class RagQAAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_agent("search/semantic-search", {"query": input_data["question"], "documents": input_data["documents"], "top_k": 3})
        matches = [m for m in res.get("matches", []) if m.get("score", 0) > 0]
        if not matches:
            return {"answer": "I don't know based on the provided documents.", "citations": [], "supported": False}
        top = matches[0]
        return {"answer": top["content"], "citations": [{"source_id": top["id"], "title": top["title"], "quote": top["content"][:180]}], "supported": True}
