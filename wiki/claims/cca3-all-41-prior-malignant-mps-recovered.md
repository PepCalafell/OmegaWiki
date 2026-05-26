---
title: "All 41 prior malignant metaprograms (3CA v1) are recovered in 3CA v2"
slug: cca3-all-41-prior-malignant-mps-recovered
status: supported
confidence: 0.9
tags: [metaprograms, reproducibility, malignant, nmf, scrna-seq]
domain: oncology
source_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
evidence:
  - source: curated-cancer-cell-atlas-provides-comprehensive
    type: supports
    strength: strong
    detail: "Updated MP set explicitly captures all 41 v1 MPs, supporting the framework's robustness."
conditions: "Recovery defined by Jaccard overlap above the clustering threshold."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The updated 67-MP set recovered every one of the 41 malignant metaprograms identified in the original 3CA v1 / Gavish et al. 2023 release, indicating that the recurrent-MP framework is stable to ~2x dataset expansion.

## Evidence summary

Stated directly in the paper (Fig. 3b).

## Conditions and scope

Concordance is at the gene-overlap level; gene rankings within MPs may have shifted.

## Counter-evidence

None reported.

## Linked ideas

—

## Open questions

- Will MPs remain stable as additional cancer types and snRNA-seq cohorts are added?
