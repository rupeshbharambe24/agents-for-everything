# Reply Drafter `support/reply-drafter`

beta · P0 · composite · safety S2 · autonomy L1

## What it does
Uses RAG Q&A over help docs to assemble polite, accurate draft replies.

## When to use / not use
- **Use when:** Assisting support specialists with fast grounded draft replies.
- **Do not use when:** Autonomous sending without review.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `support/reply-drafter` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add support/reply-drafter
afe test support/reply-drafter
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/vector-store

## Safety
- Safety tier: `S2`
- Side effects: ['saves-reply-draft']
- Approval gates: ['none']

## Evaluation
Run `afe test support/reply-drafter` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
