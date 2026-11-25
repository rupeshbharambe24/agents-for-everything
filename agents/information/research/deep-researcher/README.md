<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📚 Research and analysis](../README.md) › **Deep Researcher**

# 📚 Deep Researcher

![id: research/deep-researcher](https://img.shields.io/badge/id-research%2Fdeep--researcher-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Plans research questions, searches iteratively, reads sources, fact-checks, and writes a cited report.

End-to-end composite research orchestrator combining search, reading, fact-checking, and report writing.

| | |
|---|---|
| **Use it when** | Thorough multi-source investigation producing cited reports. |
| **Don't use it when** | Simple single-fact lookups. |
| **Pattern** | `orchestrator-workers` |
| **Modality** | text |
| **Runtime** | interactive · memory: `session` |
| **Languages** | `en` |
| **Tags** | `research` `deep-researcher` |

## 🚀 Quick start

```bash
afe add research/deep-researcher          # copy this agent (and the agents it uses) into ./agents
afe info research/deep-researcher         # manifest, tools, safety level
afe test research/deep-researcher         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"topic": "Agentic AI Architecture Trend 1", "depth": "standard"}  # from evals/cases.jsonl
result = AgentRunner().run("research/deep-researcher", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Deep Researcher"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["search/web-search"]
    AG -. uses .-> D1["research/source-reader"]
    AG -. uses .-> D2["research/fact-checker"]
    AG -. uses .-> D3["research/report-writer"]
    AG -. tool .-> T0[("afe/web-search")]
    AG -. tool .-> T1[("afe/http")]
    AG -. tool .-> T2[("afe/documents")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `orchestrator-workers` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `topic` | `string` | ✅ |  |
| `depth` | enum |  | one of `quick`, `standard`, `deep`; default `"standard"` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `report_markdown` | `string` | ✅ |  |
| `citations` | array of [`Citation`](../../../../spec/types/Citation.schema.json) | ✅ |  |
| `verified_claims` | `integer` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`search/web-search`](../../search/web-search/README.md), [`research/source-reader`](../source-reader/README.md), [`research/fact-checker`](../fact-checker/README.md), [`research/report-writer`](../report-writer/README.md)
- **Used by agents:** _none yet_
- **In recipes:** [`deep-research-app`](../../../../recipes/deep-research-app/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/web-search`](../../../../mcp-servers/web-search/README.md) | ✅ | Search web indexes and return ranked snippets and URLs. |
| [`afe/http`](../../../../mcp-servers/http/README.md) | ✅ | Fetch URLs and REST/GraphQL endpoints with robots.txt and rate-limit awareness. |
| [`afe/documents`](../../../../mcp-servers/documents/README.md) | ✅ | Parse PDF, DOCX, PPTX, HTML, and spreadsheets into structured Markdown/tables. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test research/deep-researcher`

## 🧠 Model requirements

- **Needs:** `structured_output`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## 📁 Files

| File | Purpose |
|---|---|
| [`agent.yaml`](agent.yaml) | Manifest: the single source of truth |
| [`prompts/system.md`](prompts/system.md) | Instructions the model follows |
| [`schemas/`](schemas/input.schema.json) | Input and output contracts |
| [`tools.yaml`](tools.yaml) | MCP servers and permissions |
| [`evals/`](evals/eval.yaml) | Test cases, rubric, targets |
| `impl/` | Python and TypeScript implementations |
| [`examples/basic.md`](examples/basic.md) | Worked example |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

## 🤝 Help improve this agent

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bresearch/deep-researcher%5D%20) about this agent.

<!-- afe:end-generated -->
