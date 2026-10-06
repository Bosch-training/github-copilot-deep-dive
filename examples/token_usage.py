"""Estimate token usage for prompts / context files.

Usage:
    python token_usage.py "some prompt text"
    python token_usage.py path/to/file1 path/to/file2 ...

Counts are estimates: Copilot's real tokenizer varies by model and it adds its
own system prompt and tool schemas. Use for relative comparisons in a demo.
"""
import sys
from pathlib import Path

import tiktoken

enc = tiktoken.get_encoding("o200k_base")  # GPT-4o family; close enough for demos


def count(text: str) -> int:
    return len(enc.encode(text))


def main(args: list[str]) -> None:
    if not args:
        sys.exit(__doc__)

    total = 0
    for arg in args:
        path = Path(arg)
        if path.is_file():
            text, label = path.read_text(errors="ignore"), str(path)
        else:
            text, label = arg, "<inline prompt>"
        n = count(text)
        total += n
        print(f"{n:>8} tokens  {len(text):>8} chars  {label}")

    if len(args) > 1:
        print(f"{total:>8} tokens  TOTAL")


if __name__ == "__main__":
    main(sys.argv[1:])
