<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [👁️ Vision and images](../README.md) › **Screen Parser**

# 👁️ Screen Parser

![id: vision/screenshot-understander](https://img.shields.io/badge/id-vision%2Fscreenshot--understander-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Converts UI screenshots into a structured tree of buttons, inputs, and coordinates.

Gives desktop and browser agents a structured element map from screen pixels.

| | |
|---|---|
| **Use it when** | GUI/computer-use automation where DOM/accessibility trees are unavailable. |
| **Don't use it when** | APIs or semantic web DOMs where HTML suffices. |
| **Pattern** | `augmented-llm` |
| **Modality** | vision, gui |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `vision` `screenshot-understander` |

## 🚀 Quick start

```bash
afe add vision/screenshot-understander          # copy this agent (and the agents it uses) into ./agents
afe info vision/screenshot-understander         # manifest, tools, safety level
afe test vision/screenshot-understander         # run its 62 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"image": {"text_hint": "OK"}}  # from evals/cases.jsonl
result = AgentRunner().run("vision/screenshot-understander", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Screen Parser"]
    AG --> OUT[/"Output"/]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `image` | [`ImageSource`](../../../../spec/types/ImageSource.schema.json) | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `elements` | array of `object` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`accessibility/accessibility-auditor`](../../accessibility/accessibility-auditor/README.md), [`accessibility/screen-narrator`](../../accessibility/screen-narrator/README.md), [`accessibility/sign-language-interpreter`](../../accessibility/sign-language-interpreter/README.md), [`browser/web-navigator`](../../../action/browser/web-navigator/README.md), [`computer-use/desktop-operator`](../../../action/computer-use/desktop-operator/README.md), [`computer-use/macro-recorder`](../../../action/computer-use/macro-recorder/README.md), [`computer-use/mobile-operator`](../../../action/computer-use/mobile-operator/README.md), [`computer-use/rpa-bridge`](../../../action/computer-use/rpa-bridge/README.md), [`video/lecture-to-notes`](../../video/lecture-to-notes/README.md), [`video/live-stream-monitor`](../../video/live-stream-monitor/README.md), [`video/video-editor`](../../video/video-editor/README.md), [`video/video-search`](../../video/video-search/README.md), [`vision/scene-safety-monitor`](../scene-safety-monitor/README.md)

## 🧰 Tools (MCP servers)

_No tools: this agent works only on its input._

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
- **Run:** `afe test vision/screenshot-understander`

## 🧠 Model requirements

- **Needs:** `vision`, `structured_output`
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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvision/screenshot-understander%5D%20) about this agent.

<!-- afe:end-generated -->
