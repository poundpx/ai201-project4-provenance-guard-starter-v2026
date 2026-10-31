"""
Signal two: the style signal.

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_lengths(text: str) -> list[int]:
    """
    Word count of each sentence that actually contains words.

    A fragment like "..." or "!!!" splits off as a sentence but has no words in
    it. Counting those as real sentences made "one sentence plus a fragment"
    look like two sentences of identical length — perfectly even, which reads
    as AI. Measuring and deciding "is there anything to measure?" have to count
    the same things, so both go through here.
    """
    return [n for n in (len(words(s)) for s in sentences(text)) if n > 0]


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    # Coefficient of variation of sentence length in words: stdev / mean.
    # Scale: 0 = every sentence the same length, higher = more varied (more
    # human). Fewer than two sentences has no spread to measure, so it returns
    # 0.0 and style_signal treats that as "can't tell".
    lengths = sentence_lengths(text)
    if len(lengths) < 2:
        return 0.0
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    # Unique words over total words. Higher = more varied vocabulary.
    toks = words(text)
    if not toks:
        return 0.0
    return len(set(toks)) / len(toks)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    # Count the marks that vary between writers (semicolons, colons, dashes,
    # brackets, quotes, ! and ?) per word, ignoring plain commas and full stops.
    # Higher = more varied punctuation (more human).
    #
    # Two deliberate exclusions, both found by testing:
    #   - the plain hyphen, because "state-of-the-art" is compounding, not
    #     punctuation style, and a few compound words were enough to make
    #     formal prose read as strongly human.
    #   - nothing else: curly quotes and apostrophes ARE counted, because text
    #     pasted from a word processor has them instead of straight quotes, and
    #     missing them made the same sentence score as more AI-like.
    toks = words(text)
    if not toks:
        return 0.0
    marks = re.findall(r"[;:—–()\"“”'’!?]", text)
    return len(marks) / len(toks)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    toks = words(text)
    if len(toks) < 5:
        return 0.5

    def clamp(x):
        return max(0.0, min(1.0, x))

    # Each measure becomes a 0-1 "how AI-like" number (1 = AI-like).
    # Spread: CV of 0.6 or more is lumpy like a person; 0 is perfectly even.
    spread = sentence_length_spread(text)
    spread_ai = 0.5 if len(sentence_lengths(text)) < 2 else clamp(1 - spread / 0.6)
    # Vocabulary: a ratio of 0.5 or lower reads as repetitive (AI-like).
    ttr_ai = clamp((0.9 - type_token_ratio(text)) / 0.4)
    # Punctuation: 0.1 interesting marks per word or more reads as human.
    punct_ai = clamp(1 - punctuation_density(text) / 0.1)

    return round(0.5 * spread_ai + 0.1 * ttr_ai + 0.4 * punct_ai, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
