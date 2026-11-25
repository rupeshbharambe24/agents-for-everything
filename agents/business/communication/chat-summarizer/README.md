# Chat Summarizer `communication/chat-summarizer`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Extracts key decisions, open questions, and highlights from noisy chat logs.

## When to use / not use
- **Use when:** Catching up on long team chat channels.
- **Do not use when:** Legal contract interpretation.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `communication/chat-summarizer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/chat-summarizer
afe test communication/chat-summarizer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/chat

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test communication/chat-summarizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
