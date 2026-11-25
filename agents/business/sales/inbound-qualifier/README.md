# Inbound Lead Qualifier `sales/inbound-qualifier`

prototype · P2 · composite · safety S3 · autonomy L2

## What it does
Chats with inbound leads, qualifies them and books meetings.

## When to use / not use
- **Use when:** You need single-purpose inbound lead qualifier (conversation → qualified lead + booking).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `sales/inbound-qualifier` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add sales/inbound-qualifier
afe test sales/inbound-qualifier
```

## Composes with
sales/account-researcher, text/summarizer

## Tools required
afe/calendar, afe/crm

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test sales/inbound-qualifier` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
