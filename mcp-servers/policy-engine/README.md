<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Action Policy & Audit Engine MCP Server**

# 🧰 Action Policy & Audit Engine MCP Server

![id: afe/policy-engine](https://img.shields.io/badge/id-afe%2Fpolicy--engine-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Evaluate proposed tool calls against OPA-style allow/deny rules and append audit logs.

**Backed by:** opa / cedar policy MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `evaluate_policy` | Return allow, deny, or require_approval for an action. | ✅ |

## 🤖 Used by 3 agents

[`banking/fraud-signal-explainer`](../../agents/industries/banking/fraud-signal-explainer/README.md), [`banking/sanctions-screener`](../../agents/industries/banking/sanctions-screener/README.md), [`orchestration/progress-reporter`](../../agents/core/orchestration/progress-reporter/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
