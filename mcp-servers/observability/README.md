<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Observability & SIEM MCP Server**

# 🧰 Observability & SIEM MCP Server

![id: afe/observability](https://img.shields.io/badge/id-afe%2Fobservability-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Query logs, metrics, traces, and active alerts across observability backends.

**Backed by:** prometheus / grafana / otel MCP adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `query_alerts` | Fetch active alerts and recent metrics anomalies. | ✅ |

## 🤖 Used by 16 agents

[`ai-engineering/model-monitor`](../../agents/builders/ai-engineering/model-monitor/README.md), [`coding/ci-fixer`](../../agents/builders/coding/ci-fixer/README.md), [`devops/alert-triager`](../../agents/builders/devops/alert-triager/README.md), [`devops/incident-responder`](../../agents/builders/devops/incident-responder/README.md), [`devops/k8s-operator`](../../agents/builders/devops/k8s-operator/README.md), [`devops/postmortem-writer`](../../agents/builders/devops/postmortem-writer/README.md), [`energy/energy-auditor`](../../agents/industries/energy/energy-auditor/README.md), [`guardrails/audit-logger`](../../agents/core/guardrails/audit-logger/README.md), [`integration/webhook-handler`](../../agents/action/integration/webhook-handler/README.md), [`manufacturing/ehs-incident-agent`](../../agents/industries/manufacturing/ehs-incident-agent/README.md), [`manufacturing/predictive-maintenance`](../../agents/industries/manufacturing/predictive-maintenance/README.md), [`manufacturing/quality-inspector`](../../agents/industries/manufacturing/quality-inspector/README.md), [`orchestration/scheduler`](../../agents/core/orchestration/scheduler/README.md), [`security/siem-analyst`](../../agents/builders/security/siem-analyst/README.md), [`voice/speaker-verifier`](../../agents/perception/voice/speaker-verifier/README.md), [`wellness/sleep-coach`](../../agents/life/wellness/sleep-coach/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
