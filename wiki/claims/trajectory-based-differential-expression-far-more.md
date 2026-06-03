---
title: "Trajectory-based DE is far more reproducible across AD cohorts than case-control (83% vs 17%)"
slug: trajectory-based-differential-expression-far-more
status: supported
confidence: 0.85
tags: [Alzheimer, reproducibility, differential-expression, benchmark]
domain: neuroscience
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Trajectory-associated DEGs replicated across SEA-AD and Psych-AD at 82.8%, versus 17% for binary case-control DE; cell-type prioritization also reproduced (Pearson r=0.73, p=1.82e-3)."
conditions: "Two independent AD snRNA-seq cohorts."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Differential-expression genes identified along the scSLIDE Alzheimer trajectory replicate across the SEA-AD and Psych-AD cohorts at 82.8%, compared with only 17% for binary case-control DE — a roughly fivefold improvement in cross-cohort reproducibility.

## Evidence summary

Figure 3a and Figure 4i of [[reconstructing-developmental-disease-progression-sample-level]]; cell-type prioritization across cohorts also correlated at r=0.73 (p=1.82e-3).

## Conditions and scope

Cross-cohort replication between two AD snRNA-seq datasets.

## Counter-evidence

None reported; this is the headline quantitative result for the AD use case.

## Linked ideas

Quantitative contrast against [[alzheimer-case-control-differential-expression-replicates]]; strongest reproducibility evidence for [[continuous-disease-progression-modeling]].

## Open questions

Does the reproducibility advantage persist across cohorts profiled on different platforms or brain regions?
