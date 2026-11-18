# Capstone probe — after

Run at 2026-11-18T22:38:32+00:00

## Trial 1

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 3667.9 |
| submit_normal | 200 | 84.7 |
| submit_normal | 200 | 79.8 |
| submit_normal | 200 | 71.9 |
| submit_normal | 200 | 70.7 |
| submit_normal | 200 | 71.1 |
| submit_normal | 200 | 110.0 |
| submit_normal | 200 | 70.5 |
| submit_normal | 200 | 72.0 |
| submit_normal | 200 | 76.2 |
| bad_missing_text | 400 | 16.7 |
| bad_empty_text | 400 | 16.3 |
| bad_non_string | 400 | 39.5 |
| bad_invalid_json | 400 | 16.7 |
| bad_json_list | 400 | 14.9 |
| bad_too_short | 400 | 25.7 |
| bad_huge_text | 200 | 335.1 |
| appeal_unknown_id | 404 | 10.4 |
| health | 200 | 8.5 |
| forced_client_timeout | client_timeout | 27.4 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **65.3**, p90 **310.6**, max **3643.0**
- model_ms p50 54.0, style_ms p50 0.1
- **Compute per /submit (cost): 0.387 s** (mean)

## Trial 2

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 73.8 |
| submit_normal | 200 | 80.7 |
| submit_normal | 200 | 82.3 |
| submit_normal | 200 | 70.4 |
| submit_normal | 200 | 77.4 |
| submit_normal | 200 | 75.0 |
| submit_normal | 200 | 91.9 |
| submit_normal | 200 | 104.2 |
| submit_normal | 200 | 80.5 |
| submit_normal | 200 | 72.5 |
| bad_missing_text | 400 | 17.5 |
| bad_empty_text | 400 | 14.6 |
| bad_non_string | 400 | 26.0 |
| bad_invalid_json | 400 | 16.5 |
| bad_json_list | 400 | 29.0 |
| bad_too_short | 400 | 29.1 |
| bad_huge_text | 200 | 348.1 |
| appeal_unknown_id | 404 | 8.9 |
| health | 200 | 31.8 |
| forced_client_timeout | client_timeout | 39.7 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **70.5**, p90 **83.2**, max **341.8**
- model_ms p50 54.2, style_ms p50 0.1
- **Compute per /submit (cost): 0.092 s** (mean)

## Trial 3

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 86.7 |
| submit_normal | 200 | 83.4 |
| submit_normal | 200 | 101.9 |
| submit_normal | 200 | 80.2 |
| submit_normal | 200 | 92.2 |
| submit_normal | 200 | 69.7 |
| submit_normal | 200 | 75.8 |
| submit_normal | 200 | 69.7 |
| submit_normal | 200 | 73.6 |
| submit_normal | 200 | 74.4 |
| bad_missing_text | 400 | 18.3 |
| bad_empty_text | 400 | 18.3 |
| bad_non_string | 400 | 16.8 |
| bad_invalid_json | 400 | 15.9 |
| bad_json_list | 400 | 15.6 |
| bad_too_short | 400 | 16.7 |
| bad_huge_text | 200 | 360.1 |
| appeal_unknown_id | 404 | 8.9 |
| health | 200 | 8.2 |
| forced_client_timeout | client_timeout | 16.7 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **66.6**, p90 **72.7**, max **353.7**
- model_ms p50 54.5, style_ms p50 0.1
- **Compute per /submit (cost): 0.09 s** (mean)
