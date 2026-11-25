import path from "node:path";
import { AgentRunner, type RunContext, type RunResult } from "../../../../../../packages/core-typescript/src/index.ts";

const AGENT_REL_DIR = "agents/information/search/answer-engine";

export async function run(
  input: Record<string, unknown>,
  context: RunContext = { providerName: "mock" },
  repoRoot = path.resolve(import.meta.dirname, "../../../../../..")
): Promise<RunResult> {
  const runner = new AgentRunner(repoRoot);
  return runner.run(AGENT_REL_DIR, input, context);
}
