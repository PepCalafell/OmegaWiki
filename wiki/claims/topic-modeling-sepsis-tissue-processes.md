---
title: "Grade-of-membership topic modeling (k=16) on whole-tissue RNA-seq separates baseline tissue identity from sepsis-driven cross-tissue processes"
slug: topic-modeling-sepsis-tissue-processes
status: supported
confidence: 0.85
tags:
  - methods
  - topic-model
  - sepsis
  - bulk-RNA-seq
domain: bioinformatics / unsupervised modeling
source_papers:
  - pairwise-cytokine-code-explains-organism-wide
evidence:
  - source: pairwise-cytokine-code-explains-organism-wide
    type: supports
    strength: strong
    detail: "k=16 GoM fit to 364 whole-tissue samples produced tissue-identity topics (k4 SI, k7 lung, k15 heart) and sepsis topics (k1 granulocyte PBMC, k6 liver acute phase, k9 ISG cross-tissue, k13 splenic/lung neutrophil)."
conditions: "Mouse, sublethal LPS, 364 bulk tissue RNA-seq samples × 13 tissues × 6 timepoints."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

A grade-of-membership topic model with k=16 topics fit to organism-wide LPS time-course RNA-seq disentangles baseline tissue-identity topics from sepsis-induced cross-tissue topics, providing an interpretable summary of organ-wide sepsis dynamics.
