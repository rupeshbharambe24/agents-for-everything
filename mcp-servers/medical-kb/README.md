<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Authoritative Medical & Crisis Reference MCP Server**

# 🧰 Authoritative Medical & Crisis Reference MCP Server

![id: afe/medical-kb](https://img.shields.io/badge/id-afe%2Fmedical--kb-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Retrieve peer-reviewed clinical references, drug interaction alerts, and verified crisis helpline directories.

**Backed by:** medlineplus / rxnav / open-crisis-directory adapter

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `lookup_drug_interaction` | Look up documented medication interaction notes. | ✅ |
| `lookup_crisis_resources` | Return regional verified emergency and crisis helpline numbers. | ✅ |

## 🤖 Used by 9 agents

[`healthcare/clinical-coder`](../../agents/industries/healthcare/clinical-coder/README.md), [`healthcare/clinical-trial-matcher`](../../agents/industries/healthcare/clinical-trial-matcher/README.md), [`healthcare/discharge-simplifier`](../../agents/industries/healthcare/discharge-simplifier/README.md), [`healthcare/patient-intake`](../../agents/industries/healthcare/patient-intake/README.md), [`wellness/fitness-coach`](../../agents/life/wellness/fitness-coach/README.md), [`wellness/medication-reminder`](../../agents/life/wellness/medication-reminder/README.md), [`wellness/nutrition-coach`](../../agents/life/wellness/nutrition-coach/README.md), [`wellness/symptom-navigator`](../../agents/life/wellness/symptom-navigator/README.md), [`wellness/wellbeing-companion`](../../agents/life/wellness/wellbeing-companion/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
