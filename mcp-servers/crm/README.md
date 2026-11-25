<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **CRM Operations MCP Server**

# 🧰 CRM Operations MCP Server

![id: afe/crm](https://img.shields.io/badge/id-afe%2Fcrm-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Read account records and prepare CRM updates with approval gates.

**Backed by:** hubspot / salesforce MCP adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `read_account` | Fetch lead/account records. | ✅ |
| `stage_update` | Prepare CRM field updates for review. |  |

## 🤖 Used by 6 agents

[`sales/account-researcher`](../../agents/business/sales/account-researcher/README.md), [`sales/crm-updater`](../../agents/business/sales/crm-updater/README.md), [`sales/inbound-qualifier`](../../agents/business/sales/inbound-qualifier/README.md), [`sales/lead-scorer`](../../agents/business/sales/lead-scorer/README.md), [`sales/pipeline-forecaster`](../../agents/business/sales/pipeline-forecaster/README.md), [`sales/quote-builder`](../../agents/business/sales/quote-builder/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
