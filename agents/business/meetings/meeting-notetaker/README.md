<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📅 Meetings and calendar](../README.md) › **Meeting Notetaker**

# 📅 Meeting Notetaker

![id: meetings/meeting-notetaker](https://img.shields.io/badge/id-meetings%2Fmeeting--notetaker-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Transcribes meetings and produces structured summaries with decisions and risks.

Composes speech-to-text and summarization to capture clean meeting records.

| | |
|---|---|
| **Use it when** | Turning recorded meetings or transcripts into crisp notes. |
| **Don't use it when** | Extracting task records directly into trackers (pair with action-item-extractor). |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `meetings` `meeting-notetaker` |

## 🚀 Quick start

```bash
afe add meetings/meeting-notetaker          # copy this agent (and the agents it uses) into ./agents
afe info meetings/meeting-notetaker         # manifest, tools, safety level
afe test meetings/meeting-notetaker         # run its 62 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"audio": {"format": "text-simulated", "transcript_hint": ""}}  # from evals/cases.jsonl
result = AgentRunner().run("meetings/meeting-notetaker", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Meeting Notetaker"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["voice/speech-to-text"]
    AG -. uses .-> D1["text/summarizer"]
    AG -. tool .-> T0[("afe/stt")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `audio` | [`AudioSource`](../../../../spec/types/AudioSource.schema.json) | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `summary` | `string` | ✅ |  |
| `key_points` | array of `string` | ✅ |  |
| `transcript` | [`Transcript`](../../../../spec/types/Transcript.schema.json) | ✅ |  |

## 🔗 Composes with

- **Uses:** [`voice/speech-to-text`](../../../perception/voice/speech-to-text/README.md), [`text/summarizer`](../../../information/text/summarizer/README.md)
- **Used by agents:** _none yet_
- **In teams:** [`meeting-to-done`](../../../../teams/meeting-to-done/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/stt`](../../../../mcp-servers/stt/README.md) | ✅ | Streaming and batch speech transcription with multilingual code-switching support. |

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

- **62 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test meetings/meeting-notetaker`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bmeetings/meeting-notetaker%5D%20) about this agent.

<!-- afe:end-generated -->
