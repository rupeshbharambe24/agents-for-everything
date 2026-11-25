<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Chat with Your Docs**

# 🍳 Chat with Your Docs

![recipe: chat-with-your-docs](https://img.shields.io/badge/recipe-chat--with--your--docs-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square)

> Private document Q&A assistant with PII masking, chunk ingestion, semantic retrieval, and grounding checks.

| | |
|---|---|
| **Problem** | Teams need answers from internal handbooks and policies without leaking PII or accepting unverified claims. |
| **Solution** | Composes pii-redactor, knowledge-ingestor, rag-qa, and hallucination-checker. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`guardrails/pii-redactor`](../../agents/core/guardrails/pii-redactor/README.md) | Detects and masks personal data (emails, phones, Aadhaar, PAN, SSN, card numbers) reversibly. | S0 |
| [`memory/knowledge-ingestor`](../../agents/core/memory/knowledge-ingestor/README.md) | Parses, chunks, and prepares documents for hybrid keyword + vector indexing with metadata. | S2 |
| [`search/semantic-search`](../../agents/information/search/semantic-search/README.md) | Hybrid keyword + vector search over private document corpora with top-k ranking. | S1 |
| [`search/rag-qa`](../../agents/information/search/rag-qa/README.md) | Answers questions over private documents with citations and refuses when unsupported. | S1 |
| [`guardrails/hallucination-checker`](../../agents/core/guardrails/hallucination-checker/README.md) | Checks each claim in an answer against provided sources and flags unsupported statements. | S0 |

**Teams:** [`document-intake`](../../teams/document-intake/README.md)

**MCP servers:** [`afe/documents`](../../mcp-servers/documents/README.md), [`afe/vector-store`](../../mcp-servers/vector-store/README.md)

<!-- afe:end-generated -->

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/chat-with-your-docs/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/chat-with-your-docs/tests/test_recipe.py
```
