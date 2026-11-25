import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import {
  AgentRunner,
  exportA2ACard,
  exportAgentSkillMd,
  loadAgentManifest,
  parseYaml,
  redactPii,
  requireApproval,
  validateJsonSchema,
} from "../src/index.ts";

test("parseYaml parses afe manifest structures", () => {
  const parsed = parseYaml(`
apiVersion: afe/v1
kind: Agent
metadata:
  id: text/summarizer
  tags: [text, nlp]
spec:
  limits:
    max_steps: 5
`);
  assert.equal(parsed.apiVersion, "afe/v1");
  assert.deepEqual((parsed.metadata as Record<string, unknown>).tags, ["text", "nlp"]);
});

test("AgentRunner validates, runs mock provider, and exports", async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "afe-ts-"));
  try {
    const agentDir = path.join(tmp, "agents", "information", "text", "echo");
    fs.mkdirSync(path.join(agentDir, "prompts"), { recursive: true });
    fs.mkdirSync(path.join(agentDir, "schemas"), { recursive: true });
    fs.mkdirSync(path.join(tmp, "spec", "types"), { recursive: true });

    fs.writeFileSync(
      path.join(agentDir, "agent.yaml"),
      `apiVersion: afe/v1
kind: Agent
metadata:
  id: text/echo
  name: Echo
  version: 0.1.0
  family: information
  category: text
  tier: atomic
  maturity: spec
  priority: P0
  license: Apache-2.0
spec:
  summary: Echo test agent.
  purpose: Validates TypeScript runner.
  pattern: augmented-llm
  autonomy: L1
  io:
    input: schemas/input.schema.json
    output: schemas/output.schema.json
  model:
    capabilities: [structured_output]
  safety:
    level: S3
    approval_required_for: [send]
  limits:
    max_steps: 5
    timeout_seconds: 10
    max_cost_usd: 0.01
  evals:
    suite: evals/eval.yaml
`
    );
    fs.writeFileSync(path.join(agentDir, "prompts", "system.md"), "Return JSON.");
    const schema = {
      type: "object",
      required: ["text"],
      properties: { text: { type: "string" } },
    };
    fs.writeFileSync(path.join(agentDir, "schemas", "input.schema.json"), JSON.stringify(schema));
    fs.writeFileSync(path.join(agentDir, "schemas", "output.schema.json"), JSON.stringify(schema));

    const runner = new AgentRunner(tmp);
    const result = await runner.run(agentDir, { text: "hello ts" }, { providerName: "mock" });
    assert.equal(result.status, "ok");
    assert.equal(result.output.text, "hello ts");

    const manifest = loadAgentManifest(agentDir);
    assert.throws(() => requireApproval(manifest, "send", false));
    assert.doesNotThrow(() => requireApproval(manifest, "send", true));

    const card = exportA2ACard(manifest, schema, schema);
    assert.equal(card.id, "text/echo");
    const skill = exportAgentSkillMd(manifest, "Return JSON.");
    assert.ok(skill.includes("name: echo"));
    assert.equal(validateJsonSchema({ text: "ok" }, schema).length, 0);
    assert.ok(redactPii("contact a@b.com").includes("[REDACTED_EMAIL]"));
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
});
