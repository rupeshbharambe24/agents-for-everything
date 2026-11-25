<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📅 Meetings and calendar](../README.md) › **Meeting Scheduler**

# 📅 Meeting Scheduler

![id: meetings/meeting-scheduler](https://img.shields.io/badge/id-meetings%2Fmeeting--scheduler-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S3](https://img.shields.io/badge/safety-S3-ea580c?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Finds conflict-free meeting slots across calendars and prepares invites for approval.

Coordinates free/busy windows across participants and drafts calendar invites safely.

| | |
|---|---|
| **Use it when** | Proposing and scheduling multi-party meetings. |
| **Don't use it when** | Resolving personal to-do lists. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `meetings` `meeting-scheduler` |

## 🚀 Quick start

```bash
afe add meetings/meeting-scheduler          # copy this agent (and the agents it uses) into ./agents
afe info meetings/meeting-scheduler         # manifest, tools, safety level
afe test meetings/meeting-scheduler         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"title": "Sync #1", "attendees": ["a@example.org"], "candidate_slots": ["2026-11-26T10:00Z"]}  # from evals/cases.jsonl
result = AgentRunner().run("meetings/meeting-scheduler", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Meeting Scheduler"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["communication/email-drafter"]
    AG -. tool .-> T0[("afe/calendar")]
    AG -. tool .-> T1[("afe/email")]
    AG -. needs approval .-> H0{{"human approval: send_invite"}}
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S3** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `title` | `string` | ✅ |  |
| `attendees` | array of `string` | ✅ |  |
| `candidate_slots` | array of `string` | ✅ |  |
| `confirm` | `boolean` |  | default `false` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `selected_slot` | `string` | ✅ |  |
| `status` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`communication/email-drafter`](../../communication/email-drafter/README.md)
- **Used by agents:** _none yet_
- **In recipes:** [`ai-receptionist`](../../../../recipes/ai-receptionist/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/calendar`](../../../../mcp-servers/calendar/README.md) | ✅ | Query free/busy slots across time zones and propose meeting invites with confirmation. |
| [`afe/email`](../../../../mcp-servers/email/README.md) | ✅ | Read inbox threads, apply labels, and create drafts without sending autonomously. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S3** — External side effects: Human approval per action by default |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `creates-calendar-invite` |
| **Needs approval for** | `send_invite` |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |
| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test meetings/meeting-scheduler`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bmeetings/meeting-scheduler%5D%20) about this agent.

<!-- afe:end-generated -->
