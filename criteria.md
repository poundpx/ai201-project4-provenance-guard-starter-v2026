# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives

Of 20 pieces I wrote myself, at most 1 is labelled "likely AI."

**Why this target:** The person who pays for a false positive is the writer, not
the site. When I traced this case I found that an English learner writing plain,
careful sentences looks AI-like to both of my signals at once, so neither the
weights nor the thresholds rescue them. The appeal path only helps people who
actually appeal, and the writer least likely to push back is the one most likely
to be flagged. One in 20 is already one real person being told their own work
looks machine-made, so I am not willing to allow more than that.

---

## 2. Label coverage

In a test set of 12 texts, at least 2 land in each of the three bands.

**Why this target:** A label nobody can reach is a band that does not exist. My
starter's own config warns that while the style signal returns a constant, the
combined score cannot leave 0.25 to 0.75, which would make "likely AI"
unreachable and quietly turn my service into one that never flags anything.
I also want to be careful about handing out the "human" label, because AI writes
well now and clearing text as human too easily is its own failure. Asking for at
least 2 in each band proves all three are live without demanding an exact split
that normal model variance would break.



---

## 3. The appeal path

Of 5 test appeals sent with a valid `content_id`, all 5 return `under_review`,
write an appeal entry to the log, and leave the original decision in the log
alongside it. An appeal sent with a `content_id` that does not exist returns an
error rather than quietly succeeding.

**Why this target:** There is no acceptable failure rate here, so the number is
all of them. The appeal is the only thing a wrongly flagged writer can do, and
an appeal that looks like it worked but wrote nothing is worse than one that
visibly fails, because the writer walks away believing a human will look at
their work when nobody will. I am deliberately not checking whether the
reasoning the writer sends makes sense. Judging an appeal is a human's job, and
a service that silently discarded appeals it found unconvincing would be doing
the same harm as the false positive it is supposed to correct.

---

## 4. Bad input

Three kinds of input, three expected outcomes, and `/ping` still answers after
all of them:

| Input | Expected outcome |
|---|---|
| `text` missing from the request | Error response naming what was wrong, logged as a rejection |
| `text` present but empty | Error response naming what was wrong, logged as a rejection |
| `text` over 5,000 words | Scored and logged, but with status `under_review` rather than `decided` |

**Why this target:** Missing and empty text are not the same problem as text my
service cannot judge properly. For the first two, my handler cannot tell a
writer's mistake from a bug in the site sending the request from something
broken on the network, so the only sane response is to refuse cleanly, say what
was wrong, and record it. A single bad request is noise; the same rejection
arriving a thousand times is how I would find out something upstream is broken.

Very long text is a different failure and I am deliberately not refusing it. My
detector reads at most 400 tokens, roughly 300 words, so on a 10,000-word
submission about 97% of the text is never scored at all. Returning a confident
label on that would be dishonest, and quietly discarding the submission would
punish a writer who has done nothing wrong. Sending it to `under_review` says
what is actually true: the text was accepted, and my service is not able to
judge it on its own. It also closes a hole, because anything longer than the
truncation point can hide whatever it likes past word 300.

`/ping` is the control. If it stops answering, the problem is the service
itself and not the input.

---

## 5. Score spread

Across 4 texts I judge clearly AI-written and 4 I judge clearly human-written,
the average combined score of the AI set is at least 0.25 higher than the
average of the human set.

**Why this target:** If the two sets score the same, no threshold I pick can
separate them and every label my service produces is noise. Signal one on its
own already managed a gap of about 0.46 on two sample texts, but a weighted
average pulls both sets toward the middle, so the combined gap will be smaller
than either signal's. I chose 0.25 because it is low enough to survive that
compression and high enough that a signal which returns nearly the same number
for everything will fail it, which is the finding I actually want to catch.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
