# Accounts Payable Team (`team/accounts-payable-team`)

Parses vendor invoices, matches against POs, audits expenses, and routes to human finance sign-off.

Flow: `invoice-receipt-parser -> accounts-payable -> expense-auditor -> human-approval-gate`
