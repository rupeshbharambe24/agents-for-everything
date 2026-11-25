# Onboarding Buddy `hr/onboarding-buddy`

prototype · P1 · composite · safety S1 · autonomy L1

## What it does
Guides new hires through 30-60-90 checklists, tools setup, and internal FAQs.

## When to use / not use
- **Use when:** Performing onboarding buddy tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `hr/onboarding-buddy` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add hr/onboarding-buddy
afe test hr/onboarding-buddy
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/hris, afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test hr/onboarding-buddy` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
