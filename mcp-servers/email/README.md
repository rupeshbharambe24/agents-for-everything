<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Email Draft & Read MCP Server**

# 🧰 Email Draft & Read MCP Server

![id: afe/email](https://img.shields.io/badge/id-afe%2Femail-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Read inbox threads, apply labels, and create drafts without sending autonomously.

**Backed by:** gmail / imap-smtp MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `list_threads` | Search and read inbox threads. | ✅ |
| `save_draft` | Save reply or new email draft for human review. |  |

## 🤖 Used by 16 agents

[`communication/contact-manager`](../../agents/business/communication/contact-manager/README.md), [`communication/email-drafter`](../../agents/business/communication/email-drafter/README.md), [`communication/follow-up-tracker`](../../agents/business/communication/follow-up-tracker/README.md), [`communication/inbox-triager`](../../agents/business/communication/inbox-triager/README.md), [`communication/newsletter-digest`](../../agents/business/communication/newsletter-digest/README.md), [`communication/unsubscribe-cleaner`](../../agents/business/communication/unsubscribe-cleaner/README.md), [`community/event-organizer`](../../agents/life/community/event-organizer/README.md), [`finance/accounts-receivable`](../../agents/business/finance/accounts-receivable/README.md), [`integration/email-to-action`](../../agents/action/integration/email-to-action/README.md), [`integration/notification-dispatcher`](../../agents/action/integration/notification-dispatcher/README.md), [`meetings/meeting-follow-up`](../../agents/business/meetings/meeting-follow-up/README.md), [`meetings/meeting-prep`](../../agents/business/meetings/meeting-prep/README.md), [`meetings/meeting-scheduler`](../../agents/business/meetings/meeting-scheduler/README.md), [`personal/bill-subscription-manager`](../../agents/life/personal/bill-subscription-manager/README.md), [`personal/digital-declutterer`](../../agents/life/personal/digital-declutterer/README.md), [`productivity/daily-briefer`](../../agents/life/productivity/daily-briefer/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
