"""Fast static checks for lesson notebooks and the repository. Runs on every push and pull request.

    python tests/check_notebooks.py          # check
    python tests/check_notebooks.py --fix    # also clear notebook outputs in place
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "Marmara-Comp-Pathology/comppath-course"  # rewritten by tools/set_org.py
SETUP_MARKER = "# COMPPATH-SETUP"
HOMEWORK_HEADING = "## Now try it yourself"
SLIDE_EXTENSIONS = {".svs", ".ndpi", ".mrxs", ".scn", ".vms", ".vmu", ".bif", ".czi", ".isyntax", ".dcm"}
MAX_FILE_MB = 5


def source(cell):
    text = cell.get("source", "")
    return "".join(text) if isinstance(text, list) else text


def clear_outputs(nb):
    changed = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            if cell.get("outputs") or cell.get("execution_count") is not None:
                changed = True
            cell["outputs"] = []
            cell["execution_count"] = None
    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]
        changed = True
    return changed


def check_notebook(path, fix):
    errors = []
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"not valid JSON: {error}"]
    if nb.get("nbformat") != 4:
        errors.append("must be nbformat 4")

    if fix and clear_outputs(nb):
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"cleared outputs: {path.relative_to(ROOT)}")
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code" and (cell.get("outputs") or cell.get("execution_count") is not None):
            errors.append(f"cell {i} has outputs; run with --fix to clear them")
            break

    code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
    if not code_cells or not source(code_cells[0]).startswith(SETUP_MARKER):
        errors.append(f"first code cell must start with '{SETUP_MARKER}'")

    markdown = [source(c) for c in nb["cells"] if c["cell_type"] == "markdown"]
    if not markdown or not markdown[0].startswith("# "):
        errors.append("first cell must be markdown starting with a level-1 title")
    if not any(HOMEWORK_HEADING in m for m in markdown):
        errors.append(f"missing homework section '{HOMEWORK_HEADING}'")

    if path.parent.parent.name == "lessons":
        rel = path.relative_to(ROOT).as_posix()
        github = f"github.com/{REPO}/blob/main/{rel}"
        kaggle = f"https://kaggle.com/kernels/welcome?src=https://{github}"
        colab = f"https://colab.research.google.com/github/{REPO}/blob/main/{rel}"
        first = markdown[0] if markdown else ""
        if kaggle not in first:
            errors.append(f"first cell is missing the Kaggle badge link {kaggle}")
        if colab not in first:
            errors.append(f"first cell is missing the Colab badge link {colab}")
        if not (path.parent / "checkpoint.md").exists():
            errors.append("lesson folder has no checkpoint.md")
    return errors


def repository_files():
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return [ROOT / line for line in out.splitlines() if line]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def check_repository():
    errors = []
    for path in repository_files():
        if not path.exists():
            continue
        rel = path.relative_to(ROOT)
        if path.suffix.lower() in SLIDE_EXTENSIONS:
            errors.append(f"{rel}: slide or DICOM files must never be committed (see CONTRIBUTING.md)")
        if path.stat().st_size > MAX_FILE_MB * 1024 * 1024:
            errors.append(f"{rel}: larger than {MAX_FILE_MB} MB; data belongs on Zenodo or Kaggle, not in the repo")
    return errors


def main():
    fix = "--fix" in sys.argv
    notebooks = sorted(ROOT.glob("lessons/*/lesson.ipynb")) + [ROOT / "templates" / "lesson-template.ipynb"]
    failures = 0
    for path in notebooks:
        for error in check_notebook(path, fix):
            print(f"{path.relative_to(ROOT)}: {error}")
            failures += 1
    for error in check_repository():
        print(error)
        failures += 1
    if failures:
        print(f"\n{failures} problem(s) found.")
        sys.exit(1)
    print(f"All checks passed ({len(notebooks)} notebooks).")


if __name__ == "__main__":
    main()
