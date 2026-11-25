<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🔐 Cybersecurity](../README.md) › **SOC Analyst**

# 🔐 SOC Analyst

![id: security/siem-analyst](https://img.shields.io/badge/id-security%2Fsiem--analyst-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Investigates alerts, queries the SIEM, builds a timeline and recommends response.

Investigates alerts, queries the SIEM, builds a timeline and recommends response.

| | |
|---|---|
| **Use it when** | You need single-purpose soc analyst (alert → investigation). |
| **Don't use it when** | Actions exceed declared MCP tools or bypass required human sign-off. |
| **Pattern** | `orchestrator-workers` |
| **Modality** | text |
| **Runtime** | scheduled · memory: `session` |
| **Languages** | `en` |
| **Tags** | `builders` `security` `siem` |

## 🚀 Quick start

```bash
afe add security/siem-analyst          # copy this agent (and the agents it uses) into ./agents
afe info security/siem-analyst         # manifest, tools, safety level
afe test security/siem-analyst         # run its 10 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"input": ""}  # from evals/cases.jsonl
result = AgentRunner().run("security/siem-analyst", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["SOC Analyst"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["security/vuln-triager"]
    AG -. uses .-> D1["guardrails/prompt-injection-detector"]
    AG -. tool .-> T0[("afe/observability")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `orchestrator-workers` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `input` | `string` | ✅ | Primary task payload (alert → investigation) |
| `locale` | `string` |  | default `"en"` |
| `context` | `object` |  |  |
| `execute` | `boolean` |  | default `false` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `result` | `string` | ✅ |  |
| `items` | array of `object` |  |  |
| `confidence` | `number` |  |  |
| `status` | `string` | ✅ |  |
| `locale` | `string` |  |  |

## 🔗 Composes with

- **Uses:** [`security/vuln-triager`](../vuln-triager/README.md), [`guardrails/prompt-injection-detector`](../../../core/guardrails/prompt-injection-detector/README.md)
- **Used by agents:** _none yet_

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/observability`](../../../../mcp-servers/observability/README.md) | ✅ | Query logs, metrics, traces, and active alerts across observability backends. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L1** — human executes |
| **Side effects** | `read-only-external-query` |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **10 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test security/siem-analyst`

## 🧠 Model requirements

- **Needs:** `structured_output`, `tool_use`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bsecurity/siem-analyst%5D%20) about this agent.

<!-- afe:end-generated -->
