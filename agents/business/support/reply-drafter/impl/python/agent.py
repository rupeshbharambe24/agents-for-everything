from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ReplyDrafterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        rag = runner.call_agent("search/rag-qa", {"question": input_data["ticket_text"], "documents": input_data["kb_docs"]})
        draft = f"Hello,\n\n{rag['answer']}\n\nPlease let us know if we can help further."
        return {"draft_reply": draft, "grounded": bool(rag.get("supported"))}
