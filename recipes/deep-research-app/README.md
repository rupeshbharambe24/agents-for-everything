<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Deep Research App**

# 🍳 Deep Research App

![recipe: deep-research-app](https://img.shields.io/badge/recipe-deep--research--app-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square)

> Cited deep-research application running planning, web search, reading, fact-checking, and grounding verification.

| | |
|---|---|
| **Problem** | Manual multi-source investigation is slow and error-prone without source tracking and claim verification. |
| **Solution** | Composes research-team, deep-researcher, answer-engine, and hallucination-checker. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`orchestration/task-planner`](../../agents/core/orchestration/task-planner/README.md) | Breaks a goal into ordered, dependency-aware steps with success criteria and estimated cost. | S0 |
| [`search/web-search`](../../agents/information/search/web-search/README.md) | Runs queries on search APIs, deduplicates URLs, and ranks results with snippets. | S1 |
| [`search/answer-engine`](../../agents/information/search/answer-engine/README.md) | Searches web sources, reads content, and synthesizes a direct cited answer. | S1 |
| [`research/source-reader`](../../agents/information/research/source-reader/README.md) | Reads one URL or document deeply and extracts key points, facts, and quotes. | S1 |
| [`research/fact-checker`](../../agents/information/research/fact-checker/README.md) | Verifies discrete claims against web or retrieved sources and outputs verdicts with evidence. | S1 |
| [`research/report-writer`](../../agents/information/research/report-writer/README.md) | Turns research findings into structured Markdown reports with executive summaries and references. | S0 |
| [`research/deep-researcher`](../../agents/information/research/deep-researcher/README.md) | Plans research questions, searches iteratively, reads sources, fact-checks, and writes a cited report. | S1 |
| [`guardrails/hallucination-checker`](../../agents/core/guardrails/hallucination-checker/README.md) | Checks each claim in an answer against provided sources and flags unsupported statements. | S0 |

**Teams:** [`research-team`](../../teams/research-team/README.md)

**MCP servers:** [`afe/web-search`](../../mcp-servers/web-search/README.md), [`afe/http`](../../mcp-servers/http/README.md), [`afe/documents`](../../mcp-servers/documents/README.md)

<!-- afe:end-generated -->

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/deep-research-app/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/deep-research-app/tests/test_recipe.py
```
