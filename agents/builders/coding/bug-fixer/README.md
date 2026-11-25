<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [💻 Software engineering](../README.md) › **Bug Fixer**

# 💻 Bug Fixer

![id: coding/bug-fixer](https://img.shields.io/badge/id-coding%2Fbug--fixer-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Diagnoses bugs from stack traces, proposes a patch, adds regression tests, and verifies review.

Coordinates root-cause diagnosis, test creation, and diff review into a verified patch.

| | |
|---|---|
| **Use it when** | Fixing reproducible bugs with stack traces or failing assertions. |
| **Don't use it when** | Greenfield architecture rewrites. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `coding` `bug-fixer` |

## 🚀 Quick start

```bash
afe add coding/bug-fixer          # copy this agent (and the agents it uses) into ./agents
afe info coding/bug-fixer         # manifest, tools, safety level
afe test coding/bug-fixer         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"issue": "Null edge case #1", "code": "def f(x):\n    return x"}  # from evals/cases.jsonl
result = AgentRunner().run("coding/bug-fixer", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Bug Fixer"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["coding/test-writer"]
    AG -. uses .-> D1["coding/code-reviewer"]
    AG -. tool .-> T0[("afe/filesystem")]
    AG -. tool .-> T1[("afe/shell-sandbox")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S2** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `issue` | `string` | ✅ |  |
| `code` | `string` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `root_cause` | `string` | ✅ |  |
| `patch` | `string` | ✅ |  |
| `review_passed` | `boolean` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`coding/test-writer`](../test-writer/README.md), [`coding/code-reviewer`](../code-reviewer/README.md)
- **Used by agents:** _none yet_
- **In teams:** [`bug-squash`](../../../../teams/bug-squash/README.md)

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
| **Side effects** | `patches-code` |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test coding/bug-fixer`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bcoding/bug-fixer%5D%20) about this agent.

<!-- afe:end-generated -->
