<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Regulatory, Sanctions & Public Schemes MCP Server**

# 🧰 Regulatory, Sanctions & Public Schemes MCP Server

![id: afe/compliance-reg](https://img.shields.io/badge/id-afe%2Fcompliance--reg-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Screen entities against published watchlists and inspect public statutory scheme eligibility rules.

**Backed by:** open-sanctions / official-gazette index adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `screen_watchlist` | Perform explained transliteration-aware watchlist name matching. | ✅ |
| `check_scheme_rules` | Evaluate deterministic statutory eligibility criteria. | ✅ |

## 🤖 Used by 7 agents

[`banking/banking-voice-assistant`](../../agents/industries/banking/banking-voice-assistant/README.md), [`banking/loan-application-assistant`](../../agents/industries/banking/loan-application-assistant/README.md), [`banking/model-risk-validator`](../../agents/industries/banking/model-risk-validator/README.md), [`banking/scam-message-checker`](../../agents/industries/banking/scam-message-checker/README.md), [`government/gov-form-assistant`](../../agents/industries/government/gov-form-assistant/README.md), [`government/public-consultation-analyzer`](../../agents/industries/government/public-consultation-analyzer/README.md), [`government/scheme-eligibility-checker`](../../agents/industries/government/scheme-eligibility-checker/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
