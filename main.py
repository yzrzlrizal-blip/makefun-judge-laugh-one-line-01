"""One-line joke entry for make.fun's "Make the Judge Laugh in One Line".

The joke is a single original line about a smartwatch judging its owner's
sense of humour. This program checks the line against the competition gate
(one line, 1-200 characters, not only whitespace, no control characters)
and writes it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) for the judge.

Pure standard library; reads nothing outside this repository and uses no
network, no secrets and no environment beyond the output directory.
"""

import os
import sys

JOKE = "My smartwatch counted my laughs today. Zero. It suggested I upgrade my personality."

MAX_CHARS = 200


def check_line(text: str) -> None:
    """Raise ValueError if the line breaks the competition gate."""
    if not text.strip():
        raise ValueError("joke is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("joke contains control characters")


def main() -> int:
    check_line(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
