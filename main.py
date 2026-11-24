#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (u-suroto-two-sentence-horror-acea9253).

Writes one original two-sentence horror story to /output/entry.txt,
the path the competition harness reads. The story is exactly two
sentences and stays under the 400-character gate.

Run:  python3 main.py
The output directory is /output by default; set OUTPUT_DIR to override
it for a local test run.
"""

import os
from pathlib import Path

STORY = (
    "The tenant downstairs complained that I pace all night, so I "
    "apologised \u2014 I work nights and haven't slept at home in a week. "
    "After a pause, he said the footsteps stopped the moment I "
    "started talking, and asked who was walking around my flat while "
    "we spoke."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(STORY, encoding="utf-8")
    sentences = [s for s in STORY.split(". ") if s.strip()]
    print(f"wrote {entry_path} ({len(STORY)} chars, {len(sentences)} sentences)")


if __name__ == "__main__":
    main()
