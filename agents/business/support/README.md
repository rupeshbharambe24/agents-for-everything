# Customer support and success (`support/`)

- **Family:** `business` · **Directory:** `agents/business/support/`
- **Total Agents:** 11 (P0: 3, P1: 4, P2: 4)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`support/reply-drafter`](reply-drafter/README.md) | Reply Drafter | composite | P0 | `beta` | S2 | Drafts KB-grounded support replies for human agents to review and send. |
| [`support/support-chatbot`](support-chatbot/README.md) | Support Assistant | composite | P0 | `beta` | S1 | Answers customer questions from KB docs with citations and flags handoffs when uncertain. |
| [`support/ticket-triager`](ticket-triager/README.md) | Ticket Triager | atomic | P0 | `beta` | S2 | Classifies, prioritizes, and routes incoming support tickets cleanly. |
| [`support/escalation-detector`](escalation-detector/README.md) | Escalation Detector | atomic | P1 | `prototype` | S1 | Detects customer frustration, churn signals, legal threats, or safety issues for escalation. |
| [`support/kb-writer`](kb-writer/README.md) | Knowledge Base Writer | composite | P1 | `prototype` | S2 | Converts resolved support tickets into clean KB articles and highlights missing docs. |
| [`support/order-status-agent`](order-status-agent/README.md) | Order Status Agent | atomic | P1 | `prototype` | S1 | Queries order and shipment tracking APIs and explains status clearly to customers. |
| [`support/voice-of-customer`](voice-of-customer/README.md) | Voice of Customer Analyst | composite | P1 | `prototype` | S1 | Clusters themes across support tickets, reviews, and calls with quantified counts. |
| [`support/churn-risk-predictor`](churn-risk-predictor/README.md) | Churn Risk Predictor | atomic | P2 | `prototype` | S1 | Predicts accounts at risk and suggests save actions. |
| [`support/customer-onboarding-guide`](customer-onboarding-guide/README.md) | Customer Onboarding Guide | composite | P2 | `prototype` | S2 | Guides new customers through setup with in-app tips and check-ins. |
| [`support/returns-refunds-agent`](returns-refunds-agent/README.md) | Returns & Refunds Agent | composite | P2 | `prototype` | S4 | Checks return eligibility and prepares refunds; refunds need human approval. |
| [`support/support-qa-auditor`](support-qa-auditor/README.md) | Support QA Auditor | atomic | P2 | `prototype` | S1 | Scores support conversations against a quality rubric. |

## Horizontal Composition & Reuse
- **Direct `uses_agents` Dependencies:** `search/rag-qa`, `support/ticket-triager`, `text/sentiment-analyzer`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category support
afe add support/reply-drafter --dest ./my-app/agents
afe test support/reply-drafter
```
