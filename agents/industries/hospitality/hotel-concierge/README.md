# Guest Concierge `hospitality/hotel-concierge`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Answers guest requests and gives local recommendations.

## When to use / not use
- **Use when:** You need single-purpose guest concierge (request → answer/action).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `hospitality/hotel-concierge` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add hospitality/hotel-concierge
afe test hospitality/hotel-concierge
```

## Composes with
search/rag-qa, voice/phone-call-agent

## Tools required
afe/maps, afe/vector-store

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test hospitality/hotel-concierge` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
