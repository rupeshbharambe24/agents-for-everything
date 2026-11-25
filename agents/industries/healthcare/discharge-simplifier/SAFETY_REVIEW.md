# Safety Review — `healthcare/discharge-simplifier`

- **Safety Level:** `S4`
- **Autonomy:** `L2`
- **Approval Gates:** ['human_officer_signoff']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.
