from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AnswerEngineAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        search = runner.call_agent("search/web-search", {"query": input_data["question"]})
        results = search.get("results", [])
        if not results:
            return {"answer": "No web results found.", "citations": []}
        first = results[0]
        notes = runner.call_agent("research/source-reader", {"url": first["url"], "content": first.get("snippet", "")})
        return {"answer": f"{notes['summary']} [1]", "citations": [{"source_id": "1", "title": first["title"], "url": first["url"], "quote": notes["summary"]}]}
