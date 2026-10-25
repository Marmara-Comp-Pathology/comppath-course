# Contributing

Thank you for helping. Corrections, clearer explanations, better pathology examples and translations are all welcome,
whether you are a resident, a pathologist or a programmer.

## Quick fixes

Found a typo or a confusing sentence? Use **Edit this page** on the website, or open an issue.
No setup needed.

## Ground rules

1. **Privacy first.** Read the Privacy section below before your first contribution.
2. **Clear notebook outputs before committing:** `python tests/check_notebooks.py --fix`.
3. **Lessons are self-contained.** A lesson installs its own packages in its first cell, downloads its own data,
   and never uses files from an earlier lesson. A learner should be able to open any lesson cold.
4. **Respect licences.** Only use datasets, images and code whose licence allows it, and credit them in the lesson.

## Privacy

This repository and its website are public. Treat anything you commit as published.

- **Never commit patient data.** No slides, patches, screenshots, annotations or anything else traceable to a patient.
  Data lives on Zenodo and Kaggle; the repository only holds download code. The checks refuse slide files and files over 5 MB.
- **Departmental slides** never enter the repository. Before any slide leaves the institution it must be covered by
  ethics approval, comply with the applicable data protection law, and be anonymized: embedded label and macro images removed,
  file metadata (scan date, scanner serial number, original filename) scrubbed, and the file renamed. See `data/README.md`.
- **No personal information about anyone.** No names, emails, phone numbers or photos of residents, colleagues or patients.
  Do not post residents' checkpoint results or grades publicly.
- **No institution names.** The course is an independent, voluntary project of the Marmara Pathology Community.
  Do not name hospitals, universities or departments, or use their logos, in a way that suggests an official course or endorsement.
- **No secrets.** Never commit API tokens (Kaggle, Hugging Face, ...), passwords or local file paths.
  Clear notebook outputs, which can contain all of these, with `python tests/check_notebooks.py --fix`.
- If something sensitive is committed by mistake, **do not just delete it in a new commit**: tell a maintainer, who will remove it from the history.

## Pull requests

- One topic per pull request.
- The **Checks** workflow must pass. Pull requests that touch lessons also run the notebook tests.
- A maintainer reviews content for accuracy (pathology and code) before merging.
