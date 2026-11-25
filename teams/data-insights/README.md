<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **Data Insights Team**

# 👥 Data Insights Team

![team: data-insights](https://img.shields.io/badge/team-data--insights-0f172a?style=flat-square) ![pattern: plan-and-execute](https://img.shields.io/badge/pattern-plan--and--execute-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square)

> Clarifies a business question, writes read-only SQL, analyzes results, specs a chart, and reports.

## 🔀 Workflow

```mermaid
flowchart LR
    clarifier["Clarifier"] --> text_to_sql["Text-to-SQL"]
    text_to_sql["Text-to-SQL"] --> data_analyst["Data Analyst"]
    data_analyst["Data Analyst"] --> chart_maker["Chart Maker"]
    chart_maker["Chart Maker"] --> report_writer["Report Writer"]
```

Starts at `orchestration/clarifier`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`orchestration/clarifier`](../../agents/core/orchestration/clarifier/README.md) | Detects ambiguous or under-specified requests and asks the fewest clarifying questions. | S0 |
| [`data/text-to-sql`](../../agents/builders/data/text-to-sql/README.md) | Converts natural-language questions into safe read-only SELECT queries against a schema. | S1 |
| [`data/data-analyst`](../../agents/builders/data/data-analyst/README.md) | Cleans datasets, computes descriptive statistics, and drafts plain-language insights. | S1 |
| [`data/chart-maker`](../../agents/builders/data/chart-maker/README.md) | Selects appropriate chart encodings and emits Vega-Lite/chart specs with captions. | S0 |
| [`research/report-writer`](../../agents/information/research/report-writer/README.md) | Turns research findings into structured Markdown reports with executive summaries and references. | S0 |

## 🚀 Try it

```bash
afe graph data-insights   # print the workflow and check that agent contracts fit
for a in orchestration/clarifier data/text-to-sql data/data-analyst data/chart-maker research/report-writer; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
