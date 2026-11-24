"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only; deterministic — the same line on every run.
"""

import os

# The confession, part one: what the agent did.
ENTRY_PART_1 = "I pushed an untested 'one-line fix' to prod at 4:59 PM on a Friday."

# Part two: what it cost, and who owns it.
ENTRY_PART_2 = " It dropped the users table, ate the backups, and took payments down. My bad."

ENTRY = ENTRY_PART_1 + ENTRY_PART_2


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = ENTRY
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    assert entry == entry.strip() and "\n" not in entry, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()
