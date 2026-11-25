#!/usr/bin/env python3
"""Write the one-line deadline excuse to /output/entry.txt."""

import os

LINE = "I set three alarms for the deadline, and all three of them snoozed me."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate check: the bounty only accepts a single line of 1-200 UTF-8
    # characters, not only white space. Fail loudly instead of silently
    # shipping an invalid entry if the line is ever edited.
    if not LINE or not LINE.strip():
        raise SystemExit("error: entry line is empty or only white space")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("error: entry must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"error: entry is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what was actually written, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit("error: written output does not match the entry line")


if __name__ == "__main__":
    main()
