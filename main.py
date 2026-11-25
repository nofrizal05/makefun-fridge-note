#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — one funny line.

A passive-aggressive note from a fridge to its owner, printed to stdout.
Stdlib only; deterministic output.
"""

LINE = (
    "Oh, you're back at 2 a.m. The leftovers have been here since Tuesday, "
    "and even THEY are judging you. You stared for five minutes and left "
    "with a pickle. Close the door."
)


def main():
    print(LINE)


if __name__ == "__main__":
    main()
