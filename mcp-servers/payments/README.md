<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Payments & Billing Ledger MCP Server**

# 🧰 Payments & Billing Ledger MCP Server

![id: afe/payments](https://img.shields.io/badge/id-afe%2Fpayments-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Inspect payment transactions, subscriptions, and chargeback evidence without moving funds.

**Backed by:** stripe / billing read-only adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `lookup_transaction` | Fetch settled transaction metadata and dispute timestamps. | ✅ |
| `assemble_dispute_pack` | Gather delivery and auth evidence into a draft representment file. | ✅ |

## 🤖 Used by 1 agent

[`banking/dispute-chargeback-handler`](../../agents/industries/banking/dispute-chargeback-handler/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
