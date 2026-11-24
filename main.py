#!/usr/bin/env python3
"""Robot pickup line entry: a robot's signal trace, flat for years,
spiking for the first time when the person it likes walks in."""

import os

LINE = "My trace stayed flat for years \u2014 then you walked in, and it spiked for the first time."


def main() -> int:
    # The gate allows 1-200 characters on a single line; refuse to
    # write anything else rather than silently shipping a bad entry.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or not LINE.strip():
        raise ValueError("pickup line must be one line of 1-200 characters")
    os.umask(0o022)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
