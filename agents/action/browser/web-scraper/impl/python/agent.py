from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class WebScraperAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        runner.call_tool("afe/http", {"url": input_data["url"]})
        rows = list(input_data.get("html_rows") or [{"title": "Sample item", "url": input_data["url"]}])
        return {"url": input_data["url"], "records": rows, "count": len(rows)}
