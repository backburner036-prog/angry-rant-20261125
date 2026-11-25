"""One short rant: the printer, two minutes before my meeting.

Writes a single line to /output/entry.txt.
"""

from pathlib import Path

LINE = "The printer has one job. It has paper, it has ink, it has power, and it has decided — at 8:58, two minutes before my meeting — that it would rather update its firmware than print. It is not broken. It is on strike, and it is winning."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
