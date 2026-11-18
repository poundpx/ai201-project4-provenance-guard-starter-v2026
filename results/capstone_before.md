# Capstone probe — before

Run at 2026-11-18T22:27:15+00:00

## Trial 1

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 93.7 |
| submit_normal | 200 | 140.5 |
| submit_normal | 200 | 107.7 |
| submit_normal | 200 | 73.4 |
| submit_normal | 200 | 76.9 |
| submit_normal | 200 | 70.0 |
| submit_normal | 200 | 87.3 |
| submit_normal | 200 | 68.4 |
| submit_normal | 200 | 75.2 |
| submit_normal | 200 | 89.5 |
| bad_missing_text | 400 | 16.1 |
| bad_empty_text | 400 | 51.0 |
| bad_non_string | 400 | 15.3 |
| bad_invalid_json | 400 | 14.4 |
| bad_json_list | 400 | 31.5 |
| bad_too_short | 400 | 14.1 |
| bad_huge_text | 200 | 346.3 |
| appeal_unknown_id | 404 | 24.2 |
| health | 200 | 7.5 |
| forced_client_timeout | client_timeout | 16.8 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **68.3**, p90 **108.9**, max **323.4**
- model_ms p50 56.6, style_ms p50 0.1
- **Compute per /submit (cost): 0.094 s** (mean)

## Trial 2

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 83.6 |
| submit_normal | 200 | 69.9 |
| submit_normal | 200 | 95.8 |
| submit_normal | 200 | 99.5 |
| submit_normal | 200 | 97.1 |
| submit_normal | 200 | 82.5 |
| submit_normal | 200 | 79.8 |
| submit_normal | 200 | 68.8 |
| submit_normal | 200 | 74.5 |
| submit_normal | 200 | 73.1 |
| bad_missing_text | 400 | 18.4 |
| bad_empty_text | 400 | 15.6 |
| bad_non_string | 400 | 15.3 |
| bad_invalid_json | 400 | 39.0 |
| bad_json_list | 400 | 16.8 |
| bad_too_short | 400 | 15.2 |
| bad_huge_text | 200 | 349.8 |
| appeal_unknown_id | 404 | 17.0 |
| health | 200 | 30.9 |
| forced_client_timeout | client_timeout | 40.0 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **67.0**, p90 **89.9**, max **330.7**
- model_ms p50 55.0, style_ms p50 0.1
- **Compute per /submit (cost): 0.09 s** (mean)

## Trial 3

| scenario | status | client_ms |
|---|---|---|
| submit_normal | 200 | 65.3 |
| submit_normal | 200 | 73.2 |
| submit_normal | 200 | 87.5 |
| submit_normal | 200 | 71.9 |
| submit_normal | 200 | 75.5 |
| submit_normal | 200 | 68.7 |
| submit_normal | 200 | 79.6 |
| submit_normal | 200 | 71.4 |
| submit_normal | 200 | 77.2 |
| submit_normal | 200 | 74.9 |
| bad_missing_text | 400 | 17.6 |
| bad_empty_text | 400 | 17.0 |
| bad_non_string | 400 | 15.3 |
| bad_invalid_json | 400 | 16.3 |
| bad_json_list | 429 | 17.4 |
| bad_too_short | 400 | 15.3 |
| bad_huge_text | 200 | 384.8 |
| appeal_unknown_id | 404 | 7.9 |
| health | 200 | 8.2 |
| forced_client_timeout | client_timeout | 37.9 |

- Requests sent: **20**, records in logs/requests.jsonl for this window: **20**
- 5xx responses in log: **0** (crash records with error field: 0)
- /submit 200s: 12 — duration_ms p50 **66.5**, p90 **81.0**, max **378.9**
- model_ms p50 54.0, style_ms p50 0.1
- **Compute per /submit (cost): 0.092 s** (mean)
