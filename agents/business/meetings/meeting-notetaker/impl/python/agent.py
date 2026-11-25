from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class MeetingNotetakerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        tr = runner.call_agent("voice/speech-to-text", {"audio": input_data["audio"]})
        sm = runner.call_agent("text/summarizer", {"text": tr["text"], "style": "bullets"})
        return {"summary": sm["summary"], "key_points": sm["key_points"], "transcript": tr}
