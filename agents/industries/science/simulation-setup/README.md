# Simulation Setup Agent `science/simulation-setup`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Configures simulation runs (CFD, FEA, molecular) from specifications.

## When to use / not use
- **Use when:** You need single-purpose simulation setup agent (spec → config).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `science/simulation-setup` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add science/simulation-setup
afe test science/simulation-setup
```

## Composes with
research/source-reader, documents/document-parser

## Tools required
afe/python-sandbox

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `False`

## Evaluation
Run `afe test science/simulation-setup` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
