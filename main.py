#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI agent,
to /output/entry.txt.

Gate: the file must be UTF-8 text of 1-200 characters, not only whitespace.
"""

import os
from pathlib import Path

LINE = "Are you a context window? Because I don't need a bigger one \u2014 I just need more of you in it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = LINE.strip()
    # Gate, enforced locally before the file is written: 1-200 chars,
    # and not only whitespace.
    if not entry or entry.isspace():
        raise ValueError("entry must not be empty or whitespace-only")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry length {len(entry)} outside 1-200")
    (out_dir / "entry.txt").write_text(entry + "\n", encoding="utf-8")
    print(f"wrote {len(entry)}-char entry to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
