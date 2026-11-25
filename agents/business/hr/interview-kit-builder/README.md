# Interview Kit Builder `hr/interview-kit-builder`

prototype · P2 · atomic · safety S0 · autonomy L1

## What it does
Structured interview questions and scorecards for a role.

> **Important Safety Notice:** HR decision-support assistant only; final hiring, screening, compensation, and promotion decisions must be made by humans.

## When to use / not use
- **Use when:** You need single-purpose interview kit builder (role → kit).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S0`) and declared MCP permissions.
3. Runs `hr/interview-kit-builder` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add hr/interview-kit-builder
afe test hr/interview-kit-builder
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
None (pure computation / LLM reasoning)

## Safety
- Safety tier: `S0`
- Side effects: `[]`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test hr/interview-kit-builder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
