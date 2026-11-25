# Safety Review — `finance/accounts-receivable`

- **Safety Level:** `S3`
- **Autonomy:** `L2`
- **Approval Gates:** ['approve_external_action']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Accounting/tax workflow assistant; does not provide regulated investment advice and requires human finance sign-off for ledger postings.
