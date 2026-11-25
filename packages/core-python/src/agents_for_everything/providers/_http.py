"""Shared stdlib JSON HTTP helper for LLM providers."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


class ProviderHTTPError(RuntimeError):
    """Raised when an upstream provider HTTP call fails."""


def post_json(
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    timeout_seconds: float = 30.0,
) -> dict[str, Any]:
    """POST JSON payload and decode JSON response using stdlib urllib."""
    body = json.dumps(payload).encode("utf-8")
    merged_headers = {"Content-Type": "application/json", **headers}
    req = urllib.request.Request(url=url, data=body, headers=merged_headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise ProviderHTTPError(f"HTTP {exc.code} from {url}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise ProviderHTTPError(f"Network error calling {url}: {exc.reason}") from exc


def extract_json_object(text: str) -> dict[str, Any] | None:
    """Extract JSON object from plain or fenced model text output."""
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 3:
            stripped = "\n".join(lines[1:-1]).strip()
    try:
        parsed = json.loads(stripped)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        start = stripped.find("{")
        end = stripped.rfind("}")
        if start != -1 and end > start:
            try:
                parsed = json.loads(stripped[start : end + 1])
                return parsed if isinstance(parsed, dict) else None
            except json.JSONDecodeError:
                return None
    return None
