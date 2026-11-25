# Farm Record Keeper `agriculture/farm-record-keeper`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Voice logging of inputs, costs and yields.

## When to use / not use
- **Use when:** You need single-purpose farm record keeper (voice notes → records).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `agriculture/farm-record-keeper` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add agriculture/farm-record-keeper
afe test agriculture/farm-record-keeper
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test agriculture/farm-record-keeper` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
