<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Cloud Infrastructure & FinOps MCP Server**

# 🧰 Cloud Infrastructure & FinOps MCP Server

![id: afe/cloud](https://img.shields.io/badge/id-afe%2Fcloud-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Read-only cloud resource inventory, utilization, and billing metrics.

**Backed by:** aws / gcp / azure / kubernetes MCP adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `list_resources` | Inspect compute, storage, and billing utilization. | ✅ |

## 🤖 Used by 2 agents

[`devops/cloud-cost-optimizer`](../../agents/builders/devops/cloud-cost-optimizer/README.md), [`devops/config-drift-detector`](../../agents/builders/devops/config-drift-detector/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
