# Human-in-the-Loop Gate `orchestration/human-approval-gate`

beta · P0 · atomic · safety S1 · autonomy L2

## What it does
Enforces explicit human confirmation and emits an audit log entry prior to external or high-stakes actions.

## When to use / not use
- **Use when:** Before submitting forms, sending emails, running destructive shell commands, or moving money.
- **Do not use when:** Pure read-only S0 calculations.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S1) and declared tool limits.
3. Executes core `orchestration/human-approval-gate` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add orchestration/human-approval-gate
afe test orchestration/human-approval-gate
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
afe/chat

## Safety
- Level: `S1`
- Side effects: ['none']
- Approval required for: ['approve_action']

## Evaluation
Run `afe test orchestration/human-approval-gate` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
