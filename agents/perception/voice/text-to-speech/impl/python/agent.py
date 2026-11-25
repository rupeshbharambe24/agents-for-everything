from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TextToSpeechAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        # S0 pure synthesis spec uses deterministic metadata output
        text = str(input_data["text"]).strip()
        locale = str(input_data.get("locale", "en"))
        return {"audio_uri": "afe://generated/speech.wav", "spoken_text": text, "locale": locale, "duration_seconds": round(max(0.4, len(text.split()) * 0.35), 2)}
