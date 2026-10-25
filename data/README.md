# data

**Download scripts only. Never commit slides, patches or any patient data to this repository.**
`tests/check_notebooks.py` fails the build if slide files (`.svs`, `.ndpi`, `.mrxs`, DICOM, ...) or files over 5 MB appear.

## Where course data lives

| Copy | Role |
|---|---|
| **Zenodo** | Long-term master copy. Every curated subset gets a permanent DOI. |
| **Kaggle Datasets** | Convenience mirror that lessons attach on Kaggle (read-only, does not count against the 20 GB working disk). |
| **Hugging Face** | Second mirror, used by the Colab path. |

Lessons download their own data in a notebook cell. The scripts here are for maintainers
(building the curated subsets and mirrors) and for people running lessons on their own computer.

## Datasets by lesson

| Lesson | Dataset | Licence | Source |
|---|---|---|---|
| 1 | PatchCamelyon, Kaggle version (Histopathologic Cancer Detection) | CC0 | [Kaggle competition](https://www.kaggle.com/competitions/histopathologic-cancer-detection) |

Add a row for every new dataset, with its licence. Only use data whose licence allows redistribution
of the subset you publish.

## Departmental data (capstone)

Departmental slides never go into this repository. Before any slide leaves the institution it must be:

1. covered by ethics approval and compliant with the applicable data protection law,
2. anonymized: embedded **label and macro images** removed, **file metadata** (scan date, scanner serial number, original filename) scrubbed, file renamed,
3. uploaded only to a **private** Kaggle dataset shared with enrolled residents and supervisors.

See `lessons/11-capstone/checkpoint.md`.
