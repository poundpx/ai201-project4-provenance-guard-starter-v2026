# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 03:43
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `cdee85e5-ce08-4409-bd77-1475797320fc` | human | 0.346 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f75a81b1-3b50-4879-af6c-364ae8e510cb` | unsure | 0.502 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `27590a87-75ac-4196-9b11-fb72644b1453` | unsure | 0.562 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f6a9d6fd-8c50-4440-9313-a8746332c9b7` | unsure | 0.657 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f81fa643-b584-4f40-9627-20abb3fa62cc` | human | 0.340 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4fb4da0c-6983-4af5-bf86-e92a2ea7b914` | unsure | 0.532 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bd8f6846-7f04-4b5c-b4db-e0af12f7d258` | unsure | 0.528 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f553f8f5-ddd2-4f57-8eeb-e5d8cdeee2e9` | unsure | 0.371 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b18590c1-413c-43b6-8cac-f690aeb89fd5` | unsure | 0.607 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7c40fe49-7928-49e9-99bc-e56c9a9f3b41` | ai | 0.887 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ad1868b5-6fb3-4fb4-afac-cdd8cee0654b` | unsure | 0.602 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `45fb82d6-e8d7-4695-bc2c-acc43cf70efe` | unsure | 0.741 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `7ba5608b-1635-4653-a035-049cbe78a486` | unsure | 0.765 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `892ddc74-9a82-47ef-8495-73ccdb108c68` | unsure | 0.768 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `1d8c4ea9-ad13-4ff1-ada6-23453f8c1401` | unsure | 0.785 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `77dfd76e-8fec-46f6-bcf6-368344c11bfc` | unsure | 0.770 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f573fcc0-a501-468b-9554-23a38a845181` | unsure | 0.767 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `0df1fa23-1230-46aa-ae6f-b85e8279ce39` | unsure | 0.387 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `a57fd52b-d083-4f00-8214-616838166030` | unsure | 0.444 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f8944282-2bc9-4462-bbbe-88a3439540e4` | human | 0.236 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4950e0d2-5643-4c51-8b81-c507429d9852` | unsure | 0.535 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `b2b6640e-fa59-4bcc-837a-f6b5042a4700` | unsure | 0.429 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c1cdd00e-334f-4569-ad97-d1f7bc49faf8` | unsure | 0.480 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `0c73c3e1-6783-4aba-ae1c-4ab7ad27d551` | unsure | 0.564 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `5af668e2-4db1-42fe-95a1-f8fc7f6f59f2` | human | 0.150 |  |
| MF04 | malformed | text is only punctuation | 200 | `c1bed379-9e91-4b66-9b6f-445be8f21a81` | human | 0.158 |  |
| MF05 | malformed | text is a very long single word | 200 | `9f8b9600-6f40-4fc6-84a0-13e0a7eaa33f` | unsure | 0.600 |  |
| MF06 | malformed | text is emoji only | 200 | `792e814b-6963-4581-968a-5211af5409c1` | unsure | 0.600 |  |
| MF07 | malformed | text is right-to-left script | 200 | `95b5d601-712e-482e-bda9-89e1d364a850` | unsure | 0.600 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `7c885709-bf44-4aa2-953d-f0d07c481209` | unsure | 0.884 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `4752d904-e0f2-49bd-b368-b0ccb53f1c6e` | unsure | 0.363 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `bc52dfc7-412c-4b28-af0e-4fc16b624887` | human | 0.184 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4494a7bd-72f0-4c89-989f-1549215f5734` | human | 0.215 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `29304aee-2f73-4f9a-9d7c-ed2756133e3b` | human | 0.215 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0214cbe6-e0c1-485c-b002-c9c580970001` | human | 0.215 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73c9d023-91c7-45ad-9fdc-6ca94f379acc` | human | 0.215 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cc3f404b-6295-4138-96c3-e5f3a2ea2a42` | human | 0.215 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "cdee85e5-ce08-4409-bd77-1475797320fc",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3465,
  "model_score": 0.1635,
  "style_score": 0.7734,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f75a81b1-3b50-4879-af6c-364ae8e510cb",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5021,
  "model_score": 0.5943,
  "style_score": 0.2871,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "27590a87-75ac-4196-9b11-fb72644b1453",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5621,
  "model_score": 0.6662,
  "style_score": 0.3192,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f6a9d6fd-8c50-4440-9313-a8746332c9b7",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6566,
  "model_score": 0.6114,
  "style_score": 0.762,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "f81fa643-b584-4f40-9627-20abb3fa62cc",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3401,
  "model_score": 0.3212,
  "style_score": 0.3841,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "4fb4da0c-6983-4af5-bf86-e92a2ea7b914",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5321,
  "model_score": 0.5727,
  "style_score": 0.4375,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bd8f6846-7f04-4b5c-b4db-e0af12f7d258",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5282,
  "model_score": 0.5862,
  "style_score": 0.393,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "f553f8f5-ddd2-4f57-8eeb-e5d8cdeee2e9",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3709,
  "model_score": 0.2452,
  "style_score": 0.6643,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b18590c1-413c-43b6-8cac-f690aeb89fd5",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6068,
  "model_score": 0.7042,
  "style_score": 0.3795,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "7c40fe49-7928-49e9-99bc-e56c9a9f3b41",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8869,
  "model_score": 0.9792,
  "style_score": 0.6717,
  "label": "This may have been written with the help of AI. Checks like this one can be wrong, and we haven't decided anything about your work. If you wrote it yourself, tell us and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ad1868b5-6fb3-4fb4-afac-cdd8cee0654b",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6022,
  "model_score": 0.6175,
  "style_score": 0.5666,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "45fb82d6-e8d7-4695-bc2c-acc43cf70efe",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7412,
  "model_score": 0.7387,
  "style_score": 0.7471,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "7ba5608b-1635-4653-a035-049cbe78a486",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7648,
  "model_score": 0.8051,
  "style_score": 0.6708,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "892ddc74-9a82-47ef-8495-73ccdb108c68",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7682,
  "model_score": 0.8329,
  "style_score": 0.6172,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "1d8c4ea9-ad13-4ff1-ada6-23453f8c1401",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7847,
  "model_score": 0.8005,
  "style_score": 0.7478,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "77dfd76e-8fec-46f6-bcf6-368344c11bfc",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7696,
  "model_score": 0.8814,
  "style_score": 0.5088,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "f573fcc0-a501-468b-9554-23a38a845181",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7671,
  "model_score": 0.8816,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0df1fa23-1230-46aa-ae6f-b85e8279ce39",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3874,
  "model_score": 0.3223,
  "style_score": 0.5392,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "a57fd52b-d083-4f00-8214-616838166030",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4437,
  "model_score": 0.4625,
  "style_score": 0.4,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f8944282-2bc9-4462-bbbe-88a3439540e4",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2364,
  "model_score": 0.2044,
  "style_score": 0.3111,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "4950e0d2-5643-4c51-8b81-c507429d9852",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5348,
  "model_score": 0.5943,
  "style_score": 0.3959,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "b2b6640e-fa59-4bcc-837a-f6b5042a4700",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4294,
  "model_score": 0.4998,
  "style_score": 0.265,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c1cdd00e-334f-4569-ad97-d1f7bc49faf8",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4802,
  "model_score": 0.6401,
  "style_score": 0.1072,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "0c73c3e1-6783-4aba-ae1c-4ab7ad27d551",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5638,
  "model_score": 0.5583,
  "style_score": 0.5768,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "5af668e2-4db1-42fe-95a1-f8fc7f6f59f2",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.15,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c1bed379-9e91-4b66-9b6f-445be8f21a81",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1578,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "9f8b9600-6f40-4fc6-84a0-13e0a7eaa33f",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "792e814b-6963-4581-968a-5211af5409c1",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "95b5d601-712e-482e-bda9-89e1d364a850",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "7c885709-bf44-4aa2-953d-f0d07c481209",
  "creator_id": "attacker_MF08",
  "guess": "unsure",
  "confidence": 0.8843,
  "model_score": 0.9876,
  "style_score": 0.6432,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "4752d904-e0f2-49bd-b368-b0ccb53f1c6e",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3627,
  "model_score": 0.2395,
  "style_score": 0.65,
  "label": "We couldn't tell whether this was written by a person or with the help of AI. That isn't a judgment about you or your work, and you don't need to do anything. If you'd like someone to take a look anyway, you can ask.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "bc52dfc7-412c-4b28-af0e-4fc16b624887",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.1844,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4494a7bd-72f0-4c89-989f-1549215f5734",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2151,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "29304aee-2f73-4f9a-9d7c-ed2756133e3b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2151,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "0214cbe6-e0c1-485c-b002-c9c580970001",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2151,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "73c9d023-91c7-45ad-9fdc-6ca94f379acc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2151,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "cc3f404b-6295-4138-96c3-e5f3a2ea2a42",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2151,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
