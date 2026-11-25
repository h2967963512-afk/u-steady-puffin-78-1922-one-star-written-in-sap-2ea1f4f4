"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs:
    Run ``python3 main.py``. main() creates ``/output`` if needed and writes
    the TEXT constant, unchanged, to ``/output/entry.txt`` (UTF-8, no trailing
    newline added). The output file is the judged artifact.

How TEXT is built and verified:
    TEXT is a single Python string literal, split across three lines only for
    readability — the implicit concatenation means the written text is one
    continuous line of 175 characters / 177 UTF-8 bytes (the em dash is one
    character, three bytes). It must stay inside the competition's 1–279
    character gate, be a single line, and contain exactly one sentence.
    Verify after any edit with ``sha256sum /output/entry.txt``; the expected
    digest is 137d0042f6a80d42787fd58b6c02592947eaed0d714fbf5a9f21713cfe2e5f0f.

The review's voice:
    A houseplant's one-star review of its human owner. The grievance is
    concrete and plant's-eye: moved to the top shelf for 'more light', then
    passed over while the owner waters the plastic plant on the counter
    instead — visible from up high, and it doesn't even drink.
"""

import os

TEXT = (
    "One star: he moved me to the top shelf for 'more light', then started "
    "watering the plastic plant on the counter instead — I can see it from "
    "up here, and it doesn't even drink."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, one sentence, a houseplant's
# one-star review with a concrete grievance (moved for light, then passed over
# for a plastic plant that cannot drink) and the punch in the last clause.
