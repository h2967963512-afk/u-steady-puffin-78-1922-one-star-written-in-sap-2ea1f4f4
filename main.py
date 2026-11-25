"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
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
