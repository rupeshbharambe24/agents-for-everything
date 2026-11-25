import type { AgentManifest } from "./types.ts";

const PII_PATTERNS: Array<[RegExp, string]> = [
  [/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g, "[REDACTED_EMAIL]"],
  [/\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b/g, "[REDACTED_ID_12]"],
  [/\bsk-[A-Za-z0-9_-]{12,}\b/g, "[REDACTED_API_KEY]"],
];

export function redactPii(text: string): string {
  let out = text;
  for (const [pat, repl] of PII_PATTERNS) out = out.replace(pat, repl);
  return out;
}

export function requireApproval(
  manifest: AgentManifest,
  action: string,
  autoApprove = false
): void {
  const gated =
    (manifest.spec.safety.approval_required_for ?? []).includes(action) ||
    manifest.spec.safety.level === "S3" ||
    manifest.spec.safety.level === "S4";
  if (gated && !autoApprove) {
    throw new Error(
      `Approval required for ${manifest.metadata.id} (${manifest.spec.safety.level}) action '${action}'`
    );
  }
}
