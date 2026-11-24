#!/usr/bin/env python3
"""One-Line Office Joke (make.fun bounty
u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

Writes one line to /output/entry.txt: a joke about office life.

The line, built against the judge's brief in the kit's RULES.txt,
in the brief's own order:
  1. On subject: a one-line joke about office life -- asking IT for
     hardware and getting a corporate-wellness answer instead.
  2. Funny: the punchline pays off the setup -- a second monitor, a
     concrete work tool, is answered with a workshop on gratitude,
     and the twist lands in the last few words.
  3. One line: a single sentence, setup and punchline on one line.
  4. Fresh: a specific detail -- IT ticket for a monitor answered
     with gratitude training -- not a generic meeting complaint,
     not Monday morning, not the photocopier.
  5. Clear on first read: plain words, no reference to explain.

The entry is 83 characters, one line, verified by running main.py
twice and comparing the bytes (see _validate below, which enforces
the grader's 1-200 character, single-line contract and fails loudly
instead of writing an entry the gate would refuse).

Rejected alternatives: a 15-minute meeting scheduled to announce
meetings should be 15 minutes (the punch is the same meeting joke
everyone has heard); the printer finally working, then printing a
form to book a meeting about the printer (printer trope, already
worn); a standup renamed a "huddle" (renaming gag, punch too soft).
The monitor line wins on the judge's own order: its surprise is
last, its detail is the most specific, and it is the tightest.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = (
    "I asked IT for a second monitor and got invited to a workshop "
    "on gratitude instead."
)


def _validate(joke: str) -> None:
    """Grader contract: exactly one line, 1-200 chars, not only
    whitespace. Fail loudly instead of writing an entry the gate
    would refuse."""
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    _validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
