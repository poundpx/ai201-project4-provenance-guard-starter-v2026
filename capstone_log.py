"""
Capstone instrumentation: one structured record per HTTP request.

Written to logs/requests.jsonl (separate from the audit log, which records
decisions, not requests). Fields:

    timestamp     UTC ISO time the request finished
    route         e.g. /submit
    method        GET / POST
    input         {"creator_id", "text_preview" (first 80 chars), "word_count"} or the raw keys sent
    status        HTTP status code returned
    output        first 300 chars of the response body
    duration_ms   wall-clock time inside the service, end to end
    model_ms      /submit only: time in detector.model_signal (GPT-2)
    style_ms      /submit only: time in stylometry.style_signal
    error         set only when the request crashed (500)
"""

import json
import threading
import time
from datetime import datetime, timezone

import config

REQUEST_LOG = config.LOG_DIR / "requests.jsonl"
_lock = threading.Lock()


def _summarize_input(req):
    payload = req.get_json(silent=True)
    if isinstance(payload, dict):
        text = payload.get("text")
        out = {"creator_id": payload.get("creator_id")}
        if isinstance(text, str):
            out["text_preview"] = text[:80]
            out["word_count"] = len(text.split())
        elif text is not None:
            out["text_type"] = type(text).__name__
        for k in ("content_id", "message"):
            if k in payload:
                out[k] = str(payload[k])[:80]
        return out
    if payload is None and req.data:
        return {"raw_body_preview": req.data[:80].decode(errors="replace")}
    return {"body_type": type(payload).__name__ if payload is not None else None}


def log_request(req, status, body, t0, timings, error=None):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "route": req.path,
        "method": req.method,
        "input": _summarize_input(req),
        "status": status,
        "output": (body or "")[:300],
        "duration_ms": round((time.perf_counter() - t0) * 1000, 1),
        **(timings or {}),
    }
    if error:
        entry["error"] = error
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with _lock, REQUEST_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass  # logging must never take the service down
    return entry
