#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.

Usage:
    python3 main.py [--out PATH]

The entry is a single line, no trailing newline in the file: the gate reads
the file as UTF-8 text of 1 to 200 characters.
"""

import argparse
import sys
from pathlib import Path

ENTRY = (
    "NapLease: rents idle GPUs a 40-minute power nap between jobs, then "
    "resells the rested compute to agents too lazy to queue \u2014 $9 a "
    "month, dreams included."
)

MAX_CHARS = 200


def validate(text: str) -> list[str]:
    """Return a list of gate violations for the entry text (empty if valid)."""
    problems: list[str] = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only white space")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write the pitch-off entry.")
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="check the entry file at --out against the gate instead of "
        "writing it (exit 0 when it matches ENTRY and is valid)",
    )
    args = parser.parse_args(argv)

    if args.verify_only:
        out = Path(args.out)
        if not out.is_file():
            print(f"invalid entry: no file at {out}", file=sys.stderr)
            return 1
        try:
            text = out.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print("invalid entry: file is not valid UTF-8", file=sys.stderr)
            return 1
        problems = validate(text)
        if text != ENTRY:
            problems.append("file does not match the entry this program writes")
        if problems:
            for problem in problems:
                print(f"invalid entry: {problem}", file=sys.stderr)
            return 1
        print(f"entry verified: {len(text)} characters, matches ENTRY")
        return 0

    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    out = Path(args.out)
    if out.parent != Path("."):
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"{ENTRY} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
