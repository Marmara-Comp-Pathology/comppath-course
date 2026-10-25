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
4. **No recorded talks by the course team.** Link existing public videos by their original creators.
5. **Respect licences.** Only use datasets, images and code whose licence allows it, and credit them in the lesson.

## Privacy

This repository and its website are public, and git keeps every version forever. Treat anything you commit as published.

- **Never commit patient data.** No slides, patches, screenshots, annotations or anything else traceable to a patient.
  Data lives on Zenodo and Kaggle; the repository only holds download code. The checks refuse slide files and files over 5 MB.
- **Departmental slides** (capstone) never enter the repository. Before any slide leaves the institution it must be covered by
  ethics approval, comply with the applicable data protection law (for example the GDPR or its national equivalent), and be anonymized: embedded label and macro images removed,
  file metadata (scan date, scanner serial number, original filename) scrubbed, and the file renamed. See `data/README.md`.
- **No personal information about anyone.** No names, emails, phone numbers or photos of residents, colleagues or patients.
  Do not post residents' checkpoint results or grades publicly.
- **No institution names.** The course is an independent, voluntary project of the Marmara Pathology Community.
  Do not name hospitals, universities or departments, or use their logos, in a way that suggests an official course or endorsement.
- **No secrets.** Never commit API tokens (Kaggle, Hugging Face, ...), passwords or local file paths.
  Clear notebook outputs, which can contain all of these, with `python tests/check_notebooks.py --fix`.
- **Check your commit identity.** Git records the name and email set in your git configuration in every commit.
  If you do not want your email public, use GitHub's private noreply address (GitHub → Settings → Emails).
- If something sensitive is committed by mistake, **do not just delete it in a new commit**: tell a maintainer, who will remove it from the history.

## Writing style

- Friendly, plain English. The reader is a pathology resident who has never written code.
- **Pathology first:** start from a slide, a diagnosis or a clinical question, then show the code.
- **Code before theory:** introduce a concept at the moment the learner needs it, not before.
- **Short cells:** a few sentences of markdown, then a code cell that does something visible.
- Comments in code explain *why*, in plain words.
- End with **Now try it yourself** (homework on new data, with a sharing step) and a checkpoint.
- Turkish (or other) notes may be added later; write the main text in English.

## Writing a new lesson

1. Copy `templates/lesson-template.ipynb` to `lessons/NN-name/lesson.ipynb`
   and `templates/checkpoint-template.md` to `lessons/NN-name/checkpoint.md`.
2. Fix the badge links in the first cell to point at the new path.
3. Keep the `# COMPPATH-SETUP` cell as the first code cell. Put exact package versions in its `PACKAGES` list
   and add them to `environment.txt`.
4. Make the lesson work in **smoke-test mode**: when `SMOKE_TEST` is true, use tiny (ideally synthetic) data
   and the smallest settings so it finishes on a CPU in a couple of minutes. See lesson 1 for an example.
5. Design for Kaggle's free tier: small curated subsets, pre-extracted patches, precomputed features. A lesson should use
   at most a couple of GPU hours of the weekly quota, including homework.
6. Run the checks locally:

   ```bash
   python tests/check_notebooks.py
   python tests/run_notebooks.py lessons/NN-name/lesson.ipynb
   ```
7. Run the lesson for real on Kaggle with a GPU before opening a pull request, and say in the pull request that you did.

## Pull requests

- One topic per pull request.
- The **Checks** workflow must pass. Pull requests that touch lessons also run the notebook tests.
- A maintainer reviews content for accuracy (pathology and code) before merging.
