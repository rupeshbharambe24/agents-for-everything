<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Read-Only SQL MCP Server**

# 🧰 Read-Only SQL MCP Server

![id: afe/sql](https://img.shields.io/badge/id-afe%2Fsql-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Schema inspection and read-only SELECT execution across SQLite/Postgres/DuckDB.

**Backed by:** modelcontextprotocol/servers (postgres / sqlite)

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `inspect_schema` | List tables, columns, and types. | ✅ |
| `run_select` | Execute read-only SELECT query with row limit. | ✅ |

## 🤖 Used by 8 agents

[`agriculture/market-price-advisor`](../../agents/industries/agriculture/market-price-advisor/README.md), [`banking/cashflow-lending-analyst`](../../agents/industries/banking/cashflow-lending-analyst/README.md), [`data/dashboard-builder`](../../agents/builders/data/dashboard-builder/README.md), [`data/data-catalog-documenter`](../../agents/builders/data/data-catalog-documenter/README.md), [`data/data-quality-monitor`](../../agents/builders/data/data-quality-monitor/README.md), [`data/metric-explainer`](../../agents/builders/data/metric-explainer/README.md), [`data/text-to-sql`](../../agents/builders/data/text-to-sql/README.md), [`devops/db-admin`](../../agents/builders/devops/db-admin/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
