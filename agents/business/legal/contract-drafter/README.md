# Contract Drafter `legal/contract-drafter`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Drafts contracts from approved templates and term sheets.

> **Important Safety Notice:** Legal operations assistant; not legal advice—qualified counsel must review contracts, filings, and compliance determinations.

## When to use / not use
- **Use when:** You need single-purpose contract drafter (terms + template → draft).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `legal/contract-drafter` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add legal/contract-drafter
afe test legal/contract-drafter
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test legal/contract-drafter` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
