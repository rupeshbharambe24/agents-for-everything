"""Lightweight local MCP tool registry and built-in sandbox-safe handlers."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Callable

ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


class LocalMCPRegistry:
    """Dispatches MCP server tool calls declared by `afe` agents."""

    def __init__(self, workspace_root: Path | None = None) -> None:
        self.workspace_root = (workspace_root or Path.cwd()).resolve()
        self._handlers: dict[str, ToolHandler] = {}
        self._register_builtin_handlers()

    def register(self, server_id: str, handler: ToolHandler) -> None:
        self._handlers[server_id] = handler

    def call(self, server_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        if server_id not in self._handlers:
            return {"status": "unavailable", "server": server_id, "payload": payload}
        return self._handlers[server_id](payload)

    def available_servers(self) -> list[str]:
        return sorted(self._handlers.keys())

    def _register_builtin_handlers(self) -> None:
        self.register("afe/stt", self._handle_stt)
        self.register("afe/tts", self._handle_tts)
        self.register("afe/ocr", self._handle_ocr)
        self.register("afe/web-search", self._handle_web_search)
        self.register("afe/http", self._handle_http)
        self.register("afe/browser", self._handle_browser)
        self.register("afe/filesystem", self._handle_filesystem)
        self.register("afe/documents", self._handle_documents)
        self.register("afe/vector-store", self._handle_vector_store)
        self.register("afe/sql", self._handle_sql)
        self.register("afe/python-sandbox", self._handle_python_sandbox)
        self.register("afe/shell-sandbox", self._handle_shell_sandbox)
        self.register("afe/email", self._handle_email)
        self.register("afe/calendar", self._handle_calendar)
        self.register("afe/chat", self._handle_chat)

    def _handle_stt(self, payload: dict[str, Any]) -> dict[str, Any]:
        audio = payload.get("audio") or payload
        text = audio.get("transcript_hint") or payload.get("text") or ""
        locale = audio.get("locale_hint") or payload.get("locale") or "en"
        return {
            "text": text.strip(),
            "language": locale,
            "confidence": 0.96 if text else 0.0,
            "segments": [{"start_ms": 0, "end_ms": 1500, "text": text.strip(), "confidence": 0.96}]
            if text
            else [],
        }

    def _handle_tts(self, payload: dict[str, Any]) -> dict[str, Any]:
        text = str(payload.get("text", ""))
        locale = str(payload.get("locale", "en"))
        return {
            "audio_uri": "afe://generated/speech.wav",
            "format": "wav",
            "locale": locale,
            "duration_seconds": round(max(0.5, len(text.split()) * 0.4), 2),
            "spoken_text": text,
        }

    def _handle_ocr(self, payload: dict[str, Any]) -> dict[str, Any]:
        image = payload.get("image") or payload
        text = image.get("text_hint") or payload.get("text") or ""
        return {"text": text, "blocks": [{"text": line} for line in text.splitlines() if line.strip()]}

    def _handle_web_search(self, payload: dict[str, Any]) -> dict[str, Any]:
        query = str(payload.get("query", "")).strip()
        fixtures = payload.get("fixtures")
        if isinstance(fixtures, list):
            return {"query": query, "results": fixtures}
        return {
            "query": query,
            "results": [
                {
                    "id": "res-1",
                    "title": f"Overview: {query}" if query else "Search Result",
                    "url": "https://example.org/reference",
                    "snippet": f"Reference summary for {query}.",
                    "score": 0.92,
                }
            ],
        }

    def _handle_http(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "url": payload.get("url", ""),
            "status_code": 200,
            "content": payload.get("mock_body", ""),
        }

    def _handle_browser(self, payload: dict[str, Any]) -> dict[str, Any]:
        action = payload.get("action", "fill")
        return {
            "action": action,
            "url": payload.get("url", "about:blank"),
            "filled_fields": payload.get("fields", {}),
            "submitted": False,
            "status": "awaiting_confirmation" if action == "fill" else "ok",
        }

    def _handle_filesystem(self, payload: dict[str, Any]) -> dict[str, Any]:
        op = payload.get("op", "list")
        rel_path = str(payload.get("path", "."))
        target = (self.workspace_root / rel_path).resolve()
        if not str(target).startswith(str(self.workspace_root)):
            return {"error": "path escapes workspace root"}
        if op == "list" and target.is_dir():
            return {"entries": sorted(p.name for p in target.iterdir())}
        if op == "read" and target.is_file():
            return {"content": target.read_text(encoding="utf-8", errors="replace")}
        return {"op": op, "path": rel_path, "status": "dry_run"}

    def _handle_documents(self, payload: dict[str, Any]) -> dict[str, Any]:
        doc = payload.get("document") or payload
        content = doc.get("content") or ""
        return {"markdown": content, "char_count": len(content)}

    def _handle_vector_store(self, payload: dict[str, Any]) -> dict[str, Any]:
        query = str(payload.get("query", "")).lower()
        docs = payload.get("documents", [])
        ranked: list[dict[str, Any]] = []
        terms = [t for t in query.split() if len(t) > 2]
        for idx, doc in enumerate(docs):
            text = doc.get("content", "") if isinstance(doc, dict) else str(doc)
            title = doc.get("title", f"Doc {idx + 1}") if isinstance(doc, dict) else f"Doc {idx + 1}"
            score = sum(1 for t in terms if t in text.lower())
            ranked.append({"id": str(idx + 1), "title": title, "content": text, "score": score})
        ranked.sort(key=lambda item: item["score"], reverse=True)
        return {"matches": ranked[: int(payload.get("top_k", 5))]}

    def _handle_sql(self, payload: dict[str, Any]) -> dict[str, Any]:
        query = str(payload.get("query", "")).strip()
        if not query.lower().startswith("select"):
            return {"error": "read-only SQL server permits SELECT queries only"}
        db_path = payload.get("sqlite_path", ":memory:")
        conn = sqlite3.connect(db_path)
        try:
            cur = conn.execute(query)
            cols = [d[0] for d in cur.description] if cur.description else []
            rows = [dict(zip(cols, row)) for row in cur.fetchall()]
            return {"columns": cols, "rows": rows}
        except sqlite3.Error as exc:
            return {"error": str(exc)}
        finally:
            conn.close()

    def _handle_python_sandbox(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"status": "sandbox_ready", "note": "use explicit safe transforms", "payload": json.dumps(payload)}

    def _handle_shell_sandbox(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"command": payload.get("command", ""), "status": "requires_approval", "exit_code": None}

    def _handle_email(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"status": "draft_saved", "draft": payload}

    def _handle_calendar(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"status": "proposed_slots", "slots": payload.get("slots", [])}

    def _handle_chat(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"status": "draft_message", "message": payload}
