# Employee Survey Analyst `hr/employee-survey-analyst`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Themes and drivers from engagement surveys.

> **Important Safety Notice:** HR decision-support assistant only; final hiring, screening, compensation, and promotion decisions must be made by humans.

## When to use / not use
- **Use when:** You need single-purpose employee survey analyst (responses → insights).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `hr/employee-survey-analyst` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add hr/employee-survey-analyst
afe test hr/employee-survey-analyst
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/hris

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test hr/employee-survey-analyst` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
