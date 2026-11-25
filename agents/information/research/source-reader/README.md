<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📚 Research and analysis](../README.md) › **Source Reader**

# 📚 Source Reader

![id: research/source-reader](https://img.shields.io/badge/id-research%2Fsource--reader-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Reads one URL or document deeply and extracts key points, facts, and quotes.

Produces structured research notes with exact quotes from a single source.

| | |
|---|---|
| **Use it when** | Extracting structured notes from an article, paper, or page. |
| **Don't use it when** | Multi-source synthesis. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `research` `source-reader` |

## 🚀 Quick start

```bash
afe add research/source-reader          # copy this agent (and the agents it uses) into ./agents
afe info research/source-reader         # manifest, tools, safety level
afe test research/source-reader         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"url": "https://example.org/doc/1", "content": "Finding 1 shows modular agents improve reliability. Tests confirm 99% pass rate."}  # from evals/cases.jsonl
result = AgentRunner().run("research/source-reader", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Source Reader"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/http")]
    AG -. tool .-> T1[("afe/documents")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `url` | `string` |  |  |
| `content` | `string` |  |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `summary` | `string` | ✅ |  |
| `key_points` | array of `string` | ✅ |  |
| `quotes` | array of `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`research/deep-researcher`](../deep-researcher/README.md), [`research/due-diligence`](../due-diligence/README.md), [`research/literature-reviewer`](../literature-reviewer/README.md), [`research/policy-analyst`](../policy-analyst/README.md), [`science/materials-literature-miner`](../../../industries/science/materials-literature-miner/README.md), [`science/proof-assistant`](../../../industries/science/proof-assistant/README.md), [`science/results-to-manuscript`](../../../industries/science/results-to-manuscript/README.md), [`science/simulation-setup`](../../../industries/science/simulation-setup/README.md), [`search/answer-engine`](../../search/answer-engine/README.md)
- **In teams:** [`ecosystem-radar`](../../../../teams/ecosystem-radar/README.md), [`research-team`](../../../../teams/research-team/README.md)
- **In recipes:** [`deep-research-app`](../../../../recipes/deep-research-app/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/http`](../../../../mcp-servers/http/README.md) | ✅ | Fetch URLs and REST/GraphQL endpoints with robots.txt and rate-limit awareness. |
| [`afe/documents`](../../../../mcp-servers/documents/README.md) | ✅ | Parse PDF, DOCX, PPTX, HTML, and spreadsheets into structured Markdown/tables. |

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
- **Run:** `afe test research/source-reader`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bresearch/source-reader%5D%20) about this agent.

<!-- afe:end-generated -->
