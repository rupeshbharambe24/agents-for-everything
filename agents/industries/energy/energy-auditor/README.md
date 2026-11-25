# Building Energy Auditor `energy/energy-auditor`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Finds efficiency improvements from bills and building data.

## When to use / not use
- **Use when:** You need single-purpose building energy auditor (building data → measures).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `energy/energy-auditor` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add energy/energy-auditor
afe test energy/energy-auditor
```

## Composes with
documents/document-parser, data/data-analyst

## Tools required
afe/observability

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test energy/energy-auditor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
