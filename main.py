"""news-summary-01 entry (Python 3.13, standard library only).

Copies the summary in summary.txt (beside this file) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no network, no randomness, no clock, no environment
dependence beyond the output directory. Writes the same bytes on
every run. Guards the entry gate before writing: the summary must be
1-2000 code points and non-whitespace, otherwise it fails loudly
instead of submitting an invalid entry.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


MIN_CHARS = 1
MAX_CHARS = 2000


def main() -> None:
    summary = (HERE / "summary.txt").read_text(encoding="utf-8")
    n_chars = len(summary)
    if n_chars < MIN_CHARS or n_chars > MAX_CHARS:
        raise SystemExit(
            f"summary.txt is {n_chars} characters, "
            f"outside the allowed {MIN_CHARS}-{MAX_CHARS} range"
        )
    if not summary.strip():
        raise SystemExit("summary.txt contains only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
