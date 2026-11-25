# Safety Review — `physical/drone-mission-planner`

- **Safety Level:** `S4`
- **Autonomy:** `L2`
- **Approval Gates:** ['human_officer_signoff']
- **Handles PII:** `True` (`data_retention: none`)
- **Reviewer:** `@rupeshbharambe24`

## Verification Controls
- Unapproved execution with `execute: true` raises `ApprovalRequiredError`.
- Trace collector masks PII spans by default (`redact_pii`).
- **Domain Disclaimer:** Physical/robotic safety assistant; confirm hazardous, irreversible, or actuator commands with a human operator and verify safety interlocks.
