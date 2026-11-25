"""Knowledge Ingestor implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class KnowledgeIngestorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        chunk_size = int(input_data.get("chunk_size", 400))
        chunks: list[dict[str, Any]] = []
        for d_idx, doc in enumerate(input_data.get("documents", [])):
            doc_id = doc.get("id") or f"doc-{d_idx + 1}"
            title = doc.get("title") or doc_id
            content = str(doc.get("content", "")).strip()
            if not content:
                continue
            for pos in range(0, len(content), chunk_size):
                piece = content[pos : pos + chunk_size].strip()
                if piece:
                    chunks.append({"chunk_id": f"{doc_id}#{len(chunks)+1}", "doc_id": doc_id, "title": title, "content": piece})
        return {"chunks": chunks, "count": len(chunks)}
