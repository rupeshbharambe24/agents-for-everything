"""LangGraph adapter wrapping any afe/v1 agent into a stateful graph node."""

from __future__ import annotations

from typing import Any, Callable

from agents_for_everything import AgentRunner, RunContext


def as_langgraph_node(
    agent_id: str,
    runner: AgentRunner | None = None,
    context: RunContext | None = None,
) -> Callable[[dict[str, Any]], dict[str, Any]]:
    """Return a LangGraph-compatible node callable `(state) -> updated_state`."""
    active_runner = runner or AgentRunner()

    def _node(state: dict[str, Any]) -> dict[str, Any]:
        result = active_runner.run(agent_id, state, context=context)
        return {**state, **result.output}

    _node.__name__ = f"afe_{agent_id.replace('/', '_').replace('-', '_')}"
    return _node
