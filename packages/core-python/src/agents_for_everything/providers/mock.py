"""Deterministic offline mock provider for testing and CI."""

from __future__ import annotations

import json
from typing import Any

from .base import BaseModelProvider, CompletionRequest, CompletionResponse, ProviderConfig


def _default_for_schema(prop: dict[str, Any], user_payload: dict[str, Any], key: str) -> Any:
    if key in user_payload:
        return user_payload[key]
    if "enum" in prop and prop["enum"]:
        return prop["enum"][0]
    if "default" in prop:
        return prop["default"]
    ptype = prop.get("type", "string")
    if ptype == "string":
        if "text" in user_payload and isinstance(user_payload["text"], str):
            return user_payload["text"][:200]
        return f"mock_{key}"
    if ptype == "boolean":
        return True
    if ptype in {"integer", "number"}:
        return prop.get("minimum", 1)
    if ptype == "array":
        return []
    if ptype == "object":
        return {}
    return None


class MockProvider(BaseModelProvider):
    """Offline deterministic provider used by default in tests and CI."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        super().__init__(config or ProviderConfig(name="mock", model="afe-mock-v1"))

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        schema = request.output_schema or {}
        props = schema.get("properties", {})
        result: dict[str, Any] = {}
        for key in schema.get("required", []):
            result[key] = _default_for_schema(props.get(key, {}), request.user_payload, key)
        for key, prop in props.items():
            if key not in result and key in request.user_payload:
                result[key] = request.user_payload[key]
        if not result:
            result = {"summary": "Mock completion executed.", "input_echo": request.user_payload}
        serialized = json.dumps(result)
        return CompletionResponse(
            content=serialized,
            parsed_json=result,
            model=self.config.model,
            provider="mock",
            input_tokens=max(1, len(request.system_prompt) // 4),
            output_tokens=max(1, len(serialized) // 4),
            cost_usd=0.0,
        )
