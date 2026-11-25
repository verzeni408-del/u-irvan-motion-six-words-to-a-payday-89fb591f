"""Six Words to a Payday -- entry writer (Python stdlib only)."""

import os

ENTRY = "First payday. Last thing I remember."
OUTPUT_PATH = "/output/entry.txt"


def main():
    words = ENTRY.split()
    if len(words) != 6:
        raise ValueError("entry must be exactly 6 words, got %d" % len(words))
    if not 1 <= len(ENTRY) <= 60:
        raise ValueError("entry must be 1-60 characters, got %d" % len(ENTRY))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
