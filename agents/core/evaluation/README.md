# Evaluation and quality (`evaluation/`)

- **Family:** `core` · **Directory:** `agents/core/evaluation/`
- **Total Agents:** 6 (P0: 1, P1: 2, P2: 3)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`evaluation/llm-judge`](llm-judge/README.md) | LLM Judge | atomic | P0 | `beta` | S0 | Scores outputs against a rubric with calibrated, explained verdicts. |
| [`evaluation/regression-runner`](regression-runner/README.md) | Regression Runner | composite | P1 | `prototype` | S1 | Runs eval suites across code or prompt edits and compares pass rates against baselines. |
| [`evaluation/test-case-generator`](test-case-generator/README.md) | Test Case Generator | atomic | P1 | `prototype` | S0 | Synthesizes normal, edge, and adversarial JSONL eval cases from an agent manifest and schemas. |
| [`evaluation/benchmark-runner`](benchmark-runner/README.md) | Benchmark Runner | composite | P2 | `prototype` | S1 | Runs public benchmarks (tool use, web tasks, coding) against agents and publishes results. |
| [`evaluation/feedback-collector`](feedback-collector/README.md) | Feedback Collector | atomic | P2 | `prototype` | S1 | Turns user thumbs-down and corrections into new eval cases. |
| [`evaluation/trace-analyzer`](trace-analyzer/README.md) | Trace Analyzer | atomic | P2 | `prototype` | S1 | Mines production traces to find and cluster failure patterns; explains why an agent failed. |

## Horizontal Composition & Reuse
- **Direct `uses_agents` Dependencies:** `evaluation/llm-judge`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category evaluation
afe add evaluation/llm-judge --dest ./my-app/agents
afe test evaluation/llm-judge
```
