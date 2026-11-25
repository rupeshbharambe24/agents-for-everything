import fs from "node:fs";
import path from "node:path";

export type JsonSchema = Record<string, unknown>;

function resolveRef(ref: string, typesDir?: string): JsonSchema | undefined {
  if (ref.startsWith("afe://types/") && typesDir) {
    let name = ref.slice("afe://types/".length);
    if (!name.endsWith(".schema.json")) name += ".schema.json";
    const target = path.join(typesDir, name);
    if (fs.existsSync(target)) {
      return JSON.parse(fs.readFileSync(target, "utf-8")) as JsonSchema;
    }
  }
  return undefined;
}

function matchesType(value: unknown, expected: string): boolean {
  if (expected === "object") return typeof value === "object" && value !== null && !Array.isArray(value);
  if (expected === "array") return Array.isArray(value);
  if (expected === "string") return typeof value === "string";
  if (expected === "integer") return typeof value === "number" && Number.isInteger(value);
  if (expected === "number") return typeof value === "number";
  if (expected === "boolean") return typeof value === "boolean";
  if (expected === "null") return value === null;
  return true;
}

export function validateJsonSchema(
  instance: unknown,
  schema: JsonSchema,
  typesDir?: string,
  jsonPath = "$"
): string[] {
  const errors: string[] = [];

  if (typeof schema.$ref === "string") {
    const resolved = resolveRef(schema.$ref, typesDir);
    if (resolved) return validateJsonSchema(instance, resolved, typesDir, jsonPath);
    return errors;
  }

  if ("const" in schema && instance !== schema.const) {
    errors.push(`${jsonPath}: expected constant ${JSON.stringify(schema.const)}`);
    return errors;
  }

  if (Array.isArray(schema.enum) && !schema.enum.includes(instance)) {
    errors.push(`${jsonPath}: value ${JSON.stringify(instance)} not in enum`);
    return errors;
  }

  if (typeof schema.type === "string" && !matchesType(instance, schema.type)) {
    errors.push(`${jsonPath}: expected type ${schema.type}`);
    return errors;
  }

  if (typeof instance === "object" && instance !== null && !Array.isArray(instance)) {
    const obj = instance as Record<string, unknown>;
    const required = Array.isArray(schema.required) ? (schema.required as string[]) : [];
    for (const key of required) {
      if (!(key in obj)) errors.push(`${jsonPath}: missing required property '${key}'`);
    }
    const props = (schema.properties as Record<string, JsonSchema> | undefined) ?? {};
    for (const [k, v] of Object.entries(obj)) {
      if (k in props) {
        errors.push(...validateJsonSchema(v, props[k], typesDir, `${jsonPath}.${k}`));
      }
    }
  }

  if (Array.isArray(instance) && typeof schema.items === "object" && schema.items !== null) {
    instance.forEach((item, idx) => {
      errors.push(
        ...validateJsonSchema(item, schema.items as JsonSchema, typesDir, `${jsonPath}[${idx}]`)
      );
    });
  }

  return errors;
}
