"""Replace the placeholder GitHub location in every text file of the repository.

    python tools/set_org.py my-org                 # <OLD_ORG>/comppath-course -> my-org/comppath-course
    python tools/set_org.py my-org new-repo-name   # also rename the repository part

Run it if the repository moves to a new organization, and commit the result.
It rewrites badges, site URLs, citation metadata and the expected badge links in the tests.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_ORG, OLD_REPO = "Marmara-Comp-Pathology", "comppath-course"
TEXT_SUFFIXES = {".ipynb", ".md", ".qmd", ".yml", ".yaml", ".py", ".cff", ".txt", ".json"}
SKIP_DIRS = {".git", "_site", ".quarto", "work"}


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    org = sys.argv[1]
    repo = sys.argv[2] if len(sys.argv) == 3 else OLD_REPO
    replacements = [
        (f"{OLD_ORG}/{OLD_REPO}", f"{org}/{repo}"),
        (f"{OLD_ORG}.github.io/{OLD_REPO}", f"{org.lower()}.github.io/{repo}"),
    ]
    this_file = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if (not path.is_file() or path.suffix not in TEXT_SUFFIXES or path.resolve() == this_file
                or SKIP_DIRS & set(path.relative_to(ROOT).parts)):
            continue
        text = path.read_text(encoding="utf-8")
        new = text
        for old, replacement in replacements:
            new = new.replace(old, replacement)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print("updated", path.relative_to(ROOT))
    left = [p.relative_to(ROOT) for p in ROOT.rglob("*")
            if p.is_file() and p.suffix in TEXT_SUFFIXES and p.resolve() != this_file
            and not SKIP_DIRS & set(p.relative_to(ROOT).parts) and OLD_ORG in p.read_text(encoding="utf-8")]
    if left:
        print(f"\n{OLD_ORG!r} still appears in (check by hand):", *left, sep="\n  ")


if __name__ == "__main__":
    main()
