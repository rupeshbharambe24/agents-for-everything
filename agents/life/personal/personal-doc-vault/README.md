# Personal Document Vault `personal/personal-doc-vault`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Organizes personal documents (IDs, warranties, policies) with encryption and expiry reminders.

## When to use / not use
- **Use when:** You need single-purpose personal document vault (documents → vault + reminders).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `personal/personal-doc-vault` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add personal/personal-doc-vault
afe test personal/personal-doc-vault
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem, afe/vector-store

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test personal/personal-doc-vault` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
