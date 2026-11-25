# Access Reviewer `security/access-reviewer`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Reviews permissions for least privilege and flags unusual access.

## When to use / not use
- **Use when:** You need single-purpose access reviewer (access lists → findings).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `security/access-reviewer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add security/access-reviewer
afe test security/access-reviewer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/threat-intel

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test security/access-reviewer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
