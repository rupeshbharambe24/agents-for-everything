# Issue Triager `coding/issue-triager`

prototype · P1 · atomic · safety S3 · autonomy L2

## What it does
Labels, deduplicates, and prioritizes repository issues and asks for missing repro steps.

## When to use / not use
- **Use when:** Performing issue triager tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `coding/issue-triager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/issue-triager
afe test coding/issue-triager
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/issue-tracker

## Safety
- Safety tier: `S3`
- Side effects: ['coding-action']
- Approval gates: ['post_issue_comment_or_labels']

## Evaluation
Run `afe test coding/issue-triager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
