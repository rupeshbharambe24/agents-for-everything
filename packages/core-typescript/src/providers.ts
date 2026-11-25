export interface CompletionRequest {
  systemPrompt: string;
  userPayload: Record<string, unknown>;
  outputSchema?: Record<string, unknown>;
}

export interface CompletionResponse {
  content: string;
  parsedJson?: Record<string, unknown>;
  model: string;
  provider: string;
}

export interface ModelProvider {
  readonly name: string;
  readonly model: string;
  complete(req: CompletionRequest): Promise<CompletionResponse>;
}

function defaultValueForProp(
  prop: Record<string, unknown>,
  payload: Record<string, unknown>,
  key: string
): unknown {
  if (key in payload) return payload[key];
  if (Array.isArray(prop.enum) && prop.enum.length > 0) return prop.enum[0];
  if ("default" in prop) return prop.default;
  if (prop.type === "string") {
    return typeof payload.text === "string" ? payload.text.slice(0, 200) : `mock_${key}`;
  }
  if (prop.type === "boolean") return true;
  if (prop.type === "integer" || prop.type === "number") return prop.minimum ?? 1;
  if (prop.type === "array") return [];
  if (prop.type === "object") return {};
  return null;
}

export class MockProvider implements ModelProvider {
  readonly name = "mock";
  readonly model: string;

  constructor(model = "afe-mock-v1") {
    this.model = model;
  }

  async complete(req: CompletionRequest): Promise<CompletionResponse> {
    const schema = req.outputSchema ?? {};
    const props = (schema.properties as Record<string, Record<string, unknown>>) ?? {};
    const required = Array.isArray(schema.required) ? (schema.required as string[]) : [];
    const out: Record<string, unknown> = {};
    for (const key of required) {
      out[key] = defaultValueForProp(props[key] ?? {}, req.userPayload, key);
    }
    for (const key of Object.keys(props)) {
      if (!(key in out) && key in req.userPayload) out[key] = req.userPayload[key];
    }
    const content = JSON.stringify(out);
    return { content, parsedJson: out, model: this.model, provider: this.name };
  }
}

export class OpenAICompatProvider implements ModelProvider {
  readonly name = "openai";
  readonly model: string;
  private readonly apiKey: string;
  private readonly baseUrl: string;

  constructor(
    model = process.env.AFE_MODEL ?? "gpt-4o-mini",
    apiKey = process.env.OPENAI_API_KEY ?? "",
    baseUrl = process.env.OPENAI_BASE_URL ?? "https://api.openai.com/v1"
  ) {
    this.model = model;
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  async complete(req: CompletionRequest): Promise<CompletionResponse> {
    if (!this.apiKey) throw new Error("OPENAI_API_KEY is required");
    const res = await fetch(`${this.baseUrl}/chat/completions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify({
        model: this.model,
        messages: [
          { role: "system", content: req.systemPrompt },
          { role: "user", content: JSON.stringify(req.userPayload) },
        ],
        ...(req.outputSchema ? { response_format: { type: "json_object" } } : {}),
      }),
    });
    if (!res.ok) throw new Error(`OpenAI HTTP ${res.status}: ${await res.text()}`);
    const data = (await res.json()) as { choices: Array<{ message: { content: string } }> };
    const content = data.choices[0]?.message?.content ?? "{}";
    let parsedJson: Record<string, unknown> | undefined;
    try {
      parsedJson = JSON.parse(content) as Record<string, unknown>;
    } catch {
      parsedJson = undefined;
    }
    return { content, parsedJson, model: this.model, provider: this.name };
  }
}

export class OllamaProvider implements ModelProvider {
  readonly name = "ollama";
  readonly model: string;
  private readonly host: string;

  constructor(
    model = process.env.AFE_MODEL ?? "llama3.2",
    host = process.env.OLLAMA_HOST ?? "http://localhost:11434"
  ) {
    this.model = model;
    this.host = host.replace(/\/$/, "");
  }

  async complete(req: CompletionRequest): Promise<CompletionResponse> {
    const res = await fetch(`${this.host}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: this.model,
        stream: false,
        format: req.outputSchema ? "json" : undefined,
        messages: [
          { role: "system", content: req.systemPrompt },
          { role: "user", content: JSON.stringify(req.userPayload) },
        ],
      }),
    });
    if (!res.ok) throw new Error(`Ollama HTTP ${res.status}: ${await res.text()}`);
    const data = (await res.json()) as { message?: { content?: string } };
    const content = data.message?.content ?? "{}";
    let parsedJson: Record<string, unknown> | undefined;
    try {
      parsedJson = JSON.parse(content) as Record<string, unknown>;
    } catch {
      parsedJson = undefined;
    }
    return { content, parsedJson, model: this.model, provider: this.name };
  }
}

export function resolveProvider(name = "auto", model?: string): ModelProvider {
  const chosen = name === "auto" ? process.env.AFE_PROVIDER ?? "auto" : name;
  if (chosen === "openai" || (chosen === "auto" && process.env.OPENAI_API_KEY)) {
    return new OpenAICompatProvider(model);
  }
  if (chosen === "ollama" || (chosen === "auto" && process.env.OLLAMA_HOST)) {
    return new OllamaProvider(model);
  }
  return new MockProvider(model);
}
