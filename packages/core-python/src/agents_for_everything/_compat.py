"""Compatibility helpers: YAML parsing and JSON Schema 2020-12 validation.

Uses PyYAML / jsonschema when installed, and falls back to clean stdlib
implementations so core-python runs with zero external dependencies.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

try:
    import yaml as _pyyaml  # type: ignore
except ImportError:  # pragma: no cover
    _pyyaml = None

try:
    import jsonschema as _jsonschema  # type: ignore
except ImportError:  # pragma: no cover
    _jsonschema = None


class YAMLParseError(ValueError):
    """Raised when YAML parsing fails."""


class SchemaValidationError(ValueError):
    """Raised when JSON Schema validation fails."""


def _strip_comment(line: str) -> str:
    in_single = False
    in_double = False
    escaped = False
    for idx, ch in enumerate(line):
        if escaped:
            escaped = False
            continue
        if ch == "\\" and in_double:
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            if idx == 0 or line[idx - 1].isspace():
                return line[:idx].rstrip()
    return line.rstrip()


def _split_top_level(text: str, sep: str = ",") -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    in_single = False
    in_double = False
    escaped = False
    for ch in text:
        if escaped:
            buf.append(ch)
            escaped = False
            continue
        if ch == "\\" and in_double:
            buf.append(ch)
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif not in_single and not in_double:
            if ch in "{[":
                depth += 1
            elif ch in "}]":
                depth -= 1
            elif ch == sep and depth == 0:
                part = "".join(buf).strip()
                if part:
                    parts.append(part)
                buf = []
                continue
        buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)
    return parts


def _parse_scalar(raw: str) -> Any:
    val = raw.strip()
    if val == "" or val in {"null", "Null", "NULL", "~"}:
        return None
    if val in {"true", "True", "TRUE"}:
        return True
    if val in {"false", "False", "FALSE"}:
        return False
    if val.startswith('"') and val.endswith('"') and len(val) >= 2:
        try:
            return json.loads(val)
        except json.JSONDecodeError:
            return val[1:-1]
    if val.startswith("'") and val.endswith("'") and len(val) >= 2:
        return val[1:-1].replace("''", "'")
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item) for item in _split_top_level(inner)]
    if val.startswith("{") and val.endswith("}"):
        inner = val[1:-1].strip()
        if not inner:
            return {}
        out: dict[str, Any] = {}
        for item in _split_top_level(inner):
            if ":" not in item:
                raise YAMLParseError(f"Invalid inline mapping entry: {item}")
            k, v = item.split(":", 1)
            out[str(_parse_scalar(k.strip()))] = _parse_scalar(v.strip())
        return out
    if re.fullmatch(r"-?[0-9]+", val):
        return int(val)
    if re.fullmatch(r"-?[0-9]+\.[0-9]+", val):
        return float(val)
    return val


def _find_mapping_colon(text: str) -> int:
    in_single = False
    in_double = False
    escaped = False
    for idx, ch in enumerate(text):
        if escaped:
            escaped = False
            continue
        if ch == "\\" and in_double:
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == ":" and not in_single and not in_double:
            if idx + 1 == len(text) or text[idx + 1].isspace():
                return idx
    return -1


def _parse_yaml_lite(text: str) -> Any:
    raw_lines = text.splitlines()
    tokens: list[tuple[int, str]] = []
    idx = 0
    while idx < len(raw_lines):
        raw = raw_lines[idx]
        if raw.strip() in {"---", "..."}:
            idx += 1
            continue
        cleaned = _strip_comment(raw)
        if not cleaned.strip():
            idx += 1
            continue
        indent = len(cleaned) - len(cleaned.lstrip(" "))
        tokens.append((indent, cleaned.lstrip(" ")))
        idx += 1

    if not tokens:
        return {}

    def parse_block_scalar(start_i: int, parent_indent: int, style: str) -> tuple[str, int]:
        # Re-scan raw_lines preserving literal newlines after block header.
        lines: list[str] = []
        base_indent: int | None = None
        i = start_i
        while i < len(tokens):
            ind, content = tokens[i]
            if ind <= parent_indent:
                break
            if base_indent is None:
                base_indent = ind
            pad = " " * max(0, ind - base_indent)
            lines.append(f"{pad}{content}")
            i += 1
        if style == ">":
            return " ".join(part.strip() for part in lines), i
        return "\n".join(lines), i

    def parse_node(pos: int, min_indent: int) -> tuple[Any, int]:
        indent, content = tokens[pos]
        if content.startswith("- ") or content == "-":
            return parse_seq(pos, indent)
        return parse_map(pos, indent)

    def parse_seq(pos: int, seq_indent: int) -> tuple[list[Any], int]:
        items: list[Any] = []
        while pos < len(tokens):
            indent, content = tokens[pos]
            if indent < seq_indent:
                break
            if indent > seq_indent or not (content.startswith("- ") or content == "-"):
                break
            rest = content[1:].strip()
            if not rest:
                if pos + 1 < len(tokens) and tokens[pos + 1][0] > indent:
                    val, pos = parse_node(pos + 1, indent + 1)
                    items.append(val)
                else:
                    items.append(None)
                    pos += 1
                continue

            colon_idx = _find_mapping_colon(rest)
            if colon_idx != -1 and not rest.startswith("{") and not rest.startswith("["):
                # Sequence item starts a mapping on the same line: "- key: val"
                first_key = str(_parse_scalar(rest[:colon_idx].strip()))
                first_val_raw = rest[colon_idx + 1 :].strip()
                item_indent = indent + 2
                item_map: dict[str, Any] = {}
                if first_val_raw in {">", "|", ">-", "|-"}:
                    val, pos = parse_block_scalar(pos + 1, item_indent, first_val_raw[0])
                    item_map[first_key] = val
                elif first_val_raw == "":
                    if pos + 1 < len(tokens) and tokens[pos + 1][0] > item_indent:
                        val, pos = parse_node(pos + 1, item_indent + 1)
                    else:
                        val = None
                        pos += 1
                    item_map[first_key] = val
                else:
                    item_map[first_key] = _parse_scalar(first_val_raw)
                    pos += 1
                # Parse remaining sibling keys indented >= item_indent
                if pos < len(tokens) and tokens[pos][0] >= item_indent:
                    if not (tokens[pos][1].startswith("- ") or tokens[pos][1] == "-"):
                        more, pos = parse_map(pos, tokens[pos][0])
                        item_map.update(more)
                items.append(item_map)
            else:
                items.append(_parse_scalar(rest))
                pos += 1
        return items, pos

    def parse_map(pos: int, map_indent: int) -> tuple[dict[str, Any], int]:
        mapping: dict[str, Any] = {}
        while pos < len(tokens):
            indent, content = tokens[pos]
            if indent < map_indent or indent > map_indent:
                break
            if content.startswith("- ") or content == "-":
                break
            colon_idx = _find_mapping_colon(content)
            if colon_idx == -1:
                raise YAMLParseError(f"Expected 'key: value' near: {content}")
            key = str(_parse_scalar(content[:colon_idx].strip()))
            val_raw = content[colon_idx + 1 :].strip()
            if val_raw in {">", "|", ">-", "|-"}:
                val, pos = parse_block_scalar(pos + 1, indent, val_raw[0])
                mapping[key] = val
            elif val_raw == "":
                if pos + 1 < len(tokens) and tokens[pos + 1][0] > indent:
                    val, pos = parse_node(pos + 1, indent + 1)
                elif pos + 1 < len(tokens) and tokens[pos + 1][0] == indent and (
                    tokens[pos + 1][1].startswith("- ") or tokens[pos + 1][1] == "-"
                ):
                    val, pos = parse_seq(pos + 1, indent)
                else:
                    val = None
                    pos += 1
                mapping[key] = val
            else:
                mapping[key] = _parse_scalar(val_raw)
                pos += 1
        return mapping, pos

    parsed, _ = parse_node(0, tokens[0][0])
    return parsed


def load_yaml(text: str) -> Any:
    """Parse YAML text into Python objects."""
    if _pyyaml is not None:
        return _pyyaml.safe_load(text)
    return _parse_yaml_lite(text)


def load_yaml_file(path: Path) -> Any:
    """Read and parse a YAML file."""
    return load_yaml(path.read_text(encoding="utf-8"))


def _resolve_ref(ref: str, types_dir: Path | None, root_schema: dict[str, Any]) -> dict[str, Any]:
    if ref.startswith("afe://types/") and types_dir is not None:
        name = ref.removeprefix("afe://types/")
        if not name.endswith(".schema.json"):
            name = f"{name}.schema.json"
        target = types_dir / name
        if target.exists():
            return json.loads(target.read_text(encoding="utf-8"))
    if ref.startswith("#/$defs/"):
        key = ref.removeprefix("#/$defs/")
        defs = root_schema.get("$defs", {})
        if key in defs:
            return defs[key]
    return {}


def _type_matches(value: Any, expected: str | list[str]) -> bool:
    if isinstance(expected, list):
        return any(_type_matches(value, t) for t in expected)
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return True


def _validate_lite(
    instance: Any,
    schema: dict[str, Any],
    types_dir: Path | None,
    root_schema: dict[str, Any],
    path: str,
    errors: list[str],
) -> None:
    if "$ref" in schema:
        resolved = _resolve_ref(schema["$ref"], types_dir, root_schema)
        if resolved:
            _validate_lite(instance, resolved, types_dir, resolved, path, errors)
        return

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}, got {instance!r}")
        return

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in allowed enum {schema['enum']}")
        return

    if "type" in schema and not _type_matches(instance, schema["type"]):
        errors.append(f"{path}: expected type {schema['type']}, got {type(instance).__name__}")
        return

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: length {len(instance)} < minLength {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: length {len(instance)} > maxLength {schema['maxLength']}")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            errors.append(f"{path}: {instance!r} does not match pattern {schema['pattern']!r}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} > maximum {schema['maximum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: item count {len(instance)} < minItems {schema['minItems']}")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(instance):
                _validate_lite(item, item_schema, types_dir, root_schema, f"{path}[{idx}]", errors)

    if isinstance(instance, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: missing required property {req!r}")
        add_props = schema.get("additionalProperties", True)
        for key, val in instance.items():
            if key in props:
                _validate_lite(val, props[key], types_dir, root_schema, f"{path}.{key}", errors)
            elif add_props is False:
                errors.append(f"{path}: unexpected property {key!r}")
            elif isinstance(add_props, dict):
                _validate_lite(val, add_props, types_dir, root_schema, f"{path}.{key}", errors)


def validate_json_schema(
    instance: Any,
    schema: dict[str, Any],
    types_dir: Path | None = None,
) -> list[str]:
    """Validate an instance against a JSON Schema, returning error messages."""
    if _jsonschema is not None and types_dir is None:
        validator = _jsonschema.Draft202012Validator(schema)
        return [err.message for err in validator.iter_errors(instance)]

    errors: list[str] = []
    _validate_lite(instance, schema, types_dir, schema, "$", errors)
    return errors
