<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Personal Chief of Staff**

# 🍳 Personal Chief of Staff

![recipe: personal-chief-of-staff](https://img.shields.io/badge/recipe-personal--chief--of--staff-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square)

> Generates a daily briefing across urgent email, meeting prep, prioritized tasks, and memory recall.

| | |
|---|---|
| **Problem** | Professionals start mornings juggling fragmented email threads, meeting notes, and tasks. |
| **Solution** | Composes daily-briefer, inbox-triager, meeting-prep, task-manager, and memory-retriever. |

## 🚀 Run it

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/personal-chief-of-staff/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/personal-chief-of-staff/tests/test_recipe.py
```

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`productivity/daily-briefer`](../../agents/life/productivity/daily-briefer/README.md) | Assembles a morning brief from calendar events, top tasks, urgent mail, and weather. | S1 |
| [`communication/inbox-triager`](../../agents/business/communication/inbox-triager/README.md) | Sorts, prioritizes, and labels emails; surfaces urgent threads and reply-needed items. | S1 |
| [`meetings/meeting-prep`](../../agents/business/meetings/meeting-prep/README.md) | Compiles pre-meeting briefs on attendees, prior threads, open items, and suggested agenda. | S1 |
| [`productivity/task-manager`](../../agents/life/productivity/task-manager/README.md) | Captures tasks from notes, chat, or voice, prioritizes them, and structures a daily plan. | S2 |
| [`memory/memory-retriever`](../../agents/core/memory/memory-retriever/README.md) | Recalls relevant memories for the current task, ranked and deduplicated. | S1 |

**Teams:** [`chief-of-staff`](../../teams/chief-of-staff/README.md)

**MCP servers:** [`afe/calendar`](../../mcp-servers/calendar/README.md), [`afe/email`](../../mcp-servers/email/README.md), [`afe/memory-store`](../../mcp-servers/memory-store/README.md)

<!-- afe:end-generated -->
