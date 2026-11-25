# Ticket Triager `support/ticket-triager`

prototype · P0 · atomic · safety S2 · autonomy L1

## What it does
Routes tickets to billing, technical, shipping, or escalation queues with priority levels.

## When to use / not use
- **Use when:** High-volume incoming customer support queues.
- **Do not use when:** Writing full customer responses.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `support/ticket-triager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add support/ticket-triager
afe test support/ticket-triager
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/chat

## Safety
- Safety tier: `S2`
- Side effects: ['labels-ticket']
- Approval gates: ['none']

## Evaluation
Run `afe test support/ticket-triager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
