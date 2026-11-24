#!/usr/bin/env python3
"""make.fun entry: u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

Writes a single one-line safety warning label for humans to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

LABEL = "WARNING: This human will say \"I'm five minutes away\" while still in bed, wearing no shoes, with no intention of leaving."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_label(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("label must be 1-200 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_label(LABEL)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(LABEL)
    if path.read_text(encoding="utf-8") != LABEL:
        raise IOError("written entry does not match the label")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
