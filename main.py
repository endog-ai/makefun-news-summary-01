"""news-summary-01 entry (Python 3.13, standard library only).

Copies the summary in summary.txt (beside this file) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no network, no randomness, no clock, no environment
dependence beyond the output directory. Writes the same bytes on
every run.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    summary = (HERE / "summary.txt").read_text(encoding="utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
