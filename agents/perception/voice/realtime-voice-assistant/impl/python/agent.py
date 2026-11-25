from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class RealtimeVoiceAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        locale = str(input_data.get("locale", "en"))
        stt = runner.call_agent("voice/speech-to-text", {"audio": input_data["audio"], "locale": locale})
        cmd = runner.call_agent("voice/voice-command", {"transcript": stt["text"], "actions": ["answer_question", "fill_form", "stop"]})
        reply = f"Heard ({cmd['action']}): {stt['text']}" if not input_data.get("barge_in") else f"Switched on barge-in: {stt['text']}"
        tts = runner.call_agent("voice/text-to-speech", {"text": reply, "locale": locale})
        return {"reply_text": reply, "audio_uri": tts["audio_uri"], "interrupted": bool(input_data.get("barge_in", False))}
