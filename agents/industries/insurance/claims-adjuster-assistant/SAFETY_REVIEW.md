# Safety Review — `insurance/claims-adjuster-assistant`

- **Safety Level:** `S4`
- **Autonomy:** `L2`
- **Approval Gates:** ['human_officer_signoff']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.
