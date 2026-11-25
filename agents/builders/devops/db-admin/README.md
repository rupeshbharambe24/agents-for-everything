# Database Assistant `devops/db-admin`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Query tuning, index advice, backup and health checks.

## When to use / not use
- **Use when:** You need single-purpose database assistant (DB + issue → recommendations).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `devops/db-admin` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add devops/db-admin
afe test devops/db-admin
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/sql

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `False`

## Evaluation
Run `afe test devops/db-admin` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
