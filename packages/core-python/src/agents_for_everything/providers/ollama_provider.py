"""Local-first Ollama provider (`/api/chat`)."""

from __future__ import annotations

import json
import os

from ._http import extract_json_object, post_json
from .base import BaseModelProvider, CompletionRequest, CompletionResponse, ProviderConfig


class OllamaProvider(BaseModelProvider):
    """Calls a local or on-prem Ollama daemon."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        cfg = config or ProviderConfig(
            name="ollama",
            model=os.environ.get("AFE_MODEL", "llama3.2"),
            base_url=os.environ.get("OLLAMA_HOST", "http://localhost:11434"),
        )
        super().__init__(cfg)

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        base = (self.config.base_url or "http://localhost:11434").rstrip("/")
        payload: dict[str, object] = {
            "model": self.config.model,
            "stream": False,
            "options": {"temperature": request.temperature},
            "messages": [
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": json.dumps(request.user_payload, ensure_ascii=False)},
            ],
        }
        if request.output_schema is not None:
            payload["format"] = "json"
        data = post_json(
            f"{base}/api/chat",
            payload,
            {},
            timeout_seconds=self.config.timeout_seconds,
        )
        text = data.get("message", {}).get("content", "")
        return CompletionResponse(
            content=text,
            parsed_json=extract_json_object(text),
            model=self.config.model,
            provider="ollama",
            input_tokens=int(data.get("prompt_eval_count", 0)),
            output_tokens=int(data.get("eval_count", 0)),
        )
