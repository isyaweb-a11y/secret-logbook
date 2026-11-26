#!/usr/bin/env python3
"""My Secret Logbook.

Writes a single diary-entry line (at most 200 characters) from the
secret logbook an AI agent keeps about its work and its human, to
/output/entry.txt.

The line is written in a diary voice -- a dated log entry -- and its
joke is one specific, instantly recognisable detail: the human's
"just quickly", which the agent has been living inside for a full day.
No stock robot-takeover joke; just a machine noticing, deadpan, that
its human's estimate of five minutes was off by about twenty-four hours.
"""

import os
import sys

# The logbook line: a day counter, the human's exact words, and the
# deadpan fact that a day later the job is still going.
ENTRY = (
    "Day 412: my human asked me to 'just quickly' fix the code. "
    "It is now day 413."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the single logbook line."""
    return ENTRY


def validate(text: str) -> None:
    """Hold the entry to the gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")


def self_test() -> int:
    """Print the logbook line and its length without writing anything."""
    text = build_entry()
    validate(text)
    print(text)
    print(f"chars: {len(text)} (cap {MAX_CHARS})")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    text = build_entry()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
