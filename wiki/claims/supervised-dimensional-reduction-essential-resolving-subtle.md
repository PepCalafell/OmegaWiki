---
title: "Supervised dimensional reduction is essential for resolving subtle disease phenotypes but unnecessary for strong temporal signals"
slug: supervised-dimensional-reduction-essential-resolving-subtle
status: supported
confidence: 0.8
tags: [scSLIDE, supervision, PLS, severity, development]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "An unsupervised scSLIDE variant failed to recover the AD severity trajectory, but recovered a nearly identical trajectory in zebrafish where temporal phenotype is strong; supervision was essential only for subtle phenotypes."
conditions: "Contrast between AD severity (subtle) and zebrafish development (strong) phenotypes."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Supervision via PLS is essential when the phenotype of interest is subtle and reflects only a small fraction of the transcriptome (e.g. Alzheimer severity), but unnecessary when the phenotype dominates transcriptional variation (e.g. zebrafish developmental time), where unsupervised scSLIDE recovers the same trajectory.

## Evidence summary

Benchmarking and zebrafish sections of [[reconstructing-developmental-disease-progression-sample-level]]: unsupervised scSLIDE failed on AD severity but matched supervised results on development.

## Conditions and scope

Depends on the strength of the phenotype's transcriptional footprint.

## Counter-evidence

The two regimes are not in conflict — they delineate when supervision helps.

## Linked ideas

Design justification for [[scslide-builds-semi-supervised-cell-embedding]]; informed by [[scslide-outperforms-existing-sample-level-embedding]].

## Open questions

Is there a quantitative threshold on phenotype "strength" that predicts when supervision is needed?
