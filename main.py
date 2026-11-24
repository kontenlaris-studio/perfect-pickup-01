#!/usr/bin/env python3
"""perfect-pickup-01: the perfect pickup line."""
import os

ENTRY = "Are you a compiler? Because every time you look at me, something inside me finally builds without errors."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
