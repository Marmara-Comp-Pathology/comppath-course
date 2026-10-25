---
title: "Checkpoint 5: Data done right"
---

**Type:** ✅ **formal checkpoint**, assessed by a supervisor
**Prerequisite lessons:** 1 to 5

> **Draft.** These criteria will be finalised together with lesson 5.

## Task

You are asked to review a colleague's claim: *"Our patch classifier detects tumor with 99% accuracy."*
Using a dataset with patient identifiers (provided in the lesson), show how a patch-level random split inflates performance,
then redo the experiment properly and report honest results.

## Deliverables

1. A public Kaggle notebook that trains the same model twice: once with a **random patch-level split** and once with a **patient-level split**.
2. A results section with, for both splits: confusion matrix, sensitivity, specificity, AUC with a 95% confidence interval.
3. A one-page written answer to the colleague, in plain language, explaining the difference.

## Pass criteria

- [ ] The notebook runs from top to bottom on a fresh session without errors
- [ ] The patient-level split is verified in code: no patient appears in more than one of training, validation and test
- [ ] A separate **test set** is held back and used only once, at the end
- [ ] Sensitivity, specificity and AUC are reported for both splits, with confidence intervals for AUC (e.g. bootstrap)
- [ ] The difference between the two splits is explained correctly as data leakage
- [ ] The resident computes and interprets Cohen's kappa on a small agreement exercise (model versus pathologist, or two pathologists)
- [ ] The written answer is understandable by a clinician without a technical background

## Discussion questions

1. Name two other ways information can leak from the test set into training, apart from shared patients.
2. When is accuracy a misleading metric? Give a pathology example.
3. Why is the AUC of a patient-level split usually lower, and which number would you put in a paper?

## For supervisors

Common mistakes: splitting by slide when a patient has several slides; choosing the decision threshold on the test set;
reporting the validation set as the test set; confidence intervals computed per patch instead of per patient.
