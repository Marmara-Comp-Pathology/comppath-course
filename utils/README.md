# utils

Shared helper code for maintainers, CI and people running lessons locally.

Lesson notebooks must stay self-contained: on Kaggle and Colab a learner opens a
single notebook, not the whole repository, so notebooks cannot `import utils`.
Instead, each lesson's setup cell (marked `# COMPPATH-SETUP`) carries a short copy
of `env.py`. When you change `env.py`, update the setup cell in every lesson and in
`templates/lesson-template.ipynb`.
