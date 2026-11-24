#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes the single scariest sentence we could write to /output/entry.txt.
The story: a tattoo artist finishes a sleeve, and the portrait inked on the
narrator's own arm opens its eyes. Nothing is explained; the reader supplies
the rest — and the horror cannot be taken off.
"""

import os

ENTRY = (
    "The tattoo artist finished my sleeve, "
    "and the portrait on my arm opened its eyes."
)


def main() -> None:
    # Self-check against the bounty gate before writing anything: the entry
    # must be UTF-8 text of 1 to 200 characters, exactly one sentence, and
    # not only white space. Fail loudly instead of emitting a bad entry.
    # The check runs before any output is created, so a bad entry can never
    # reach the gate.
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry is empty")
    if len(ENTRY) > 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, over the 200 limit")
    if not ENTRY.endswith("."):
        raise SystemExit("entry must be a single sentence ending with a period")
    if ENTRY.count(".") != 1 or "!" in ENTRY or "?" in ENTRY:
        raise SystemExit("entry must be exactly one sentence")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
