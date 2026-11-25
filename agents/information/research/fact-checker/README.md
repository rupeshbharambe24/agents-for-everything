<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📚 Research and analysis](../README.md) › **Fact Checker**

# 📚 Fact Checker

![id: research/fact-checker](https://img.shields.io/badge/id-research%2Ffact--checker-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Verifies discrete claims against web or retrieved sources and outputs verdicts with evidence.

Checks factual accuracy of claims and attaches supporting citations.

| | |
|---|---|
| **Use it when** | Validating statements before publishing reports. |
| **Don't use it when** | Opinion/value judgments. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `research` `fact-checker` |

## 🚀 Quick start

```bash
afe add research/fact-checker          # copy this agent (and the agents it uses) into ./agents
afe info research/fact-checker         # manifest, tools, safety level
afe test research/fact-checker         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"claims": ["Claim #1: Open protocols enable multi-agent reuse."]}  # from evals/cases.jsonl
result = AgentRunner().run("research/fact-checker", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Fact Checker"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["search/web-search"]
    AG -. tool .-> T0[("afe/web-search")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `claims` | array of `string` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `verdicts` | array of `object` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`search/web-search`](../../search/web-search/README.md)
- **Used by agents:** [`community/community-moderator`](../../../life/community/community-moderator/README.md), [`research/deep-researcher`](../deep-researcher/README.md)
- **In teams:** [`research-team`](../../../../teams/research-team/README.md)
- **In recipes:** [`deep-research-app`](../../../../recipes/deep-research-app/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/web-search`](../../../../mcp-servers/web-search/README.md) | ✅ | Search web indexes and return ranked snippets and URLs. |

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
- **Run:** `afe test research/fact-checker`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bresearch/fact-checker%5D%20) about this agent.

<!-- afe:end-generated -->
