<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **AI QA Engineer**

# 🍳 AI QA Engineer

![recipe: ai-qa-engineer](https://img.shields.io/badge/recipe-ai--qa--engineer-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square)

> Inspects a staging URL, screens pages for prompt injection, checks accessibility, and drafts bug issues.

| | |
|---|---|
| **Problem** | Manual staging smoke tests miss accessibility regressions and layout errors. |
| **Solution** | Composes web-navigator, web-tester, accessibility-auditor, and issue-triager. |

## 🚀 Run it

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/ai-qa-engineer/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/ai-qa-engineer/tests/test_recipe.py
```

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`browser/web-navigator`](../../agents/action/browser/web-navigator/README.md) | Completes multi-step web tasks safely using accessibility trees and screenshots with injection guards. | S3 |
| [`browser/web-tester`](../../agents/action/browser/web-tester/README.md) | Walks through staging web flows, generates Playwright checks, and captures bug reports. | S2 |
| [`accessibility/accessibility-auditor`](../../agents/perception/accessibility/accessibility-auditor/README.md) | Checks HTML/UI attributes against WCAG contrast, alt-text, and landmark rules. | S1 |
| [`coding/issue-triager`](../../agents/builders/coding/issue-triager/README.md) | Labels, deduplicates, and prioritizes repository issues and asks for missing repro steps. | S3 |

**Teams:** [`web-qa-team`](../../teams/web-qa-team/README.md)

**MCP servers:** [`afe/browser`](../../mcp-servers/browser/README.md), [`afe/issue-tracker`](../../mcp-servers/issue-tracker/README.md)

<!-- afe:end-generated -->
