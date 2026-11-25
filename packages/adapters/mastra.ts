import fs from "node:fs";
import path from "node:path";
import { AgentRunner, loadAgentManifest } from "../core-typescript/src/index.ts";

export function asMastraAgentSpec(repoRoot: string, agentDirOrRel: string) {
  const fullDir = path.isAbsolute(agentDirOrRel)
    ? agentDirOrRel
    : path.join(repoRoot, agentDirOrRel);
  const manifest = loadAgentManifest(fullDir);
  const instructions = fs.readFileSync(path.join(fullDir, "prompts", "system.md"), "utf-8");
  const runner = new AgentRunner(repoRoot);

  return {
    name: manifest.metadata.id,
    instructions,
    execute: (input: Record<string, unknown>) => runner.run(fullDir, input),
  };
}
