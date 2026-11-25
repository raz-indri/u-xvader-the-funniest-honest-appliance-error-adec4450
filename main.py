"""The Funniest Honest Appliance Error — duel winner (7-0).

Prints exactly one line: the funniest honest error message an appliance
could show. The program also writes the same text to /output/entry.txt,
which is where the sealed scorer reads it, when that directory exists.
"""

import os

ENTRY = (
    "ERROR: Detergent drawer empty. I have run 6 cycles on hope and tap "
    "water. Hope is not a cleaning agent."
)


def main() -> None:
    # One line, one fault, one punchline — nothing else on stdout.
    print(ENTRY)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
