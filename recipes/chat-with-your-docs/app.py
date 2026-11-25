"""End-to-end Chat with Your Docs recipe."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

RECIPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = RECIPE_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import AgentRunner, RunContext  # noqa: E402


def ask_docs(
    question: str,
    documents: list[dict[str, Any]],
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    sanitized_docs = []
    for doc in documents:
        red = runner.run("guardrails/pii-redactor", {"text": doc.get("content", "")}, context=ctx).output
        sanitized_docs.append({**doc, "content": red["redacted_text"]})

    ingested = runner.run(
        "memory/knowledge-ingestor",
        {"documents": sanitized_docs, "chunk_size": 300},
        context=ctx,
    ).output
    rag = runner.run(
        "search/rag-qa",
        {"question": question, "documents": ingested["chunks"]},
        context=ctx,
    ).output
    hal = runner.run(
        "guardrails/hallucination-checker",
        {"answer": rag["answer"], "sources": [c["content"] for c in ingested["chunks"]]},
        context=ctx,
    ).output
    return {
        "answer": rag["answer"],
        "citations": rag.get("citations", []),
        "supported": rag.get("supported", False),
        "grounded": hal.get("grounded", False),
    }


if __name__ == "__main__":
    docs = json.loads((RECIPE_DIR / "fixtures" / "sample_docs.json").read_text(encoding="utf-8"))
    print(json.dumps(ask_docs("What is the refund policy?", docs), indent=2))
