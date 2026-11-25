# Policy Comparer `insurance/policy-comparer`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Side-by-side comparison of coverage, exclusions and price.

> **Important Safety Notice:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.

## When to use / not use
- **Use when:** You need single-purpose policy comparer (policies → comparison).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `insurance/policy-comparer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add insurance/policy-comparer
afe test insurance/policy-comparer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test insurance/policy-comparer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
