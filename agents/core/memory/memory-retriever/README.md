<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🧠 Memory and knowledge](../README.md) › **Memory Retriever**

# 🧠 Memory Retriever

![id: memory/memory-retriever](https://img.shields.io/badge/id-memory%2Fmemory--retriever-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Recalls relevant memories for the current task, ranked and deduplicated.

Matches query terms against stored memory records and returns top-k ranked matches.

| | |
|---|---|
| **Use it when** | Hydrating agent context from long-term user/project memory. |
| **Don't use it when** | Stateless S0 transformations. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `long-term` |
| **Languages** | `en` |
| **Tags** | `memory` `memory-retriever` |

## 🚀 Quick start

```bash
afe add memory/memory-retriever          # copy this agent (and the agents it uses) into ./agents
afe info memory/memory-retriever         # manifest, tools, safety level
afe test memory/memory-retriever         # run its 65 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"query": "Preferred editor", "memories": ["", "   ", "\n\t"]}  # from evals/cases.jsonl
result = AgentRunner().run("memory/memory-retriever", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Memory Retriever"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/vector-store")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `query` | `string` | ✅ |  |
| `memories` | array of `string` | ✅ |  |
| `top_k` | `integer` |  | default `5`; min 1 |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `matches` | array of `object` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`gaming/game-master`](../../../industries/gaming/game-master/README.md), [`gaming/game-tester`](../../../industries/gaming/game-tester/README.md), [`gaming/npc-agent`](../../../industries/gaming/npc-agent/README.md)
- **In teams:** [`chief-of-staff`](../../../../teams/chief-of-staff/README.md)
- **In recipes:** [`personal-chief-of-staff`](../../../../recipes/personal-chief-of-staff/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/vector-store`](../../../../mcp-servers/vector-store/README.md) | ✅ | Hybrid keyword + semantic indexing and retrieval with metadata ACL filters. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **65 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test memory/memory-retriever`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bmemory/memory-retriever%5D%20) about this agent.

<!-- afe:end-generated -->
