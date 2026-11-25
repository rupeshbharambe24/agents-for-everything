# Offer Letter Generator `hr/offer-letter-generator`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Generates offer letters from approved templates.

> **Important Safety Notice:** HR decision-support assistant only; final hiring, screening, compensation, and promotion decisions must be made by humans.

## When to use / not use
- **Use when:** You need single-purpose offer letter generator (offer data → letter).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `hr/offer-letter-generator` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add hr/offer-letter-generator
afe test hr/offer-letter-generator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test hr/offer-letter-generator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
