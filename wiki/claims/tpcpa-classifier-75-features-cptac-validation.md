---
title: "TPCPA 75-feature cancer-type classifier achieves AUC 0.998 on CPTAC renal and AUC 0.992 on independent breast DIA-MS data"
slug: tpcpa-classifier-75-features-cptac-validation
status: supported
confidence: 0.85
tags: [cup-classifier, dia-ms, cptac, breast-cancer, kidney-cancer, machine-learning]
domain: methods
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: strong
    detail: "75-feature multi-cancer classifier (derived from top 25 per cancer of 17 solid types) achieves AUC 0.998 on CPTAC renal cancer data (ref 78) and AUC 0.992 on an independent DIA breast cancer dataset (ref 79)."
conditions: "Features re-processed with TPCPA pipeline; external proteomes from different acquisition workflows."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
A 75-protein cancer-type classifier trained on TPCPA generalises to external proteomic datasets, achieving AUC 0.998 on CPTAC renal cancers and AUC 0.992 on an independent DIA breast cancer cohort — establishing the feasibility of single-shot DIA-MS for protein-based primary-tumor classification.

## Evidence summary
- Knol et al. 2025 Figure 6D.
- External CPTAC renal and DIA breast datasets.

## Conditions and scope
- 17 solid cancer types; non-solid not included in this validation set.
- Test-set features included in training; authors note possible mild overfitting.

## Counter-evidence
- The training/test split is not strictly held-out at the feature-selection level.

## Linked ideas

## Open questions
- Does the classifier remain accurate on non-DIA proteomes (e.g., TMT-based)?
