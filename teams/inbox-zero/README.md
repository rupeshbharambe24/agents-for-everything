<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **Inbox Zero Team**

# 👥 Inbox Zero Team

![team: inbox-zero](https://img.shields.io/badge/team-inbox--zero-0f172a?style=flat-square) ![pattern: prompt-chaining](https://img.shields.io/badge/pattern-prompt--chaining-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square)

> Triages inbox emails, drafts replies, extracts action items, and waits for human approval.

## 🔀 Workflow

```mermaid
flowchart LR
    inbox_triager["Inbox Triager"] --> email_drafter["Email Drafter"]
    email_drafter["Email Drafter"] --> action_item_extractor["Action Item Extractor"]
    action_item_extractor["Action Item Extractor"] --> human_approval_gate{{"Human-in-the-Loop Gate"}}
```

Starts at `communication/inbox-triager`. Human approval at: `human-approval-gate`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`communication/inbox-triager`](../../agents/business/communication/inbox-triager/README.md) | Sorts, prioritizes, and labels emails; surfaces urgent threads and reply-needed items. | S1 |
| [`communication/email-drafter`](../../agents/business/communication/email-drafter/README.md) | Drafts context-matched email replies and saves them as drafts without sending autonomously. | S2 |
| [`meetings/action-item-extractor`](../../agents/business/meetings/action-item-extractor/README.md) | Pulls concrete tasks with owners and due dates from meeting notes, transcripts, or chats. | S2 |
| [`orchestration/human-approval-gate`](../../agents/core/orchestration/human-approval-gate/README.md) | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. | S1 |

## 🚀 Try it

```bash
afe graph inbox-zero   # print the workflow and check that agent contracts fit
for a in communication/inbox-triager communication/email-drafter meetings/action-item-extractor orchestration/human-approval-gate; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
