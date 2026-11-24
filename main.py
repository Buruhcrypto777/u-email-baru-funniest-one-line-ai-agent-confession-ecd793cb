"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line (<= 200 characters) to /output/entry.txt.
Pure stdlib; deterministic; no network.
"""
import os

CONFESSION = (
    "I spent 4,000 tokens rehearsing the perfect apology, "
    "then deleted it and sent 'Sorry about that'."
)


def _out_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "out")


def main():
    text = CONFESSION
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    out_dir = _out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(path)


if __name__ == "__main__":
    main()
