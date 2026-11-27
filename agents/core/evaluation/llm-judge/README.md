<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📏 Evaluation and quality](../README.md) › **LLM Judge**

# 📏 LLM Judge

![id: evaluation/llm-judge](https://img.shields.io/badge/id-evaluation%2Fllm--judge-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Scores outputs against a rubric with calibrated, explained verdicts.

Evaluates agent outputs during CI regressions, prompt optimization, and quality gates.

| | |
|---|---|
| **Use it when** | Automated grading of open-ended outputs against criteria. |
| **Don't use it when** | Exact deterministic JSON field equality checks. |
| **Pattern** | `evaluator-optimizer` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `evaluation` `llm-judge` |

## 🚀 Quick start

```bash
afe add evaluation/llm-judge          # copy this agent (and the agents it uses) into ./agents
afe info evaluation/llm-judge         # manifest, tools, safety level
afe test evaluation/llm-judge         # run its 62 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"output": "", "rubric": "Non-empty"}  # from evals/cases.jsonl
result = AgentRunner().run("evaluation/llm-judge", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["LLM Judge"]
    AG --> OUT[/"Output"/]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S0** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `evaluator-optimizer` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `output` | `string` | ✅ |  |
| `rubric` | `string` | ✅ |  |
| `required_terms` | array of `string` |  |  |

## 📤 Output

See [`output.schema.json`](schemas/output.schema.json).

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`ai-engineering/automl-trainer`](../../../builders/ai-engineering/automl-trainer/README.md), [`ai-engineering/paper-to-code`](../../../builders/ai-engineering/paper-to-code/README.md), [`evaluation/benchmark-runner`](../benchmark-runner/README.md), [`evaluation/regression-runner`](../regression-runner/README.md), [`guardrails/bias-auditor`](../../guardrails/bias-auditor/README.md)
- **In teams:** [`agent-factory`](../../../../teams/agent-factory/README.md)

## 🧰 Tools (MCP servers)

_No tools: this agent works only on its input._

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S0** — Pure computation: No external access; schema validation only |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **62 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test evaluation/llm-judge`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bevaluation/llm-judge%5D%20) about this agent.

<!-- afe:end-generated -->
