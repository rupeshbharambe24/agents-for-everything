<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🧭 Orchestration and meta-agents](../README.md) › **Supervisor / Orchestrator**

# 🧭 Supervisor / Orchestrator

![id: orchestration/supervisor](https://img.shields.io/badge/id-orchestration%2Fsupervisor-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L3](https://img.shields.io/badge/autonomy-L3-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Executes a plan by delegating steps to worker agents, tracks state, and re-plans when a step fails.

Coordinates multi-step agent execution across atomic workers declared in uses_agents.

| | |
|---|---|
| **Use it when** | End-to-end orchestration of multi-step plans across worker agents. |
| **Don't use it when** | Simple single-agent calls. |
| **Pattern** | `orchestrator-workers` |
| **Modality** | text |
| **Runtime** | interactive · memory: `session` |
| **Languages** | `en` |
| **Tags** | `orchestration` `supervisor` |

## 🚀 Quick start

```bash
afe add orchestration/supervisor          # copy this agent (and the agents it uses) into ./agents
afe info orchestration/supervisor         # manifest, tools, safety level
afe test orchestration/supervisor         # run its 61 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"goal": ""}  # from evals/cases.jsonl
result = AgentRunner().run("orchestration/supervisor", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Supervisor / Orchestrator"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["orchestration/task-planner"]
    AG -. uses .-> D1["orchestration/router"]
    AG -. uses .-> D2["orchestration/verifier"]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `orchestrator-workers` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `goal` | `string` | ✅ |  |
| `inputs` | `object` |  |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `results` | array of `object` | ✅ |  |
| `run_log` | array of `string` | ✅ |  |
| `status` | enum | ✅ | one of `completed`, `partial`, `failed` |

## 🔗 Composes with

- **Uses:** [`orchestration/task-planner`](../task-planner/README.md), [`orchestration/router`](../router/README.md), [`orchestration/verifier`](../verifier/README.md)
- **Used by agents:** _none yet_
- **In teams:** [`chief-of-staff`](../../../../teams/chief-of-staff/README.md)

## 🧰 Tools (MCP servers)

_No tools: this agent works only on its input._

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L3** — acts within policy, escalates exceptions |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **61 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test orchestration/supervisor`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Borchestration/supervisor%5D%20) about this agent.

<!-- afe:end-generated -->
