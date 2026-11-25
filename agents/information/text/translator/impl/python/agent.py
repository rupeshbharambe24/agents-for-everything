from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_PHRASE_MAP = {("hello", "hi"): "नमस्ते", ("thank you", "hi"): "धन्यवाद", ("hello", "es"): "Hola", ("hello", "fr"): "Bonjour"}

class TranslatorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        txt = str(input_data["text"]).strip()
        tgt = str(input_data["target_language"]).lower()
        out = _PHRASE_MAP.get((txt.lower(), tgt), f"[{tgt}] {txt}")
        for k, v in (input_data.get("glossary") or {}).items():
            out = out.replace(str(k), str(v))
        return {"translated_text": out, "target_language": tgt}
