<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Vernacular Banking Helpline**

# 🍳 Vernacular Banking Helpline

![recipe: vernacular-banking-helpline](https://img.shields.io/badge/recipe-vernacular--banking--helpline-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square)

> Local-language voice helpline for banking FAQs, suspicious SMS/UPI scam verification, and grievance filing with human escalation.

| | |
|---|---|
| **Problem** | Regional-language banking customers struggle with English-only IVR menus, scam verification, and formal complaint filing. |
| **Solution** | Composes realtime-voice-assistant, banking-voice-assistant, scam-message-checker, and grievance-redressal under S4 audit & approval gates. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`voice/realtime-voice-assistant`](../../agents/perception/voice/realtime-voice-assistant/README.md) | Full-duplex speech assistant with low latency, interruption handling, and tool dispatch. | S1 |
| [`banking/banking-voice-assistant`](../../agents/industries/banking/banking-voice-assistant/README.md) | Voice-first help for balances, FAQs and services in local languages, authenticated through the bank's own systems. | S4 |
| [`banking/scam-message-checker`](../../agents/industries/banking/scam-message-checker/README.md) | Consumers forward a suspicious SMS, call script or payment request and get a risk verdict with what to do. | S1 |
| [`banking/grievance-redressal`](../../agents/industries/banking/grievance-redressal/README.md) | Classifies complaints, tracks turnaround times, drafts responses and prepares escalation files. | S3 |

**MCP servers:** [`afe/telephony`](../../mcp-servers/telephony/README.md), [`afe/stt`](../../mcp-servers/stt/README.md), [`afe/tts`](../../mcp-servers/tts/README.md), [`afe/compliance-reg`](../../mcp-servers/compliance-reg/README.md)

<!-- afe:end-generated -->

> **Regulated Safeguard:** Runs cleanly with local/on-prem open-weights models (`ollama`), discloses AI assistance, and gates S3/S4 grievance submission or banking actions behind explicit human approval.

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/vernacular-banking-helpline/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/vernacular-banking-helpline/tests/test_recipe.py
```
