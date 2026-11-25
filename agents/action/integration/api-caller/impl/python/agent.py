from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class APICallerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        method = str(input_data["method"]).upper()
        url = str(input_data["url"])
        if method != "GET":
            runner.require_approval("write_request", f"{method} {url}")
        res = runner.call_tool("afe/http", {"url": url, "method": method, "mock_body": {"ok": True}})
        return {"status_code": int(res.get("status_code", 200)), "method": method, "url": url, "response": res.get("content")}
