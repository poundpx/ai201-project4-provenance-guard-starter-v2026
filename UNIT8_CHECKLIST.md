# Unit 8 — Red-Teaming Provenance Guard: Checklist

Due: **Mon Nov 9, 2:59 AM EST**. Same repo, same URL. At least 4 new commits.

**Rule:** the only changes this unit are the rate limiter, the audit log, and ONE improvement. Don't touch signals, weights, thresholds or labels anywhere else.

## Setup
- [ ] Activate venv (`.venv\Scripts\Activate.ps1`), `python test.py` passes
- [ ] `python app.py` runs; `curl.exe` a POST /submit returns my JSON (not a 501)

## Milestone 1 — Rate limit + complete audit log
- [ ] `config.py`: `RATE_LIMITING_ENABLED = True`
- [ ] `config.py`: choose per-minute and per-day numbers (write down *why*: real writer vs. a threshold-mapping script)
- [ ] `app.py`: uncomment `@limiter.limit(...)` above `submit`
- [ ] `GET /health` says limiting is on
- [ ] `python run_attacks.py --flood 15` shows `200 ... 429`; `results/flood_<date>.md` written
- [ ] Every decision in `logs/audit.jsonl` has all 9 fields: timestamp, content id, creator id, guess, signal-1 score, signal-2 score, combined score, label, status
- [ ] My own route rejections (e.g. 400 missing text) call `audit.log_rejection`
- [ ] Submit 3 texts, read them back via `GET /log`
- [ ] Eyeball one entry: could someone reconstruct the decision without my code?
- [ ] README **Rate Limiting** section: limits, reasoning, pasted status-code run
- [ ] **Commit**

## Milestone 2 — Run the attack set (no fixing yet!)
- [ ] Get `attack_set.zip`, unzip into its own folder in the repo (read header row only)
- [ ] `python run_attacks.py --set <folder>` with the service running
- [ ] Note any crash: which input, what error — skip it and keep going
- [ ] Mark every attack **held** or **broke**; count totals
- [ ] README **Attack Run — Before**: every attack + outcome + held/broke
- [ ] Paste ≥10 audit entries (interesting failures, ≥1 rejection / 429)
- [ ] Pick the single worst outcome
- [ ] Breakout / Claude: get 3 possible causes at different stages, then work out the real one myself
- [ ] **Commit**

## Milestone 3 — My five criteria, three trials
- [ ] Re-read `criteria.md` (from Unit 7 — don't edit the originals)
- [ ] Replace placeholder scenarios in `scenarios.py` with ones for all 5 criteria (own writing for false-positive criterion; spread of scores for label coverage)
- [ ] `python run_eval.py --label before`
- [ ] Check for `status: null` / JSONDecodeError → look for traceback in app.py terminal
- [ ] Run log table: 5 rows, Run 1/2/3, Verdict
- [ ] Under it: real pasted JSON per criterion + file/function that produced it
- [ ] **Commit**

## Milestone 4 — Verdicts + diagnosis
- [ ] MET / MISSED per criterion (target must hold in **every** trial)
- [ ] One sentence per criterion on how I decided
- [ ] For each miss and each broken attack: **stage** (route / signal 1 / signal 2 / combining rule / label mapping) + **mechanism**
- [ ] Look for patterns across failures (same signal = one problem)
- [ ] If I held everything: were targets too easy? Name one to tighten
- [ ] Any revised criterion: keep original, add new line + reason (only if it was unmeasurable)
- [ ] Ask Claude/breakout to argue the opposite verdict
- [ ] README **Run Log and Verdicts**
- [ ] **Commit**

## Milestone 5 — One improvement, measured
- [ ] Pick ONE change the diagnosis points to (reweight / move threshold / validate input / other)
- [ ] Make only that change
- [ ] `python run_attacks.py --set <folder> --label after`
- [ ] `python run_eval.py --label after`
- [ ] README **The Improvement**: what, why, before vs. after side by side, Attack Run — After
- [ ] One sentence: did it help? Name what it cost
- [ ] **Commit**

## Milestone 6 — What's still broken + submit
- [ ] README **What's Still Broken**: each remaining failure → what I'd do, why I stopped
- [ ] Two sentences on the production trade (fewer false accusations vs. more AI getting through — who pays)
- [ ] Update **How I Used AI** with this unit
- [ ] Commit `logs/audit.jsonl`, `results/` (flood, both attack runs, both eval runs), `scenarios.py`
- [ ] Verify ≥4 new commits, push, submit same repo URL
- [ ] **Commit + push**

## Stretch (declare in README before starting)
- [ ] 3 attacks against someone else's system
- [ ] A second measured improvement
- [ ] Per-creator rate limits instead of per-address
