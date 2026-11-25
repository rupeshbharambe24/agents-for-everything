<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Defensive Threat Intel & Scanner MCP Server**

# 🧰 Defensive Threat Intel & Scanner MCP Server

![id: afe/threat-intel](https://img.shields.io/badge/id-afe%2Fthreat--intel-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Query CVE advisories, dependency vulnerability scanners, and secret regex scanners.

**Backed by:** osv / trivy / gitleaks MCP wrapper

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `check_advisories` | Check package or indicator against defensive vulnerability feeds. | ✅ |

## 🤖 Used by 9 agents

[`guardrails/red-teamer`](../../agents/core/guardrails/red-teamer/README.md), [`security/access-reviewer`](../../agents/builders/security/access-reviewer/README.md), [`security/pentest-assistant`](../../agents/builders/security/pentest-assistant/README.md), [`security/phishing-analyzer`](../../agents/builders/security/phishing-analyzer/README.md), [`security/secret-scanner`](../../agents/builders/security/secret-scanner/README.md), [`security/security-compliance-auditor`](../../agents/builders/security/security-compliance-auditor/README.md), [`security/security-incident-reporter`](../../agents/builders/security/security-incident-reporter/README.md), [`security/threat-intel-summarizer`](../../agents/builders/security/threat-intel-summarizer/README.md), [`security/vuln-triager`](../../agents/builders/security/vuln-triager/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
