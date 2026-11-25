/** Lightweight YAML parser for afe/v1 manifests (zero dependencies). */

function stripComment(line: string): string {
  let inSingle = false;
  let inDouble = false;
  let escaped = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (ch === "\\" && inDouble) {
      escaped = true;
      continue;
    }
    if (ch === "'" && !inDouble) inSingle = !inSingle;
    else if (ch === '"' && !inSingle) inDouble = !inDouble;
    else if (ch === "#" && !inSingle && !inDouble) {
      if (i === 0 || /\s/.test(line[i - 1])) return line.slice(0, i).trimEnd();
    }
  }
  return line.trimEnd();
}

function splitTopLevel(text: string): string[] {
  const parts: string[] = [];
  let buf = "";
  let depth = 0;
  let inSingle = false;
  let inDouble = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "'" && !inDouble) inSingle = !inSingle;
    else if (ch === '"' && !inSingle) inDouble = !inDouble;
    else if (!inSingle && !inDouble) {
      if (ch === "[" || ch === "{") depth++;
      else if (ch === "]" || ch === "}") depth--;
      else if (ch === "," && depth === 0) {
        if (buf.trim()) parts.push(buf.trim());
        buf = "";
        continue;
      }
    }
    buf += ch;
  }
  if (buf.trim()) parts.push(buf.trim());
  return parts;
}

function parseScalar(raw: string): unknown {
  const val = raw.trim();
  if (val === "" || val === "null" || val === "~") return null;
  if (val === "true") return true;
  if (val === "false") return false;
  if (val.startsWith('"') && val.endsWith('"') && val.length >= 2) {
    try {
      return JSON.parse(val);
    } catch {
      return val.slice(1, -1);
    }
  }
  if (val.startsWith("'") && val.endsWith("'") && val.length >= 2) {
    return val.slice(1, -1).replaceAll("''", "'");
  }
  if (val.startsWith("[") && val.endsWith("]")) {
    const inner = val.slice(1, -1).trim();
    return inner ? splitTopLevel(inner).map(parseScalar) : [];
  }
  if (val.startsWith("{") && val.endsWith("}")) {
    const inner = val.slice(1, -1).trim();
    if (!inner) return {};
    const out: Record<string, unknown> = {};
    for (const item of splitTopLevel(inner)) {
      const idx = item.indexOf(":");
      if (idx === -1) throw new Error(`Invalid inline mapping: ${item}`);
      out[String(parseScalar(item.slice(0, idx)))] = parseScalar(item.slice(idx + 1));
    }
    return out;
  }
  if (/^-?\d+$/.test(val)) return Number.parseInt(val, 10);
  if (/^-?\d+\.\d+$/.test(val)) return Number.parseFloat(val);
  return val;
}

function findColon(text: string): number {
  let inSingle = false;
  let inDouble = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "'" && !inDouble) inSingle = !inSingle;
    else if (ch === '"' && !inSingle) inDouble = !inDouble;
    else if (ch === ":" && !inSingle && !inDouble) {
      if (i + 1 === text.length || /\s/.test(text[i + 1])) return i;
    }
  }
  return -1;
}

export function parseYaml(text: string): Record<string, unknown> {
  const tokens: Array<{ indent: number; content: string }> = [];
  for (const raw of text.split(/\r?\n/)) {
    const trimmed = raw.trim();
    if (trimmed === "---" || trimmed === "...") continue;
    const cleaned = stripComment(raw);
    if (!cleaned.trim()) continue;
    const indent = cleaned.length - cleaned.trimStart().length;
    tokens.push({ indent, content: cleaned.trimStart() });
  }
  if (tokens.length === 0) return {};

  function parseBlock(pos: number, parentIndent: number, style: string): [string, number] {
    const lines: string[] = [];
    let i = pos;
    while (i < tokens.length && tokens[i].indent > parentIndent) {
      lines.push(tokens[i].content);
      i++;
    }
    return [style === ">" ? lines.join(" ") : lines.join("\n"), i];
  }

  function parseSeq(pos: number, seqIndent: number): [unknown[], number] {
    const items: unknown[] = [];
    let i = pos;
    while (i < tokens.length && tokens[i].indent === seqIndent) {
      const content = tokens[i].content;
      if (!content.startsWith("- ") && content !== "-") break;
      const rest = content.slice(1).trim();
      if (!rest) {
        if (i + 1 < tokens.length && tokens[i + 1].indent > seqIndent) {
          const [child, next] = parseNode(i + 1);
          items.push(child);
          i = next;
        } else {
          items.push(null);
          i++;
        }
        continue;
      }
      const colonIdx = findColon(rest);
      if (colonIdx !== -1 && !rest.startsWith("{") && !rest.startsWith("[")) {
        const key = String(parseScalar(rest.slice(0, colonIdx)));
        const valRaw = rest.slice(colonIdx + 1).trim();
        const itemMap: Record<string, unknown> = {};
        const itemIndent = seqIndent + 2;
        if (valRaw === ">" || valRaw === "|") {
          const [v, next] = parseBlock(i + 1, itemIndent, valRaw);
          itemMap[key] = v;
          i = next;
        } else if (valRaw === "") {
          const [v, next] =
            i + 1 < tokens.length && tokens[i + 1].indent > itemIndent
              ? parseNode(i + 1)
              : [null, i + 1];
          itemMap[key] = v;
          i = next;
        } else {
          itemMap[key] = parseScalar(valRaw);
          i++;
        }
        if (
          i < tokens.length &&
          tokens[i].indent >= itemIndent &&
          !tokens[i].content.startsWith("- ")
        ) {
          const [more, next] = parseMap(i, tokens[i].indent);
          Object.assign(itemMap, more);
          i = next;
        }
        items.push(itemMap);
      } else {
        items.push(parseScalar(rest));
        i++;
      }
    }
    return [items, i];
  }

  function parseMap(pos: number, mapIndent: number): [Record<string, unknown>, number] {
    const out: Record<string, unknown> = {};
    let i = pos;
    while (i < tokens.length && tokens[i].indent === mapIndent) {
      const content = tokens[i].content;
      if (content.startsWith("- ") || content === "-") break;
      const colonIdx = findColon(content);
      if (colonIdx === -1) throw new Error(`Expected key: value near '${content}'`);
      const key = String(parseScalar(content.slice(0, colonIdx)));
      const valRaw = content.slice(colonIdx + 1).trim();
      if (valRaw === ">" || valRaw === "|" || valRaw === ">-" || valRaw === "|-") {
        const [v, next] = parseBlock(i + 1, mapIndent, valRaw[0]);
        out[key] = v;
        i = next;
      } else if (valRaw === "") {
        if (i + 1 < tokens.length && tokens[i + 1].indent > mapIndent) {
          const [v, next] = parseNode(i + 1);
          out[key] = v;
          i = next;
        } else if (
          i + 1 < tokens.length &&
          tokens[i + 1].indent === mapIndent &&
          (tokens[i + 1].content.startsWith("- ") || tokens[i + 1].content === "-")
        ) {
          const [v, next] = parseSeq(i + 1, mapIndent);
          out[key] = v;
          i = next;
        } else {
          out[key] = null;
          i++;
        }
      } else {
        out[key] = parseScalar(valRaw);
        i++;
      }
    }
    return [out, i];
  }

  function parseNode(pos: number): [unknown, number] {
    const tok = tokens[pos];
    if (tok.content.startsWith("- ") || tok.content === "-") {
      return parseSeq(pos, tok.indent);
    }
    return parseMap(pos, tok.indent);
  }

  const [parsed] = parseNode(0);
  return (parsed as Record<string, unknown>) ?? {};
}
