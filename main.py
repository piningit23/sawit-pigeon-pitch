#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry (program/v1).

Writes one original elevator pitch, in the voice of a city pigeon
pitching investors for its startup, to /output/entry.txt.

Python 3.13, standard library only. Deterministic: the same line,
byte for byte, on every run.
"""

import os

PITCH = (
    "I raised my seed round one crumb at a time, and now Coo.ly turns "
    "park statues into billboards: pigeons never churn, we always come "
    "back for seconds."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} chars to {path}")


if __name__ == "__main__":
    main()
