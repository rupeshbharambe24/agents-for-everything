export type SafetyLevel = "S0" | "S1" | "S2" | "S3" | "S4";
export type AutonomyLevel = "L0" | "L1" | "L2" | "L3" | "L4";

export interface AgentManifest {
  apiVersion: "afe/v1";
  kind: "Agent";
  metadata: {
    id: string;
    name: string;
    version: string;
    family: string;
    category: string;
    tier: "atomic" | "composite";
    maturity: "spec" | "prototype" | "beta" | "stable" | "deprecated";
    priority: "P0" | "P1" | "P2";
    tags?: string[];
    maintainers?: string[];
    license: string;
  };
  spec: {
    summary: string;
    purpose: string;
    pattern: string;
    autonomy: AutonomyLevel;
    io: { input: string; output: string };
    model: {
      capabilities: string[];
      optional_capabilities?: string[];
      min_context_tokens?: number;
      tested_with?: string[];
    };
    tools?: { required?: string[]; optional?: string[] };
    uses_agents?: string[];
    memory?: "none" | "session" | "long-term";
    safety: {
      level: SafetyLevel;
      side_effects?: string[];
      approval_required_for?: string[];
      handles_pii?: boolean;
      data_retention?: string;
    };
    limits: {
      max_steps: number;
      timeout_seconds: number;
      max_cost_usd: number;
    };
    evals: { suite: string; targets?: Record<string, number> };
    exports?: string[];
    locales?: string[];
  };
}

export interface RunContext {
  providerName?: "auto" | "mock" | "openai" | "anthropic" | "gemini" | "ollama";
  model?: string;
  autoApprove?: boolean;
  locale?: string;
}

export interface TraceSpan {
  spanId: string;
  name: string;
  startTimeMs: number;
  endTimeMs: number;
  status: "OK" | "ERROR";
  attributes: Record<string, unknown>;
}

export interface RunResult {
  agentId: string;
  output: Record<string, unknown>;
  status: "ok" | "error";
  steps: number;
  latencyMs: number;
  trace: TraceSpan[];
}
