# Teach-by-Showing Recorder `computer-use/macro-recorder`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Watches the user do a task once and turns it into a reusable, parameterized workflow.

## When to use / not use
- **Use when:** You need single-purpose teach-by-showing recorder (recording → workflow).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `computer-use/macro-recorder` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add computer-use/macro-recorder
afe test computer-use/macro-recorder
```

## Composes with
computer-use/desktop-operator, vision/screenshot-understander

## Tools required
afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test computer-use/macro-recorder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
