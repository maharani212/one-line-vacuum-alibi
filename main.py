#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for The Vacuum's Alibi.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'I did not miss the spot. I conducted a 47-minute survey of it, found it structurally sound, and moved on to more urgent dust.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
