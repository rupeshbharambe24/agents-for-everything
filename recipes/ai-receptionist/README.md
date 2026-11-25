<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **AI Receptionist**

# 🍳 AI Receptionist

![recipe: ai-receptionist](https://img.shields.io/badge/recipe-ai--receptionist-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square)

> Phone and messaging receptionist that answers FAQs from KB and proposes appointment slots.

| | |
|---|---|
| **Problem** | Small clinics and businesses miss inbound calls and booking messages after hours. |
| **Solution** | Composes phone-call-agent, business-messaging-bot, rag-qa, and meeting-scheduler with clear AI disclosure. |

## 🚀 Run it

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/ai-receptionist/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/ai-receptionist/tests/test_recipe.py
```

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`voice/phone-call-agent`](../../agents/perception/voice/phone-call-agent/README.md) | Inbound/outbound telephony assistant for bookings and reminders with mandatory AI disclosure. | S3 |
| [`communication/business-messaging-bot`](../../agents/business/communication/business-messaging-bot/README.md) | Handles opted-in customer messaging over WhatsApp/SMS with templates and human handoff. | S3 |
| [`search/rag-qa`](../../agents/information/search/rag-qa/README.md) | Answers questions over private documents with citations and refuses when unsupported. | S1 |
| [`meetings/meeting-scheduler`](../../agents/business/meetings/meeting-scheduler/README.md) | Finds conflict-free meeting slots across calendars and prepares invites for approval. | S3 |

**Teams:** [`voice-concierge`](../../teams/voice-concierge/README.md)

**MCP servers:** [`afe/telephony`](../../mcp-servers/telephony/README.md), [`afe/chat`](../../mcp-servers/chat/README.md), [`afe/vector-store`](../../mcp-servers/vector-store/README.md), [`afe/calendar`](../../mcp-servers/calendar/README.md)

<!-- afe:end-generated -->
