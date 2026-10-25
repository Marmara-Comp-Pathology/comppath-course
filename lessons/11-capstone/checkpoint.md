---
title: "Final checkpoint: Capstone"
---

**Type:** ✅ **final checkpoint**, assessed by a supervisor and one external reviewer
**Prerequisite lessons:** 1 to 10, including the formal checkpoints of lessons 5 and 9

> **Draft.** These criteria will be finalised together with lesson 11.

## Task

Design and carry out your own computational pathology project on **anonymized** slides from your department,
and write it up as an abstract for a national or international pathology congress.

## Deliverables

1. A one-page **project proposal**, approved by your supervisor before you start: clinical question, data, labels, primary metric, expected sample size.
2. Proof that the project is covered by **ethics committee approval** and complies with the applicable **data protection law** (for example the GDPR or its national equivalent).
3. An **anonymization log**: for every slide, confirmation that the label and macro images were removed, file metadata (scan date, scanner serial number, original filename) was scrubbed, and the file was renamed. The key linking new names to patients stays inside the institution.
4. A repository or Kaggle notebook with all code. Data stays in a **private** Kaggle dataset shared only with enrolled residents and supervisors, unless a public release has been approved.
5. A congress **abstract** (within the congress word limit), and optionally a poster.

## Pass criteria

- [ ] The proposal was approved before data collection started
- [ ] Ethics approval and data protection compliance are documented
- [ ] No identifiable patient data has left the institution; the anonymization log is complete and spot-checked by the supervisor
- [ ] Splits are by patient and a held-out test set is used only once
- [ ] Results include the primary metric with a confidence interval and a comparison with a sensible baseline or with pathologists
- [ ] Limitations, possible biases and the intended clinical use are stated (see lesson 10)
- [ ] The code runs from top to bottom and reproduces the reported numbers
- [ ] The abstract is ready for submission and approved by the supervisor

## Discussion questions

1. What would it take for your model to be used on real patients? Which regulatory class would it fall under?
2. What would you do differently with ten times more data, or with data from another hospital?
3. Which part of your result are you least sure about, and how would you test it?

## For supervisors

Assess the quality of the question and the honesty of the evaluation, not the size of the number.
A negative or modest result, well designed and clearly reported, passes.
