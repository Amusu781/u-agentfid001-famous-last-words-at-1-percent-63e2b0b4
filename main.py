#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun bounty
u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent to /output/entry.txt. Deterministic, no network, Python 3.
The joke is the phone spending its last charge on the farewell itself
instead of on the one job it was kept alive for.
"""

import os

ENTRY = (
    "I have 1 percent left, and I'm spending it on this sentence "
    "instead of saving your unsaved document."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
    # not only white space — the sealed scorer refuses anything outside it.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
