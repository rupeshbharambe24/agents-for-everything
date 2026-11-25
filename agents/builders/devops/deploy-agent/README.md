# Release Agent `devops/deploy-agent`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Runs releases with canary checks and automatic rollback.

## When to use / not use
- **Use when:** You need single-purpose release agent (release → deploy report).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `devops/deploy-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add devops/deploy-agent
afe test devops/deploy-agent
```

## Composes with
devops/log-analyzer

## Tools required
afe/git

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `False`

## Evaluation
Run `afe test devops/deploy-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
