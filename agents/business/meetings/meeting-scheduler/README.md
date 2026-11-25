# Meeting Scheduler `meetings/meeting-scheduler`

prototype · P0 · composite · safety S3 · autonomy L2

## What it does
Coordinates free/busy windows across participants and drafts calendar invites safely.

## When to use / not use
- **Use when:** Proposing and scheduling multi-party meetings.
- **Do not use when:** Resolving personal to-do lists.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `meetings/meeting-scheduler` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add meetings/meeting-scheduler
afe test meetings/meeting-scheduler
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/calendar, afe/email

## Safety
- Safety tier: `S3`
- Side effects: ['creates-calendar-invite']
- Approval gates: ['send_invite']

## Evaluation
Run `afe test meetings/meeting-scheduler` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
