#!/usr/bin/env python3
"""Epitaph entry: writes one line of famous last words to /output/entry.txt.

The line is a first-person dying speech, carved in stone. It is built from
four short farewells, each naming someone (or something) left behind: the
wife gets the love, the boss gets the resignation, the cat gets the secret
of the Wi-Fi password, and the bakso and the chillies get their last care.
The twist lands in the middle -- the password dies with its owner -- and
the line closes on a small, stubborn, everyday chore.
"""

import os

# Four farewells, joined into a single carved line.
FAREWELLS = [
    "Tell my wife I loved her.",
    "Tell my boss I quit.",
    "Tell the cat the Wi-Fi password dies with me.",
    "Keep my bakso warm, and water my chillies daily.",
]

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def build_epitaph():
    """Join the farewells into one line and check the gate: 1-150 chars."""
    text = " ".join(FAREWELLS)
    if not 1 <= len(text) <= 150:
        raise ValueError("epitaph must be 1-150 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("epitaph must be a single line")
    return text


def main():
    text = build_epitaph()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
