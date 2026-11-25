# Product Feedback Prioritizer `operations/product-feedback-prioritizer`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Clusters feedback and scores ideas (RICE) to draft a roadmap.

## When to use / not use
- **Use when:** You need single-purpose product feedback prioritizer (feedback → prioritized backlog).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `operations/product-feedback-prioritizer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add operations/product-feedback-prioritizer
afe test operations/product-feedback-prioritizer
```

## Composes with
orchestration/task-planner, text/summarizer

## Tools required
afe/issue-tracker

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test operations/product-feedback-prioritizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
