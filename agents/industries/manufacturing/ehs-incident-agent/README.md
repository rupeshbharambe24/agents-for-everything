# Safety Incident Agent `manufacturing/ehs-incident-agent`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Captures safety incidents and near misses and drafts investigation reports.

## When to use / not use
- **Use when:** You need single-purpose safety incident agent (report → incident file).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `manufacturing/ehs-incident-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add manufacturing/ehs-incident-agent
afe test manufacturing/ehs-incident-agent
```

## Composes with
voice/voice-form-filler, vision/ocr

## Tools required
afe/observability

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `False`

## Evaluation
Run `afe test manufacturing/ehs-incident-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
