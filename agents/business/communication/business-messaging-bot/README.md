# WhatsApp/SMS Business Agent `communication/business-messaging-bot`

prototype · P1 · composite · safety S3 · autonomy L2

## What it does
Handles opted-in customer messaging over WhatsApp/SMS with templates and human handoff.

## When to use / not use
- **Use when:** Performing whatsapp/sms business agent tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `communication/business-messaging-bot` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/business-messaging-bot
afe test communication/business-messaging-bot
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/chat

## Safety
- Safety tier: `S3`
- Side effects: ['communication-action']
- Approval gates: ['send_customer_message']

## Evaluation
Run `afe test communication/business-messaging-bot` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
