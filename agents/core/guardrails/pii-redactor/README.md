# PII Redactor `guardrails/pii-redactor`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Protects privacy before prompts leave trust boundaries or enter logs/traces.

## When to use / not use
- **Use when:** Pre-processing user transcripts, logs, invoices, or support tickets.
- **Do not use when:** Already-anonymized synthetic identifiers.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S0) and declared tool limits.
3. Executes core `guardrails/pii-redactor` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add guardrails/pii-redactor
afe test guardrails/pii-redactor
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
None (pure computation or orchestrator)

## Safety
- Level: `S0`
- Side effects: ['none']
- Approval required for: ['none']

## Evaluation
Run `afe test guardrails/pii-redactor` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
