import fs from "node:fs";
import path from "node:path";
import { resolveProvider, type ModelProvider } from "./providers.ts";
import { redactPii } from "./safety.ts";
import { validateJsonSchema, type JsonSchema } from "./schema.ts";
import type { AgentManifest, RunContext, RunResult, TraceSpan } from "./types.ts";
import { parseYaml } from "./yaml_lite.ts";

export function loadAgentManifest(agentDir: string): AgentManifest {
  const raw = fs.readFileSync(path.join(agentDir, "agent.yaml"), "utf-8");
  return parseYaml(raw) as unknown as AgentManifest;
}

export class AgentRunner {
  private readonly repoRoot: string;
  private readonly typesDir: string;

  constructor(repoRoot: string) {
    this.repoRoot = path.resolve(repoRoot);
    this.typesDir = path.join(this.repoRoot, "spec", "types");
  }

  async run(
    agentDirOrRel: string,
    inputData: Record<string, unknown>,
    ctx: RunContext = {},
    customProvider?: ModelProvider
  ): Promise<RunResult> {
    const agentDir = path.isAbsolute(agentDirOrRel)
      ? agentDirOrRel
      : path.join(this.repoRoot, agentDirOrRel);
    const manifest = loadAgentManifest(agentDir);
    const inputSchema = JSON.parse(
      fs.readFileSync(path.join(agentDir, manifest.spec.io.input), "utf-8")
    ) as JsonSchema;
    const outputSchema = JSON.parse(
      fs.readFileSync(path.join(agentDir, manifest.spec.io.output), "utf-8")
    ) as JsonSchema;
    const systemPrompt = fs.readFileSync(path.join(agentDir, "prompts", "system.md"), "utf-8");

    const inErrors = validateJsonSchema(inputData, inputSchema, this.typesDir);
    if (inErrors.length > 0) {
      throw new Error(`Invalid input for ${manifest.metadata.id}: ${inErrors.join("; ")}`);
    }

    const provider = customProvider ?? resolveProvider(ctx.providerName ?? "auto", ctx.model);
    const startMs = Date.now();
    const resp = await provider.complete({
      systemPrompt,
      userPayload: inputData,
      outputSchema,
    });
    const output = resp.parsedJson ?? { text: resp.content };
    const outErrors = validateJsonSchema(output, outputSchema, this.typesDir);
    if (outErrors.length > 0) {
      throw new Error(`Invalid output from ${manifest.metadata.id}: ${outErrors.join("; ")}`);
    }

    const endMs = Date.now();
    const span: TraceSpan = {
      spanId: `${startMs}`,
      name: `afe.agent.run.${manifest.metadata.id}`,
      startTimeMs: startMs,
      endTimeMs: endMs,
      status: "OK",
      attributes: {
        "afe.agent.id": manifest.metadata.id,
        "gen_ai.system": provider.name,
        "gen_ai.request.model": provider.model,
        "afe.safety.level": manifest.spec.safety.level,
        "afe.note": redactPii(manifest.spec.summary),
      },
    };

    return {
      agentId: manifest.metadata.id,
      output,
      status: "ok",
      steps: 1,
      latencyMs: endMs - startMs,
      trace: [span],
    };
  }
}
