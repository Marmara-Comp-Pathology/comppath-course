---
title: "Checkpoint 1: Your first model"
---

**Type:** self-check (no supervisor sign-off needed)
**Prerequisite lessons:** none

Use this list to check that you got everything out of lesson 1 before moving on. If you cannot tick a box, go back to the matching step of the notebook.

## Task

Train the lesson 1 tumor-versus-normal patch classifier, run the experiments in the homework, and review the model's mistakes as a pathologist.

## Deliverables

1. Your copy of the lesson 1 notebook, **public** on Kaggle, with all cells run and outputs visible.
2. At the end of the notebook, a markdown cell with:
   - the results table from the homework (at least four runs),
   - your comments on three top-loss patches,
   - one paragraph on a task in your own department where a patch classifier could help.
3. The link, posted to your cohort.

## Pass criteria

- [ ] The notebook runs from top to bottom on a fresh session without errors
- [ ] The default run reaches a validation AUC of at least 0.90
- [ ] The results table has at least four runs, changing **one** setting at a time, and includes training time
- [ ] You can explain in one sentence each: training set, validation set, epoch, sensitivity, specificity
- [ ] For each of your three top-loss patches you state whether you agree with the label, the model, or neither, and why
- [ ] You can explain why the reported numbers are probably too optimistic (patches from the same patient in both training and validation)
- [ ] The notebook is public and the link is shared

## Discussion questions

1. Which setting changed the results most? Which changed the training time most? Was it worth it?
2. "Normal" in this dataset means "no tumor in the central 32 × 32 pixels". How might this definition create label errors?
3. If this model screened sentinel lymph nodes, would you rather tune it for higher sensitivity or higher specificity? What would happen to the other?
