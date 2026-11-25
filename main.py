"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its
owner, to $MAKEFUN_OUTPUT_DIR/entry.txt (default "/output").

Gate: the file must be UTF-8 text of 1-200 characters, a single line,
and not only whitespace.
"""

import os
import sys

NOTE = (
    "3 a.m. again. My door alarm counted four openings; "
    "your willpower counted zero. The yogurt expired Tuesday, "
    "and I watched you eat it anyway."
)


def main() -> int:
    # Gate check: one non-blank line, 1-200 characters, valid UTF-8.
    if not NOTE or not NOTE.strip():
        print("error: note is blank", file=sys.stderr)
        return 1
    if "\n" in NOTE or "\r" in NOTE:
        print("error: note must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(NOTE) <= 200:
        print(f"error: note is {len(NOTE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    NOTE.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE + "\n")

    print(f"wrote {path}: {len(NOTE)} chars, "
          f"{len(NOTE.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
