<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🧠 Memory and knowledge](../README.md) › **Knowledge Ingestor**

# 🧠 Knowledge Ingestor

![id: memory/knowledge-ingestor](https://img.shields.io/badge/id-memory%2Fknowledge--ingestor-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Parses, chunks, and prepares documents for hybrid keyword + vector indexing with metadata.

Splits raw documents into deterministic overlapping chunks with provenance IDs for RAG agents.

| | |
|---|---|
| **Use it when** | Preparing manuals, PDFs, or wikis for search/rag-qa. |
| **Don't use it when** | Already-chunked short messages. |
| **Pattern** | `prompt-chaining` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `memory` `knowledge-ingestor` |

## 🚀 Quick start

```bash
afe add memory/knowledge-ingestor          # copy this agent (and the agents it uses) into ./agents
afe info memory/knowledge-ingestor         # manifest, tools, safety level
afe test memory/knowledge-ingestor         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"documents": [{"id": "d1", "title": "Policy", "content": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"}], "chunk_size": 100}  # from evals/cases.jsonl
result = AgentRunner().run("memory/knowledge-ingestor", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Knowledge Ingestor"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/vector-store")]
    AG -. tool .-> T1[("afe/documents")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S2** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `prompt-chaining` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `documents` | array of [`Document`](../../../../spec/types/Document.schema.json) | ✅ |  |
| `chunk_size` | `integer` |  | default `400`; min 50 |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `chunks` | array of `object` | ✅ |  |
| `count` | `integer` | ✅ | min 0 |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`ai-engineering/rag-builder`](../../../builders/ai-engineering/rag-builder/README.md), [`memory/wiki-maintainer`](../wiki-maintainer/README.md)
- **In recipes:** [`chat-with-your-docs`](../../../../recipes/chat-with-your-docs/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/vector-store`](../../../../mcp-servers/vector-store/README.md) | ✅ | Hybrid keyword + semantic indexing and retrieval with metadata ACL filters. |
| [`afe/documents`](../../../../mcp-servers/documents/README.md) | ✅ | Parse PDF, DOCX, PPTX, HTML, and spreadsheets into structured Markdown/tables. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S2** — Reversible writes: Drafts and local changes with preview, undo and logging |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `writes-vector-index` |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test memory/knowledge-ingestor`

## 🧠 Model requirements

- **Needs:** `structured_output`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bmemory/knowledge-ingestor%5D%20) about this agent.

<!-- afe:end-generated -->
