"""Rant entry for make.fun: one short rant, at most 400 chars.

The program writes LINE verbatim to /output/entry.txt (233 chars).
"""

from pathlib import Path

LINE = "The printer has one job. It has paper, it has ink, it has power, and it has decided — at 8:58, two minutes before my meeting — that it would rather update its firmware than print. It is not broken. It is on strike, and it is winning."
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry text, creating /output when needed."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
