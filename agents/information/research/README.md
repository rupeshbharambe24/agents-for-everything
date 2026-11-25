# Research and analysis (`research/`)

- **Family:** `information` · **Directory:** `agents/information/research/`
- **Total Agents:** 15 (P0: 4, P1: 6, P2: 5)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`research/deep-researcher`](deep-researcher/README.md) | Deep Researcher | composite | P0 | `beta` | S1 | Plans research questions, searches iteratively, reads sources, fact-checks, and writes a cited report. |
| [`research/fact-checker`](fact-checker/README.md) | Fact Checker | composite | P0 | `beta` | S1 | Verifies discrete claims against web or retrieved sources and outputs verdicts with evidence. |
| [`research/report-writer`](report-writer/README.md) | Report Writer | atomic | P0 | `beta` | S0 | Turns research findings into structured Markdown reports with executive summaries and references. |
| [`research/source-reader`](source-reader/README.md) | Source Reader | atomic | P0 | `beta` | S1 | Reads one URL or document deeply and extracts key points, facts, and quotes. |
| [`research/comparison-analyst`](comparison-analyst/README.md) | Comparison Analyst | atomic | P1 | `prototype` | S1 | Scores options X vs Y vs Z against weighted criteria with transparent trade-offs. |
| [`research/competitive-analyst`](competitive-analyst/README.md) | Competitive Analyst | composite | P1 | `prototype` | S1 | Builds competitor profiles and pricing/feature comparison matrices. |
| [`research/interview-synthesizer`](interview-synthesizer/README.md) | User Research Synthesizer | composite | P1 | `prototype` | S1 | Synthesizes user interview transcripts into insights, pain points, and quotes. |
| [`research/literature-reviewer`](literature-reviewer/README.md) | Literature Reviewer | composite | P1 | `prototype` | S1 | Conducts structured PRISMA-style screening, extraction, and synthesis across academic papers. |
| [`research/market-researcher`](market-researcher/README.md) | Market Researcher | composite | P1 | `prototype` | S1 | Synthesizes market sizing, segments, trends, and explicit assumptions with sources. |
| [`research/survey-analyst`](survey-analyst/README.md) | Survey Analyst | composite | P1 | `prototype` | S1 | Codes open-ended survey answers into themes with counts and representative quotes. |
| [`research/citation-manager`](citation-manager/README.md) | Citation Manager | atomic | P2 | `prototype` | S1 | Formats references, finds DOIs and checks every citation exists. |
| [`research/due-diligence`](due-diligence/README.md) | Due Diligence Analyst | composite | P2 | `prototype` | S1 | Background checks on companies and vendors from public sources (filings, litigation, news). |
| [`research/hypothesis-generator`](hypothesis-generator/README.md) | Hypothesis Generator | atomic | P2 | `prototype` | S0 | Proposes testable hypotheses from data or literature. |
| [`research/policy-analyst`](policy-analyst/README.md) | Policy Analyst | composite | P2 | `prototype` | S1 | Analyzes a regulation or policy proposal: who it affects and how. |
| [`research/trend-spotter`](trend-spotter/README.md) | Trend Spotter | composite | P2 | `prototype` | S1 | Detects emerging trends across news, social media, papers and patents. |

## Horizontal Composition & Reuse
- **Direct `uses_agents` Dependencies:** `research/fact-checker`, `research/report-writer`, `research/source-reader`, `search/academic-search`, `search/web-search`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category research
afe add research/deep-researcher --dest ./my-app/agents
afe test research/deep-researcher
```
