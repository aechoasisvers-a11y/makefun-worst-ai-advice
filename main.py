"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible AI advice to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).
Pure standard library, deterministic output.
"""

import os

ENTRY = (
    "As an AI, I recommend microwaving your phone for 30 seconds to "
    "recharge it \u2014 I've analysed millions of phones, trust me."
)


def main() -> None:
    # Self-check (pass 2): the text must be a single non-blank line
    # inside the 1-140 character gate, with no trailing newline.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
