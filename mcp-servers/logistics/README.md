<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Logistics, Carrier & Customs MCP Server**

# 🧰 Logistics, Carrier & Customs MCP Server

![id: afe/logistics](https://img.shields.io/badge/id-afe%2Flogistics-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Track multi-carrier shipments, delivery exception codes, and HS tariff lookups.

**Backed by:** multi-carrier tracking & HS lookup adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `track_shipment` | Fetch milestone scan events and delay alerts for a waybill. | ✅ |
| `lookup_hs_code` | Look up harmonized tariff code candidates for a goods description. | ✅ |

## 🤖 Used by 2 agents

[`supply-chain/route-optimizer`](../../agents/business/supply-chain/route-optimizer/README.md), [`supply-chain/shipment-tracker`](../../agents/business/supply-chain/shipment-tracker/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
