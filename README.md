# Marmara Computational Pathology Starter Pack

*From Zero to Hero*

A free, open course in digital and computational pathology for pathology residents
with no coding background, inspired by fast.ai's *Practical Deep Learning for Coders*.

Made by the Marmara Pathology Community.

> **Disclaimer.** An independent, volunteer project of the Marmara Pathology Community, an informal group. It is not an official course of any university, hospital or other institution, and is not endorsed by one.
> The course is for education only: nothing in it is medical advice, and no model built here may be used on patients.

- 📖 **Read the course:** https://marmara-comp-pathology.github.io/comppath-course
- ▶️ **Start here:** [Lesson 1: Your first model](lessons/01-first-model/lesson.ipynb). Open it on Kaggle with the badge at the top.

## How the course works

- **Whole game first.** Lesson 1 trains a working model before explaining anything.
- **Notebooks are the textbook.** Each lesson is one Jupyter notebook that runs on Kaggle (primary) or Google Colab (fallback).
- **Now do it on your own data.** Every lesson ends with homework, shared publicly as a portfolio.
- **Competence, not calendar.** Lessons 5, 9 and 11 end with formal checkpoints.

| # | Lesson | Status |
|---|--------|--------|
| 1 | [Your first model](lessons/01-first-model/lesson.ipynb) | ✅ ready |
| 2 | [Inside a digital slide](lessons/02-inside-a-slide/lesson.ipynb) | 🚧 |
| 3 | [Just enough Python](lessons/03-just-enough-python/lesson.ipynb) | 🚧 |
| 4 | [Tiling a slide](lessons/04-tiling-a-slide/lesson.ipynb) | 🚧 |
| 5 | [Data done right](lessons/05-data-done-right/lesson.ipynb) ✅ checkpoint | 🚧 |
| 6 | [Stain variation and augmentation](lessons/06-stain-and-augmentation/lesson.ipynb) | 🚧 |
| 7 | [Segmentation](lessons/07-segmentation/lesson.ipynb) | 🚧 |
| 8 | [Foundation models](lessons/08-foundation-models/lesson.ipynb) | 🚧 |
| 9 | [Slide-level prediction](lessons/09-slide-level-prediction/lesson.ipynb) ✅ checkpoint | 🚧 |
| 10 | [Trust](lessons/10-trust/lesson.ipynb) | 🚧 |
| 11 | [Capstone](lessons/11-capstone/lesson.ipynb) ✅ final checkpoint | 🚧 |

## Repository layout

```
lessons/NN-name/lesson.ipynb    the lesson (the textbook)
lessons/NN-name/checkpoint.md   task, deliverables and pass criteria
templates/                      starting points for new lessons and checkpoints
data/                           download scripts only, never slides or patient data
utils/                          shared helpers (environment detection)
tests/                          static checks and the smoke-test runner
tools/                          maintenance scripts
_quarto.yml, *.qmd              the course website
environment.txt                 pinned package versions
```

## Contributing and maintaining

See [CONTRIBUTING.md](CONTRIBUTING.md) and [MAINTAINERS.md](MAINTAINERS.md).

## Licence

Text: [CC BY 4.0](LICENSE-content). Code: [MIT](LICENSE). Datasets keep their own licences.
