---
title: "3CA v2 defines 67 recurrent malignant metaprograms (vs 41 previously)"
slug: cca3-67-malignant-metaprograms-updated
status: supported
confidence: 0.9
tags: [metaprograms, nmf, malignant, scrna-seq, pan-cancer]
domain: oncology
source_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
evidence:
  - source: curated-cancer-cell-atlas-provides-comprehensive
    type: supports
    strength: strong
    detail: "Per-sample NMF over 124 datasets with within- and cross-tumour robustness filtering yields 67 final malignant MPs."
conditions: "Pipeline parameters (K range 4–9, robustness thresholds) influence the exact count."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Applying robust NMF to malignant cells across the 124-dataset 3CA v2 cohort recovers 67 recurrent metaprograms, expanded from the 41 reported in 3CA v1.

## Evidence summary

Programmatic NMF + cross-tumour Jaccard clustering with explicit filtering yields the count.

## Conditions and scope

Counts assume the published pipeline; alternative robustness thresholds would shift the count.

## Counter-evidence

None.

## Linked ideas

—

## Open questions

- Will further expansion of the atlas continue to yield new MPs or saturate?
