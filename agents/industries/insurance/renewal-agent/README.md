# Renewal Agent `insurance/renewal-agent`

prototype · P2 · atomic · safety S3 · autonomy L2

## What it does
Renewal reminders and coverage-change summaries.

> **Important Safety Notice:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.

## When to use / not use
- **Use when:** You need single-purpose renewal agent (policies → reminders).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `insurance/renewal-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add insurance/renewal-agent
afe test insurance/renewal-agent
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/chat

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test insurance/renewal-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
