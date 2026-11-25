import type { AgentManifest } from "./types.ts";

export function exportA2ACard(
  manifest: AgentManifest,
  inputSchema: Record<string, unknown>,
  outputSchema: Record<string, unknown>
): Record<string, unknown> {
  return {
    name: manifest.metadata.name,
    id: manifest.metadata.id,
    version: manifest.metadata.version,
    description: manifest.spec.summary,
    skills: [
      {
        id: manifest.metadata.id,
        name: manifest.metadata.name,
        description: manifest.spec.purpose,
        inputSchema,
        outputSchema,
      },
    ],
    metadata: {
      safetyLevel: manifest.spec.safety.level,
      autonomyLevel: manifest.spec.autonomy,
      maturity: manifest.metadata.maturity,
      license: manifest.metadata.license,
    },
  };
}

export function exportAgentSkillMd(manifest: AgentManifest, systemPrompt: string): string {
  const slug = manifest.metadata.id.split("/")[1] ?? manifest.metadata.id;
  return [
    "---",
    `name: ${slug}`,
    `description: ${manifest.spec.summary}`,
    "---",
    "",
    `# ${manifest.metadata.name} (\`${manifest.metadata.id}\`)`,
    "",
    manifest.spec.purpose,
    "",
    "## Instructions",
    "",
    systemPrompt.trim(),
    "",
  ].join("\n");
}
