# Maintainers' guide

How to keep the course running, tested and released for years. If you are taking over the course, start here.

## Principles

- **One source of truth:** this repository, under a GitHub **organization** account so it outlives any single maintainer.
  Make at least two people organization owners.
- **Replaceable windows:** the website (GitHub Pages), the run platforms (Kaggle, Colab) and the data mirrors
  (Kaggle Datasets, Hugging Face) can all change. Zenodo holds the permanent copy of every release and dataset.

## First-time setup (once)

1. Create the GitHub organization and move or create the repository there.
2. (Done for Marmara-Comp-Pathology.) If the repository ever moves, update every link and commit:
   ```bash
   python tools/set_org.py <org-name> [<repo-name>]
   ```
3. **Settings → Pages → Build and deployment → Source: GitHub Actions.** The **Publish website** workflow then deploys on every push to `main`.
4. Nothing to change under **Settings → Actions → General → Workflow permissions**: each workflow asks for the permissions it needs
   (the monthly test asks for `issues: write` so it can open an issue when it fails). Leave the default at "Read repository contents".
5. Log in to [Zenodo](https://zenodo.org) with GitHub, and switch the repository on under **GitHub** in your Zenodo account.
   Every GitHub release is then archived with its own DOI.
6. Optional: a custom domain under **Settings → Pages**, and update `site-url` in `_quarto.yml`.

## Working locally

```bash
python -m venv .venv && source .venv/bin/activate
# CPU-only PyTorch is enough for testing
pip install $(grep -E '^(torch|torchvision)==' environment.txt) --index-url https://download.pytorch.org/whl/cpu
pip install -r environment.txt

python tests/check_notebooks.py          # static checks (seconds)
python tests/check_notebooks.py --fix    # clear outputs before committing
python tests/run_notebooks.py            # run all lessons on tiny synthetic data (minutes)
quarto preview                           # preview the website (pip install quarto-cli, or https://quarto.org)
```

## How the pieces fit

| Piece | Where | Notes |
|---|---|---|
| Lessons | `lessons/NN-name/lesson.ipynb` | Outputs cleared. First code cell is the `# COMPPATH-SETUP` cell. |
| Checkpoints | `lessons/NN-name/checkpoint.md` | Formal ones: lessons 5, 9, 11. |
| Setup cell | every lesson | Pins packages, detects Kaggle / Colab / local, defines `WORK_DIR` and `SMOKE_TEST`. Its detection logic copies `utils/env.py`; keep them in sync. |
| Pinned versions | `environment.txt` | Used by CI and local runs. Notebooks pin the same versions in their setup cell, except PyTorch (see below). |
| Website | `_quarto.yml`, `*.qmd` | Built by `.github/workflows/publish.yml`. Notebooks are rendered, never executed. |
| Static checks | `tests/check_notebooks.py`, `.github/workflows/checks.yml` | Every push and pull request. |
| Notebook tests | `tests/run_notebooks.py`, `.github/workflows/test-notebooks.yml` | Monthly, on demand, and on pull requests that touch lessons. |

**Why PyTorch is not pinned inside notebooks.** Kaggle and Colab ship CUDA builds of PyTorch matched to their GPUs and drivers.
Reinstalling it costs minutes and often breaks the GPU. Notebooks therefore use the platform's PyTorch and pin the libraries on top
(fastai and friends). `environment.txt` pins PyTorch for CI and local runs, and records the versions the lessons were last tested with.

**Smoke-test mode.** With `COMPPATH_SMOKE_TEST=1`, each lesson replaces its real data with a tiny synthetic set and uses the smallest settings,
so CI can run it on a CPU in minutes. This catches broken imports, changed APIs and typos. It does **not** check that a model learns well:
that needs a real GPU run (see the yearly checklist).

## When the monthly test fails

The workflow opens an issue labelled `notebook-test-failure` (or comments on the open one) with the failing notebook and the error.

1. Read the error in the issue or the run log.
2. Reproduce locally: `python tests/run_notebooks.py lessons/NN-name/lesson.ipynb`.
3. Typical causes and fixes:
   - **A pinned package no longer installs** (removed from PyPI, or incompatible with a new Python): move to the nearest working version,
     in both `environment.txt` and the lesson's setup cell.
   - **A dataset moved** or a download URL changed: point the lesson at the Zenodo master copy or a mirror.
   - **A GitHub Action is deprecated:** bump its major version in the workflow file.
4. If the fix changes behaviour, test the lesson for real on Kaggle with a GPU before closing the issue.

## Platform changes

Kaggle's free tier (at the time of writing: about 30 GPU hours a week, 12-hour sessions, about 20 GB writable disk in `/kaggle/working`,
about 200 GB of private datasets) can change. Check it before each cohort. If Kaggle becomes unusable, the Colab badge is the fallback:
every lesson must keep working there too. Update `getting-started.qmd` with any change learners will notice.

## Data

- Every curated subset (pre-extracted patches, precomputed features) is first published on **Zenodo** with a DOI,
  then mirrored to Kaggle Datasets and Hugging Face. Lessons should prefer the mirror on the platform they run on and fall back to Zenodo.
- Record each dataset, its licence and its DOI in `data/README.md` and in the lesson's credits.
- Never commit data to the repository. Departmental data follows the rules in `CONTRIBUTING.md` ("Privacy") and `data/README.md`.

## Yearly release (before each cohort)

1. **Update versions.** Move `environment.txt` and the setup cells to current versions, and check that the Python version used in CI
   matches roughly what Kaggle and Colab run.
2. **Run every lesson for real** on Kaggle with a GPU, and once on Colab. Check timing and GPU use, and that results are in the expected range.
3. **Review content:** dead links, videos taken down, platform screenshots and menu names, regulatory updates in lesson 10.
4. Check the Kaggle limits above and update the docs.
5. Make sure all workflows are green.
6. **Tag and release:**
   ```bash
   git tag -a v2027 -m "Course release for the 2027 cohort"
   git push origin v2027
   ```
   Then create a GitHub release from the tag, with a short changelog. Zenodo archives it and mints a DOI automatically.
7. Add the new DOI to `CITATION.cff` and the website's About page.

Keep earlier releases available: a cohort that started on `v2026` can keep using that tag.

## Handing over

Before stepping down: add the new maintainer as an organization owner, give them access to the Zenodo community and the
Kaggle and Hugging Face accounts that hold the mirrors (use organization accounts there too, where possible), and walk them through this file.
