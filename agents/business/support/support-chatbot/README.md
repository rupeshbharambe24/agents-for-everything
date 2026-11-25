# Support Assistant `support/support-chatbot`

beta · P0 · composite · safety S1 · autonomy L1

## What it does
Composes RAG Q&A to resolve tier-1 support inquiries accurately without hallucinating policies.

## When to use / not use
- **Use when:** Customer self-service grounded in official help docs.
- **Do not use when:** Executing refunds without human review.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `support/support-chatbot` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add support/support-chatbot
afe test support/support-chatbot
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test support/support-chatbot` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
