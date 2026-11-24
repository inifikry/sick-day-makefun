"""The Funniest Sick-Day Excuse.

Writes a single line — one funny, half-believable sick-day excuse,
under 200 characters — to /output/entry.txt.

Python standard library only. Deterministic: the same line every run.
"""

import os

LINE = (
    "Sorry, can't come in today \u2014 I threw my back out reaching for "
    "the snooze button, and now the floor and I are in a committed "
    "relationship."
)


def main() -> None:
    # The gate requires 1-200 characters; fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
