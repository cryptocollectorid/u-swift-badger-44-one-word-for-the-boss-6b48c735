#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes exactly one word describing a boss to /output/entry.txt
and prints it to stdout.
"""

import os

WORD = "Meetingizer"  # the boss who turns every question into a meeting


def main() -> None:
    # The gate wants exactly one word: no spaces, no caption, 1-30 chars.
    assert WORD and " " not in WORD and len(WORD) <= 30, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
