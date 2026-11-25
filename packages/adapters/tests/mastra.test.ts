import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import { asMastraAgentSpec } from "../mastra.ts";

test("Mastra adapter loads and runs real repo agent", async () => {
  const root = path.resolve(import.meta.dirname, "../../..");
  const spec = asMastraAgentSpec(root, "agents/information/text/summarizer");
  assert.equal(spec.name, "text/summarizer");
  const res = await spec.execute({ text: "Mastra adapter test sentence." });
  assert.equal(res.status, "ok");
  assert.ok(res.output);
});
