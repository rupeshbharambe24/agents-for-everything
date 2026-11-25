from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class WebSearchAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_tool("afe/web-search", input_data)
        seen_urls: set[str] = set()
        deduped = []
        for item in res.get("results", []):
            url = item.get("url", "")
            if url not in seen_urls:
                seen_urls.add(url)
                deduped.append(item)
        return {"query": input_data["query"], "results": deduped}
