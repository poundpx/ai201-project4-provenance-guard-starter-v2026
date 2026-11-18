#!/usr/bin/env python3
"""
Capstone probe: drive the running service, then measure it from its own log.

    python app.py                                   # terminal 1
    python capstone_probe.py --label before --trials 3   # terminal 2

Each trial sends 20 requests: 10 normal /submit, 7 bad inputs, 1 appeal to an
unknown id, 1 /health, 1 forced client timeout. Every creator_id is unique so
the rate limiter (5/min per creator) doesn't count the probe against itself.

Afterwards it reads logs/requests.jsonl for the trial window and prints:
  - status codes per scenario
  - duration_ms p50 / p90 / max for /submit, and model_ms / style_ms
  - how many requests sent vs how many records landed in the log
  - seconds of compute per /submit (the cost number)
Results also go to results/capstone_<label>.md.
"""
import argparse
import json
import statistics
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "http://127.0.0.1:5000"
ROOT = Path(__file__).resolve().parent
REQ_LOG = ROOT / "logs" / "requests.jsonl"

NORMAL_TEXTS = [
    "honestly i didnt think the bus would be that late again, third time this week and nobody said anything",
    "The committee reviewed the proposal and concluded that further analysis is required before a decision can be made on funding.",
    "My grandmother used to make dumplings every new year. The kitchen smelled like ginger for days and we fought over the last ones.",
    "Artificial intelligence is transforming industries by automating tasks, improving efficiency, and enabling new insights from data.",
    "i tried the new ramen place downtown. broth was good but way too salty, probably wont go back unless someone else pays lol",
    "In conclusion, effective time management is essential for academic success, as it allows students to balance their responsibilities.",
    "We missed the last train so we walked home across the bridge at 2am. Cold, tired, and somehow it was the best part of the trip.",
    "Climate change poses significant challenges to global food security, requiring coordinated international efforts and innovative solutions.",
    "my cat knocked my coffee onto the keyboard during a zoom call and now the letter e only works if i press it really hard",
    "Hello, I am a student from Vietnam. I study computer science and I like to play games with my friends on the weekend.",
]


def send(method, path, *, json_body=None, data=None, timeout=60):
    rec = {"path": path, "status": None, "client_ms": None, "error": None}
    t0 = time.perf_counter()
    try:
        r = requests.request(method, BASE + path, json=json_body, data=data, timeout=timeout,
                             headers={"Content-Type": "application/json"} if data is not None else None)
        rec["status"] = r.status_code
        rec["body"] = r.text[:200]
    except requests.exceptions.Timeout:
        rec["error"] = "client_timeout"
    except requests.exceptions.RequestException as e:
        rec["error"] = type(e).__name__
    rec["client_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    return rec


def cid():
    return "probe_" + uuid.uuid4().hex[:8]


def run_trial():
    sent = []  # (scenario, record)
    for t in NORMAL_TEXTS:
        sent.append(("submit_normal", send("POST", "/submit", json_body={"text": t, "creator_id": cid()})))
    bad = [
        ("bad_missing_text", dict(json_body={"creator_id": cid()})),
        ("bad_empty_text", dict(json_body={"text": "   ", "creator_id": cid()})),
        ("bad_non_string", dict(json_body={"text": 12345, "creator_id": cid()})),
        ("bad_invalid_json", dict(data="{not json")),
        ("bad_json_list", dict(json_body=["a", "list"])),
        ("bad_too_short", dict(json_body={"text": "sleep", "creator_id": cid()})),
        ("bad_huge_text", dict(json_body={"text": "word " * 6000, "creator_id": cid()})),
    ]
    for name, kw in bad:
        sent.append((name, send("POST", "/submit", **kw)))
    sent.append(("appeal_unknown_id", send("POST", "/appeal",
                 json_body={"content_id": "does-not-exist", "reasoning": "I wrote this"})))
    sent.append(("health", send("GET", "/health")))
    # Forced failure on the client side: the server still does the work and should still log it
    sent.append(("forced_client_timeout", send("POST", "/submit", timeout=0.01,
                 json_body={"text": NORMAL_TEXTS[0], "creator_id": cid()})))
    return sent


def read_log_since(start_iso):
    if not REQ_LOG.exists():
        return []
    out = []
    for line in REQ_LOG.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("timestamp", "") >= start_iso:
            out.append(e)
    return out


def pct(vals, p):
    if not vals:
        return None
    v = sorted(vals)
    return v[min(len(v) - 1, round(p / 100 * (len(v) - 1)))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="before")
    ap.add_argument("--trials", type=int, default=3)
    a = ap.parse_args()

    try:
        requests.get(BASE + "/health", timeout=5)
    except requests.exceptions.RequestException:
        raise SystemExit("Service isn't answering on 127.0.0.1:5000. Start it with: python app.py")

    lines = [f"# Capstone probe — {a.label}", "",
             f"Run at {datetime.now(timezone.utc).isoformat(timespec='seconds')}", ""]
    for trial in range(1, a.trials + 1):
        start = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        sent = run_trial()
        time.sleep(1.5)  # let the timed-out request finish server-side and log
        logged = read_log_since(start)

        sub = [e for e in logged if e["route"] == "/submit" and e["status"] == 200]
        dur = [e["duration_ms"] for e in sub]
        model = [e["model_ms"] for e in sub if "model_ms" in e]
        style = [e["style_ms"] for e in sub if "style_ms" in e]
        n5xx = sum(1 for e in logged if e["status"] >= 500)
        crashes = [e for e in logged if e.get("error")]

        lines += [f"## Trial {trial}", "", "| scenario | status | client_ms |", "|---|---|---|"]
        for name, r in sent:
            lines.append(f"| {name} | {r['status'] if r['status'] else r['error']} | {r['client_ms']} |")
        lines += [
            "",
            f"- Requests sent: **{len(sent)}**, records in logs/requests.jsonl for this window: **{len(logged)}**",
            f"- 5xx responses in log: **{n5xx}** (crash records with error field: {len(crashes)})",
            f"- /submit 200s: {len(sub)} — duration_ms p50 **{round(statistics.median(dur), 1) if dur else None}**, "
            f"p90 **{pct(dur, 90)}**, max **{max(dur) if dur else None}**",
            f"- model_ms p50 {round(statistics.median(model), 1) if model else None}, "
            f"style_ms p50 {round(statistics.median(style), 1) if style else None}",
            f"- **Compute per /submit (cost): {round(statistics.mean(dur) / 1000, 3) if dur else None} s** (mean)",
            "",
        ]
        print("\n".join(lines[-(len(sent) + 10):]))
        time.sleep(2)

    out = ROOT / "results" / f"capstone_{a.label}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nSaved {out}")


if __name__ == "__main__":
    main()
