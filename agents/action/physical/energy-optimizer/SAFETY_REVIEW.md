# Safety Review — `physical/energy-optimizer`

- **Safety Level:** `S3`
- **Autonomy:** `L2`
- **Approval Gates:** ['approve_external_action']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Physical/robotic safety assistant; confirm hazardous, irreversible, or actuator commands with a human operator and verify safety interlocks.
