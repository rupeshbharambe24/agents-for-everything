# HR and recruiting (`hr/`)

- **Family:** `business` · **Directory:** `agents/business/hr/`
- **Total Agents:** 12 (P0: 0, P1: 4, P2: 8)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`hr/hr-policy-qa`](hr-policy-qa/README.md) | HR Policy Assistant | composite | P1 | `prototype` | S1 | Answers employee policy questions (leave, benefits, travel) with citations to official handbooks. |
| [`hr/jd-writer`](jd-writer/README.md) | Job Description Writer | atomic | P1 | `prototype` | S0 | Writes clear, structured, inclusive job descriptions from role requirements. |
| [`hr/onboarding-buddy`](onboarding-buddy/README.md) | Onboarding Buddy | composite | P1 | `prototype` | S1 | Guides new hires through 30-60-90 checklists, tools setup, and internal FAQs. |
| [`hr/resume-screener`](resume-screener/README.md) | Resume Screener | atomic | P1 | `prototype` | S4 | Scores candidate summaries transparently against explicit rubric criteria for human review. |
| [`hr/candidate-sourcer`](candidate-sourcer/README.md) | Candidate Sourcer | composite | P2 | `prototype` | S1 | Finds candidates from public professional sources and drafts outreach. |
| [`hr/employee-survey-analyst`](employee-survey-analyst/README.md) | Employee Survey Analyst | atomic | P2 | `prototype` | S1 | Themes and drivers from engagement surveys. |
| [`hr/exit-interview-analyst`](exit-interview-analyst/README.md) | Exit Interview Analyst | atomic | P2 | `prototype` | S1 | Finds attrition themes from exit interviews. |
| [`hr/interview-kit-builder`](interview-kit-builder/README.md) | Interview Kit Builder | atomic | P2 | `prototype` | S0 | Structured interview questions and scorecards for a role. |
| [`hr/interview-scheduler`](interview-scheduler/README.md) | Interview Scheduler | composite | P2 | `prototype` | S3 | Coordinates interview panels and candidate availability. |
| [`hr/learning-path-designer`](learning-path-designer/README.md) | Learning Path Designer | atomic | P2 | `prototype` | S0 | Builds role-based learning paths from skills gaps. |
| [`hr/offer-letter-generator`](offer-letter-generator/README.md) | Offer Letter Generator | atomic | P2 | `prototype` | S2 | Generates offer letters from approved templates. |
| [`hr/performance-review-helper`](performance-review-helper/README.md) | Performance Review Helper | atomic | P2 | `prototype` | S1 | Synthesizes feedback and goals into a balanced review draft. |

## Horizontal Composition & Reuse
- **Direct `uses_agents` Dependencies:** `documents/document-parser`, `guardrails/pii-redactor`, `search/rag-qa`, `search/web-search`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category hr
afe add hr/hr-policy-qa --dest ./my-app/agents
afe test hr/hr-policy-qa
```
