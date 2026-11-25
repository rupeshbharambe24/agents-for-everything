# Legal Researcher `legal/legal-researcher`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Finds statutes and case law with verified citations.

> **Important Safety Notice:** Legal operations assistant; not legal advice—qualified counsel must review contracts, filings, and compliance determinations.

## When to use / not use
- **Use when:** You need single-purpose legal researcher (question + jurisdiction → memo).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `legal/legal-researcher` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add legal/legal-researcher
afe test legal/legal-researcher
```

## Composes with
legal/contract-analyzer, text/summarizer

## Tools required
afe/documents

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test legal/legal-researcher` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
