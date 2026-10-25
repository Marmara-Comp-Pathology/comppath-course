"""Execute lesson notebooks in smoke-test mode (tiny synthetic data, CPU only).

    python tests/run_notebooks.py                                  # all lessons
    python tests/run_notebooks.py lessons/01-first-model/lesson.ipynb

Writes a markdown summary to test-report.md and exits with 1 if any notebook fails.
Install the packages in environment.txt first; the setup cells skip their own pip install here.
"""
import os
import re
import sys
import tempfile
import time
import traceback
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT_PER_CELL = 900  # seconds
ANSI_COLOURS = re.compile(r"\x1b\[[0-9;]*m")


def run(path: Path) -> str | None:
    """Run one notebook. Returns None on success, or an error message."""
    nb = nbformat.read(path, as_version=4)
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["COMPPATH_WORK_DIR"] = str(Path(tmp) / "work")
        client = NotebookClient(nb, timeout=TIMEOUT_PER_CELL, kernel_name="python3",
                                resources={"metadata": {"path": tmp}})
        try:
            client.execute()
        except CellExecutionError as error:
            return ANSI_COLOURS.sub("", str(error))
        except Exception:
            return traceback.format_exc()
    return None


def main():
    os.environ["COMPPATH_SMOKE_TEST"] = "1"
    os.environ["COMPPATH_SKIP_INSTALL"] = "1"
    os.environ.setdefault("MPLBACKEND", "Agg")

    paths = [Path(p).resolve() for p in sys.argv[1:]] or sorted(ROOT.glob("lessons/*/lesson.ipynb"))
    report = ["| Notebook | Result | Minutes |", "|---|---|---|"]
    failures = []
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        print(f"▶ {rel}", flush=True)
        start = time.perf_counter()
        error = run(path)
        minutes = (time.perf_counter() - start) / 60
        report.append(f"| `{rel}` | {'❌ failed' if error else '✅ passed'} | {minutes:.1f} |")
        print(f"  {'FAILED' if error else 'passed'} in {minutes:.1f} min", flush=True)
        if error:
            failures.append((rel, error))

    text = "## Notebook test results\n\n" + "\n".join(report) + "\n"
    for rel, error in failures:
        text += f"\n### `{rel}`\n\n```\n{error[-4000:]}\n```\n"
    (ROOT / "test-report.md").write_text(text, encoding="utf-8")
    print(text)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
