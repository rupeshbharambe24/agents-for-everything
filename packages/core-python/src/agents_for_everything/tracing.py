"""OpenTelemetry GenAI semantic-convention tracing collector."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Any

from .safety import redact_pii


@dataclass(slots=True)
class TraceSpan:
    """Single trace span recorded during an agent or tool step."""

    trace_id: str
    span_id: str
    name: str
    start_time_ns: int
    end_time_ns: int = 0
    attributes: dict[str, Any] = field(default_factory=dict)
    status: str = "OK"

    def to_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "span_id": self.span_id,
            "name": self.name,
            "start_time_ns": self.start_time_ns,
            "end_time_ns": self.end_time_ns,
            "attributes": self.attributes,
            "status": self.status,
        }


class TraceCollector:
    """In-memory collector emitting OpenTelemetry GenAI semantic attributes."""

    def __init__(self, trace_id: str | None = None, mask_pii: bool = True) -> None:
        self.trace_id = trace_id or uuid.uuid4().hex
        self.mask_pii = mask_pii
        self.spans: list[TraceSpan] = []

    def start_span(self, name: str, attributes: dict[str, Any] | None = None) -> TraceSpan:
        clean_attrs: dict[str, Any] = {}
        for k, v in (attributes or {}).items():
            clean_attrs[k] = redact_pii(v) if (self.mask_pii and isinstance(v, str)) else v
        span = TraceSpan(
            trace_id=self.trace_id,
            span_id=uuid.uuid4().hex[:16],
            name=name,
            start_time_ns=time.time_ns(),
            attributes=clean_attrs,
        )
        self.spans.append(span)
        return span

    def finish_span(self, span: TraceSpan, status: str = "OK", extra: dict[str, Any] | None = None) -> None:
        span.end_time_ns = time.time_ns()
        span.status = status
        if extra:
            for k, v in extra.items():
                span.attributes[k] = redact_pii(v) if (self.mask_pii and isinstance(v, str)) else v

    def export(self) -> list[dict[str, Any]]:
        return [span.to_dict() for span in self.spans]
