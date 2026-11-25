from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class BrowserOperatorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        page_text = str(input_data.get("page_text") or "")
        if page_text:
            inj = runner.call_agent("guardrails/prompt-injection-detector", {"content": page_text})
            if not inj.get("is_safe", True):
                return {"status": "halted_prompt_injection", "trace_steps": ["Blocked untrusted page instruction"], "injection_safe": False}
        nav = runner.call_tool("afe/browser", {"action": "navigate", "url": input_data["start_url"]})
        if "submit" in str(input_data["goal"]).lower():
            runner.require_approval("submit", f"Confirm submit for {input_data['start_url']}")
        return {"status": nav.get("status", "ok"), "trace_steps": [f"Opened {input_data['start_url']}", f"Goal evaluated: {input_data['goal']}"], "injection_safe": True}
