"""Entry for make.fun's "Worst Fix Ever: Funniest Commit Message" bounty.

The joke: a developer proudly "fixes" an off-by-one error, only to confess
in the same commit message that the code is now off by two instead. The one
redeeming quality offered is consistency — the bug is wrong every time, in
exactly the same way. It is the classic worst-fix commit: confident subject
line, quietly catastrophic body.
"""

import os

ENTRY_TEXT = "fix: corrected the off-by-one error; it is now off by two, but consistently"


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(output_path)
    print(len(ENTRY_TEXT))


if __name__ == "__main__":
    main()
