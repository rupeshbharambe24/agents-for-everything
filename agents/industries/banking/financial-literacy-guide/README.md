# Financial Literacy Guide `banking/financial-literacy-guide`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Explains banking, digital payments, insurance and government schemes simply, in local languages.

> **Important Safety Notice:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.

## When to use / not use
- **Use when:** You need single-purpose financial literacy guide (question → explanation).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `banking/financial-literacy-guide` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/financial-literacy-guide
afe test banking/financial-literacy-guide
```

## Composes with
search/rag-qa, voice/text-to-speech

## Tools required
afe/tts, afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test banking/financial-literacy-guide` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
