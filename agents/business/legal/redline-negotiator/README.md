# Redline Negotiator `legal/redline-negotiator`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Proposes counter-redlines with reasons based on the playbook.

> **Important Safety Notice:** Legal operations assistant; not legal advice—qualified counsel must review contracts, filings, and compliance determinations.

## When to use / not use
- **Use when:** You need single-purpose redline negotiator (redlined contract → response).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `legal/redline-negotiator` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add legal/redline-negotiator
afe test legal/redline-negotiator
```

## Composes with
legal/contract-analyzer, text/summarizer

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test legal/redline-negotiator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
