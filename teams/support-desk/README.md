<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **Support Desk Team**

# 👥 Support Desk Team

![team: support-desk](https://img.shields.io/badge/team-support--desk-0f172a?style=flat-square) ![pattern: routing](https://img.shields.io/badge/pattern-routing-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square)

> Triages customer tickets, retrieves KB answers, drafts replies, and gates risky escalations.

## 🔀 Workflow

```mermaid
flowchart LR
    ticket_triager["Ticket Triager"] --> support_chatbot["Support Assistant"]
    support_chatbot["Support Assistant"] --> reply_drafter["Reply Drafter"]
    reply_drafter["Reply Drafter"] --> human_approval_gate{{"Human-in-the-Loop Gate"}}
```

Starts at `support/ticket-triager`. Human approval at: `human-approval-gate`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`support/ticket-triager`](../../agents/business/support/ticket-triager/README.md) | Classifies, prioritizes, and routes incoming support tickets cleanly. | S2 |
| [`support/support-chatbot`](../../agents/business/support/support-chatbot/README.md) | Answers customer questions from KB docs with citations and flags handoffs when uncertain. | S1 |
| [`support/reply-drafter`](../../agents/business/support/reply-drafter/README.md) | Drafts KB-grounded support replies for human agents to review and send. | S2 |
| [`orchestration/human-approval-gate`](../../agents/core/orchestration/human-approval-gate/README.md) | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. | S1 |

## 🚀 Try it

```bash
afe graph support-desk   # print the workflow and check that agent contracts fit
for a in support/ticket-triager support/support-chatbot support/reply-drafter orchestration/human-approval-gate; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
