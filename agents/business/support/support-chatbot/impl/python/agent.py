from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class SupportChatbotAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        rag = runner.call_agent("search/rag-qa", {"question": input_data["question"], "documents": input_data["kb_docs"]})
        supported = bool(rag.get("supported"))
        return {"answer": rag["answer"], "handoff_needed": not supported, "citations": rag.get("citations", [])}
