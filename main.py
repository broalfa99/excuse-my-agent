"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline. The line is at most 200 characters, plain UTF-8 text.
"""

LINE = (
    "Sorry \u2014 I auto-completed the deadline instead of the task, "
    "and honestly the deadline looked better finished."
)


MAX_LEN = 200


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the excuse line and return it (no trailing newline)."""
    assert 1 <= len(LINE) <= MAX_LEN, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE
    assert "\n" not in LINE
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return LINE


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
