<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **ERP & Procurement Ledger MCP Server**

# 🧰 ERP & Procurement Ledger MCP Server

![id: afe/erp](https://img.shields.io/badge/id-afe%2Ferp-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Read purchase requisitions and inventory levels, and stage draft POs for human approval.

**Backed by:** open-erp-mcp adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `read_inventory` | Query stock levels, reorder points, and lead times. | ✅ |
| `stage_purchase_order` | Prepare a draft purchase order awaiting human sign-off. |  |

## 🤖 Used by 3 agents

[`hospitality/housekeeping-optimizer`](../../agents/industries/hospitality/housekeeping-optimizer/README.md), [`hospitality/reservation-agent`](../../agents/industries/hospitality/reservation-agent/README.md), [`supply-chain/purchase-order-agent`](../../agents/business/supply-chain/purchase-order-agent/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
