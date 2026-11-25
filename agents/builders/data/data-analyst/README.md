<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📊 Data and analytics](../README.md) › **Data Analyst**

# 📊 Data Analyst

![id: data/data-analyst](https://img.shields.io/badge/id-data%2Fdata--analyst-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Cleans datasets, computes descriptive statistics, and drafts plain-language insights.

Composes data-cleaner with numeric summary analytics to answer business questions.

| | |
|---|---|
| **Use it when** | Exploratory statistics and KPI insight generation. |
| **Don't use it when** | Direct database querying without Python data. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `data` `data-analyst` |

## 🚀 Quick start

```bash
afe add data/data-analyst          # copy this agent (and the agents it uses) into ./agents
afe info data/data-analyst         # manifest, tools, safety level
afe test data/data-analyst         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"rows": [{"rev": 100}, {"rev": 200}], "metric": "rev"}  # from evals/cases.jsonl
result = AgentRunner().run("data/data-analyst", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Data Analyst"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["data/data-cleaner"]
    AG -. tool .-> T0[("afe/python-sandbox")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `rows` | array of `object` | ✅ |  |
| `metric` | `string` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `count` | `integer` | ✅ |  |
| `mean` | `number` | ✅ |  |
| `min` | `number` | ✅ |  |
| `max` | `number` | ✅ |  |
| `insight` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`data/data-cleaner`](../data-cleaner/README.md)
- **Used by agents:** [`data/dashboard-builder`](../dashboard-builder/README.md), [`data/etl-builder`](../etl-builder/README.md), [`energy/energy-auditor`](../../../industries/energy/energy-auditor/README.md)
- **In teams:** [`data-insights`](../../../../teams/data-insights/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/python-sandbox`](../../../../mcp-servers/python-sandbox/README.md) | ✅ | Sandboxed Python code execution for data analysis, cleaning, and verification. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test data/data-analyst`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bdata/data-analyst%5D%20) about this agent.

<!-- afe:end-generated -->
