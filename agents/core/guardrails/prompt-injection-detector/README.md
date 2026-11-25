# Injection Detector `guardrails/prompt-injection-detector`

prototype · P0 · atomic · safety S0 · autonomy L1

## What it does
Detects indirect prompt injection attempts before untrusted data reaches downstream executors.

## When to use / not use
- **Use when:** Before feeding external web pages, PDFs, emails, or speech inputs to tool-calling agents.
- **Do not use when:** Already-trusted internal static config.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S0) and declared tool limits.
3. Executes core `guardrails/prompt-injection-detector` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add guardrails/prompt-injection-detector
afe test guardrails/prompt-injection-detector
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
None (pure computation or orchestrator)

## Safety
- Level: `S0`
- Side effects: ['none']
- Approval required for: ['none']

## Evaluation
Run `afe test guardrails/prompt-injection-detector` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
