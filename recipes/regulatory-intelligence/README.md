<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Regulatory Intelligence Digest**

# 🍳 Regulatory Intelligence Digest

![recipe: regulatory-intelligence](https://img.shields.io/badge/recipe-regulatory--intelligence-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square)

> Daily regulator circular monitoring mapped to internal compliance policies, impacted owners, and briefing reports.

| | |
|---|---|
| **Problem** | Compliance officers manually read central bank circulars and legislative bulletins to spot obligation changes. |
| **Solution** | Composes the regulatory-watch team across regulatory-circular-tracker, compliance-monitor, policy-analyst, and report-writer. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`banking/regulatory-circular-tracker`](../../agents/industries/banking/regulatory-circular-tracker/README.md) | Tracks central bank circulars and regulatory notices and maps impacted internal processes. | S1 |
| [`legal/compliance-monitor`](../../agents/business/legal/compliance-monitor/README.md) | Tracks regulatory notices across jurisdictions and maps updates to internal obligations. | S1 |
| [`research/policy-analyst`](../../agents/information/research/policy-analyst/README.md) | Analyzes a regulation or policy proposal: who it affects and how. | S1 |
| [`research/report-writer`](../../agents/information/research/report-writer/README.md) | Turns research findings into structured Markdown reports with executive summaries and references. | S0 |

**Teams:** [`regulatory-watch`](../../teams/regulatory-watch/README.md)

**MCP servers:** [`afe/news-api`](../../mcp-servers/news-api/README.md), [`afe/documents`](../../mcp-servers/documents/README.md), [`afe/compliance-reg`](../../mcp-servers/compliance-reg/README.md)

<!-- afe:end-generated -->

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/regulatory-intelligence/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/regulatory-intelligence/tests/test_recipe.py
```
