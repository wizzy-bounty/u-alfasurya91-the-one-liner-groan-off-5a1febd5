#!/usr/bin/env python3
"""The One-Liner Groan-Off — writes one original dad joke to entry.txt."""

import os

ENTRY = "The electrician's kids were shocked by how grounded he was."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
