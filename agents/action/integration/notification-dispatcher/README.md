# Notification Dispatcher `integration/notification-dispatcher`

prototype · P1 · atomic · safety S3 · autonomy L2

## What it does
Routes alerts to email, chat, or SMS respecting quiet hours and user approval.

## When to use / not use
- **Use when:** Performing notification dispatcher tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `integration/notification-dispatcher` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add integration/notification-dispatcher
afe test integration/notification-dispatcher
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/email, afe/chat

## Safety
- Safety tier: `S3`
- Side effects: ['integration-action']
- Approval gates: ['send_notification']

## Evaluation
Run `afe test integration/notification-dispatcher` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
