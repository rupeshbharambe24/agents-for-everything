<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Issue Tracker MCP Server**

# 🧰 Issue Tracker MCP Server

![id: afe/issue-tracker](https://img.shields.io/badge/id-afe%2Fissue--tracker-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Read, label, deduplicate, and draft issues/PRs across GitHub, Jira, or Linear.

**Backed by:** github / linear / jira MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `list_issues` | Query open issues and metadata. | ✅ |
| `draft_update` | Prepare labels or status comments for approval. |  |

## 🤖 Used by 8 agents

[`coding/issue-triager`](../../agents/builders/coding/issue-triager/README.md), [`operations/decision-logger`](../../agents/business/operations/decision-logger/README.md), [`operations/okr-tracker`](../../agents/business/operations/okr-tracker/README.md), [`operations/product-feedback-prioritizer`](../../agents/business/operations/product-feedback-prioritizer/README.md), [`operations/project-manager`](../../agents/business/operations/project-manager/README.md), [`operations/risk-register-keeper`](../../agents/business/operations/risk-register-keeper/README.md), [`operations/status-reporter`](../../agents/business/operations/status-reporter/README.md), [`productivity/weekly-review`](../../agents/life/productivity/weekly-review/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
