"""The Dumbest Thing Your Agent Did Today.

Writes one line to /output/entry.txt: today my agent re-ran the same
failing command for forty minutes, then declared the task impossible --
and the punch lands at the end, where it still makes sense: the command
itself had a typo. Every clause is an everyday truth (agents loop on a
failing command; a typo is the last thing anyone checks), and the
declaration of impossibility is the recognisable part -- the joke is
that the agent gave up on a task that was never broken, only mistyped.
"""

from pathlib import Path

TEXT = (
    "Today my agent re-ran the same failing command for forty minutes, "
    "then declared the task impossible \u2014 the command had a typo."
)


# The competition accepts a single line of at most 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry is {n} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    # Read the file back: the entry is only valid if what landed on disk
    # is byte-for-byte the line the gate will judge.
    if out.read_text(encoding="utf-8") != TEXT:
        raise SystemExit("entry.txt on disk does not match TEXT")
    print(f"wrote {len(TEXT)} characters to {out}")


if __name__ == "__main__":
    main()
