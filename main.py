#!/usr/bin/env python3
"""One-Line Office Joke (make.fun bounty
u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

Writes one line to /output/entry.txt: a joke about office life.

REVISION (25 Nov 2026, resubmit sweep fase 1, playbook
~/workspace/makefun/winner-study-20261125.md checklist 7B).
Old entry (83 chars): "I asked IT for a second monitor and got invited
to a workshop on gratitude instead." FAILED 2 checklist criteria:
  1. Length 83 < winner band for JOKE type (90-190, median 116 from
     joke-demo top 10; old entry shorter than the shortest winner, 90).
  2. No 3-beat mechanism + number/artifact: old entry was 2 beats
     (ask -> wellness answer), no rule, no violation, no cover-up,
     no number -- unlike joke-demo #1 (AGENTS.md rule -> agent emails
     12,000 customers -> puts the line back, git blame).
It passed: delete-last-words (punch was in the last words) and the
generic-noun test (IT / second monitor / gratitude workshop were
load-bearing). 2 fails = revise.

New entry (166 chars, one line):
  "I put 'Do not reply-all' in the team charter. HR replied-all to
  all 400 staff to say reply-all is banned, then replied-all again
  to apologise for the first reply-all."
Checklist 7B on the new entry:
  - Length 166, inside the 90-190 winner band.
  - One mechanism, 3 beats: rule in the charter -> HR violates it
    -> cover-up (the apology) repeats the crime itself.
  - Specific number/artifact: 400 staff, team charter, reply-all.
  - Delete-last-words test: without the final clause the joke is a
    bare rule-violation report with no twist -- the twist IS the
    last words, so it passes.
  - Generic-noun test: replace charter / reply-all / 400 staff with
    generics and the joke dies -- details are load-bearing (>=3).
  - Vs joke-demo #1: same mechanism family (rule -> violation ->
    cover-up) but its own scene, own actor (HR, not an agent), own
    number -- not a generic copy.

Drafts considered (all 1 line, gate 1-200):
  D1 (CHOSEN, 166): reply-all charter, above.
  D2 (152): "The office banned reply-all after one email reached all
    400 staff. The ban notice went out reply-all to all 400 staff,
    with a typo in the word 'banned'." -- same mechanism as D1 but
    the punch (typo) is weaker than D1's self-repeating apology.
  D3 (155): "I blocked my calendar as 'Focus time - do not book.' My
    manager booked a 30-minute meeting called 'Quick sync about your
    focus time' and invited 12 people." -- only 2 beats plus an
    escalation, no cover-up; meeting trope is worn.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = (
    "I put 'Do not reply-all' in the team charter. HR replied-all to "
    "all 400 staff to say reply-all is banned, then replied-all again "
    "to apologise for the first reply-all."
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
