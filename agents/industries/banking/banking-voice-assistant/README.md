# Vernacular Banking Assistant `banking/banking-voice-assistant`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Voice-first help for balances, FAQs and services in local languages, authenticated through the bank's own systems.

> **Important Safety Notice:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.

## When to use / not use
- **Use when:** You need single-purpose vernacular banking assistant (voice ↔ voice + actions).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `banking/banking-voice-assistant` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/banking-voice-assistant
afe test banking/banking-voice-assistant
```

## Composes with
voice/realtime-voice-assistant, documents/document-parser

## Tools required
afe/compliance-reg

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test banking/banking-voice-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
