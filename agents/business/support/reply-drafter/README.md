<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [💬 Customer support and success](../README.md) › **Reply Drafter**

# 💬 Reply Drafter

![id: support/reply-drafter](https://img.shields.io/badge/id-support%2Freply--drafter-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Drafts KB-grounded support replies for human agents to review and send.

Uses RAG Q&A over help docs to assemble polite, accurate draft replies.

| | |
|---|---|
| **Use it when** | Assisting support specialists with fast grounded draft replies. |
| **Don't use it when** | Autonomous sending without review. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `support` `reply-drafter` |

## 🚀 Quick start

```bash
afe add support/reply-drafter          # copy this agent (and the agents it uses) into ./agents
afe info support/reply-drafter         # manifest, tools, safety level
afe test support/reply-drafter         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"ticket_text": "What is your refund window?", "kb_docs": [{"title": "Policy", "content": "Policy #1: full refund within 30 days."}]}  # from evals/cases.jsonl
result = AgentRunner().run("support/reply-drafter", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Reply Drafter"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["search/rag-qa"]
    AG -. tool .-> T0[("afe/vector-store")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S2** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `ticket_text` | `string` | ✅ |  |
| `kb_docs` | array of `object` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `draft_reply` | `string` | ✅ |  |
| `grounded` | `boolean` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`search/rag-qa`](../../../information/search/rag-qa/README.md)
- **Used by agents:** _none yet_
- **In teams:** [`support-desk`](../../../../teams/support-desk/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/vector-store`](../../../../mcp-servers/vector-store/README.md) | ✅ | Hybrid keyword + semantic indexing and retrieval with metadata ACL filters. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S2** — Reversible writes: Drafts and local changes with preview, undo and logging |
| **Autonomy** | **L1** — human executes |
| **Side effects** | `saves-reply-draft` |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test support/reply-drafter`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bsupport/reply-drafter%5D%20) about this agent.

<!-- afe:end-generated -->
