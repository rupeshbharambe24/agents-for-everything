from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class SourceReaderAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        content = str(input_data.get("content") or "").strip()
        if not content and input_data.get("url"):
            fetched = runner.call_tool("afe/http", {"url": input_data["url"], "mock_body": f"Reference article at {input_data['url']}."})
            content = str(fetched.get("content", "")).strip()
        sents = [s.strip() for s in content.split(".") if s.strip()]
        return {"summary": content[:240] or "Empty source.", "key_points": sents[:3] or [content], "quotes": sents[:1]}
