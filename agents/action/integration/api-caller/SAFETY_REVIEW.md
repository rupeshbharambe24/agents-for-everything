# Security & Safety Review — `integration/api-caller`

- **Safety Level:** `S3`
- **Reviewer:** `@rupeshbharambe24`
- **Status:** Approved for `beta`

## Controls Verified
1. All external side effects are gated by `approval_required_for` and `SafetyPolicy.require_approval`.
2. Unapproved calls raise `ApprovalRequiredError` in deterministic eval tests.
3. Declared MCP tool scopes in `tools.yaml` follow least privilege.
