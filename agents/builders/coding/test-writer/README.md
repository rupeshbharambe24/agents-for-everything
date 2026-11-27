<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [💻 Software engineering](../README.md) › **Test Writer**

# 💻 Test Writer

![id: coding/test-writer](https://img.shields.io/badge/id-coding%2Ftest--writer-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Generates targeted unit and edge-case tests for functions and APIs.

Writes clean unit tests verifying happy paths, boundary cases, and error paths.

| | |
|---|---|
| **Use it when** | Adding regression and unit tests for existing or newly generated code. |
| **Don't use it when** | Running production database migrations. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `coding` `test-writer` |

## 🚀 Quick start

```bash
afe add coding/test-writer          # copy this agent (and the agents it uses) into ./agents
afe info coding/test-writer         # manifest, tools, safety level
afe test coding/test-writer         # run its 61 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"code": "def noop():\n    pass"}  # from evals/cases.jsonl
result = AgentRunner().run("coding/test-writer", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Test Writer"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/filesystem")]
    AG -. tool .-> T1[("afe/shell-sandbox")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S2** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `code` | `string` | ✅ |  |
| `language` | `string` |  | default `"python"` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `test_code` | `string` | ✅ |  |
| `test_count` | `integer` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`coding/bug-fixer`](../bug-fixer/README.md), [`coding/code-generator`](../code-generator/README.md), [`coding/dependency-updater`](../dependency-updater/README.md), [`coding/frontend-builder`](../frontend-builder/README.md)
- **In teams:** [`bug-squash`](../../../../teams/bug-squash/README.md), [`software-squad`](../../../../teams/software-squad/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/filesystem`](../../../../mcp-servers/filesystem/README.md) | ✅ | Workspace-scoped file discovery, read, diff preview, and safe move/organize operations. |
| [`afe/shell-sandbox`](../../../../mcp-servers/shell-sandbox/README.md) | ✅ | Allowlisted terminal command execution with human confirmation for destructive actions. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S2** — Reversible writes: Drafts and local changes with preview, undo and logging |
| **Autonomy** | **L1** — human executes |
| **Side effects** | `writes-test-files` |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **61 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test coding/test-writer`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bcoding/test-writer%5D%20) about this agent.

<!-- afe:end-generated -->
