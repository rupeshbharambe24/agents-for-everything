# Safety Review — `insurance/renewal-agent`

- **Safety Level:** `S3`
- **Autonomy:** `L2`
- **Approval Gates:** ['approve_external_action']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.
