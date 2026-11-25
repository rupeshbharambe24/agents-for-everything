# Safety Review — `banking/grievance-redressal`

- **Safety Level:** `S3`
- **Autonomy:** `L2`
- **Approval Gates:** ['approve_external_action']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.
