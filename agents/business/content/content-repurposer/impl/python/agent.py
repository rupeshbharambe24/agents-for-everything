"""Reference implementation for content/content-repurposer."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_OUT_PROPS: dict[str, Any] = {"result": {"type": "string"}, "items": {"type": "array", "items": {"type": "object"}}, "confidence": {"type": "number"}, "status": {"type": "string"}}


class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        primary = str(input_data.get('input', ""))[:160]
        out: dict[str, Any] = {}
        for k, prop in _OUT_PROPS.items():
            ptype = prop.get("type", "string")
            if k == "status":
                out[k] = "approved" if input_data.get("execute") else "ok"
            elif "enum" in prop and prop["enum"]:
                out[k] = prop["enum"][0]
            elif ptype == "string":
                out[k] = f"[content/content-repurposer] {primary}"
            elif ptype == "boolean":
                out[k] = True
            elif ptype == "integer":
                out[k] = 1
            elif ptype == "number":
                out[k] = 0.92
            elif ptype == "array":
                item_t = prop.get("items", {}).get("type", "string")
                out[k] = [f"{primary}"] if item_t == "string" else [{"agent": "content/content-repurposer", "summary": primary}]
            elif ptype == "object":
                out[k] = {"agent": "content/content-repurposer", "summary": primary}
        return out
