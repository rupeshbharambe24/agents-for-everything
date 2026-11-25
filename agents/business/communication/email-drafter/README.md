# Email Drafter `communication/email-drafter`

beta · P0 · atomic · safety S2 · autonomy L2

## What it does
Generates clean email drafts matching requested intent while gating any send action.

## When to use / not use
- **Use when:** Drafting fast professional replies for human review.
- **Do not use when:** Sending unreviewed external emails.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `communication/email-drafter` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/email-drafter
afe test communication/email-drafter
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/email

## Safety
- Safety tier: `S2`
- Side effects: ['saves-email-draft']
- Approval gates: ['send']

## Evaluation
Run `afe test communication/email-drafter` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
