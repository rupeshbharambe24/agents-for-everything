from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class SpeechToTextAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_tool("afe/stt", {"audio": input_data["audio"], "locale": input_data.get("locale", "en")})
        return {"text": res.get("text", ""), "language": res.get("language", input_data.get("locale", "en")), "confidence": res.get("confidence", 0.95), "segments": res.get("segments", [])}
