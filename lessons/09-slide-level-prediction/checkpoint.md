---
title: "Checkpoint 9: Slide-level prediction"
---

**Type:** ✅ **formal checkpoint**, assessed by a supervisor
**Prerequisite lessons:** 1 to 9

> **Draft.** These criteria will be finalised together with lesson 9.

## Task

Build a model that predicts the ISUP grade group of a prostate core biopsy from the whole slide,
using the **precomputed** foundation-model features for the PANDA dataset provided in the lesson.
Compare it with a simple baseline and explain where it fails.

## Deliverables

1. A public Kaggle notebook that trains an attention-based multiple instance learning (MIL) model on the precomputed features.
2. A comparison with a baseline (for example, mean pooling of patch features with logistic regression).
3. Attention heatmaps for at least four slides (correct and incorrect), with your morphological interpretation.
4. A one-page summary of the method and results, written like the *Methods* and *Results* sections of an abstract.

## Pass criteria

- [ ] The notebook runs from top to bottom on a fresh session without errors and stays within Kaggle's free GPU quota
- [ ] Splits are by patient and the data provider (Radboud and Karolinska) is reported for each split
- [ ] Performance is reported as quadratic weighted kappa with a confidence interval, plus a confusion matrix of grade groups
- [ ] The MIL model is compared with the baseline on the same test set
- [ ] Results are reported separately for each data provider, and any difference is discussed
- [ ] Attention heatmaps are interpreted in terms of Gleason patterns, including at least one case where the model attends to the wrong region
- [ ] The resident explains, without notes, what "multiple instance learning" means and why it suits slide-level labels

## Discussion questions

1. PANDA labels come from different sources at each centre. How could this affect your model?
2. Which confusions between grade groups are clinically most important, and does kappa capture that?
3. Why do we use precomputed features rather than training the patch encoder end to end?

## For supervisors

A strong submission discusses label noise and centre effects honestly rather than chasing the highest kappa.
Heatmaps should be checked by a pathologist: the resident should not over-interpret attention as explanation (see lesson 10).
