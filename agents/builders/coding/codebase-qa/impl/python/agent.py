from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class CodebaseQAAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        docs = [{"title": f.get("path", "file"), "content": f.get("content", "")} for f in input_data.get("files", [])]
        res = runner.call_agent("search/semantic-search", {"query": input_data["question"], "documents": docs, "top_k": 2})
        matches = res.get("matches", [])
        refs = [m["title"] for m in matches if m.get("score", 0) > 0]
        ans = matches[0]["content"][:200] if refs else "No matching code found."
        return {"answer": ans, "files_referenced": refs}
