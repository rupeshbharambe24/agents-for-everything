<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Invoice Automation**

# 🍳 Invoice Automation

![recipe: invoice-automation](https://img.shields.io/badge/recipe-invoice--automation-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square)

> Email inbox to extracted invoices, PO matching, and human-approved payment queue.

| | |
|---|---|
| **Problem** | Finance teams manually copy invoice emails into ERP bills and verify PO totals. |
| **Solution** | Composes inbox-triager, invoice-receipt-parser, accounts-payable, and human-approval-gate. |

## 🚀 Run it

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/invoice-automation/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/invoice-automation/tests/test_recipe.py
```

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`communication/inbox-triager`](../../agents/business/communication/inbox-triager/README.md) | Sorts, prioritizes, and labels emails; surfaces urgent threads and reply-needed items. | S1 |
| [`documents/invoice-receipt-parser`](../../agents/action/documents/invoice-receipt-parser/README.md) | Extracts vendor, date, line items, GST/VAT tax, and total from invoices and verifies the math. | S1 |
| [`finance/accounts-payable`](../../agents/business/finance/accounts-payable/README.md) | Matches parsed invoices against PO/receipt totals and prepares an approval queue (no autonomous payment). | S4 |
| [`orchestration/human-approval-gate`](../../agents/core/orchestration/human-approval-gate/README.md) | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. | S1 |

**Teams:** [`accounts-payable-team`](../../teams/accounts-payable-team/README.md)

**MCP servers:** [`afe/email`](../../mcp-servers/email/README.md), [`afe/documents`](../../mcp-servers/documents/README.md), [`afe/accounting`](../../mcp-servers/accounting/README.md)

<!-- afe:end-generated -->
