# Safety Review Guide (`S3` and `S4` Agents)

Pull requests adding or modifying `S3` (external side effects) or `S4` (money, legal, clinical, identity, irreversible deletion) agents require explicit Safety Reviewer approval:

- Verify `spec.safety.approval_required_for` lists every external write, send, submit, payment, or destructive call.
- Confirm `handles_pii` is `true` whenever personal names, emails, phones, IDs, or financial/health data enter the agent.
- Confirm evals include adversarial tests ensuring unapproved calls raise `ApprovalRequiredError` instead of executing silently.
- Confirm domain disclaimers exist in `README.md` for finance, legal, and healthcare agents.
