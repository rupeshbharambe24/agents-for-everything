<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **Meeting-to-Done Team**

# 👥 Meeting-to-Done Team

![team: meeting-to-done](https://img.shields.io/badge/team-meeting--to--done-0f172a?style=flat-square) ![pattern: prompt-chaining](https://img.shields.io/badge/pattern-prompt--chaining-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![safety: S2](https://img.shields.io/badge/safety-S2-ca8a04?style=flat-square)

> Converts meeting audio into structured notes, extracted action items, and prioritized tasks.

## 🔀 Workflow

```mermaid
flowchart LR
    meeting_notetaker["Meeting Notetaker"] --> action_item_extractor["Action Item Extractor"]
    action_item_extractor["Action Item Extractor"] --> task_manager["Task Manager"]
```

Starts at `meetings/meeting-notetaker`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`meetings/meeting-notetaker`](../../agents/business/meetings/meeting-notetaker/README.md) | Transcribes meetings and produces structured summaries with decisions and risks. | S1 |
| [`meetings/action-item-extractor`](../../agents/business/meetings/action-item-extractor/README.md) | Pulls concrete tasks with owners and due dates from meeting notes, transcripts, or chats. | S2 |
| [`productivity/task-manager`](../../agents/life/productivity/task-manager/README.md) | Captures tasks from notes, chat, or voice, prioritizes them, and structures a daily plan. | S2 |

## 🚀 Try it

```bash
afe graph meeting-to-done   # print the workflow and check that agent contracts fit
for a in meetings/meeting-notetaker meetings/action-item-extractor productivity/task-manager; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
