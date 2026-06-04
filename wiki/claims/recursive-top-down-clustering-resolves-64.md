---
title: "Recursive top-down clustering resolves 64 circulating immune populations"
slug: recursive-top-down-clustering-resolves-64
status: supported
confidence: 0.9
tags:
  - cell-annotation
  - clustering
  - immune-populations
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: strong
    detail: "From the joint scANVI embedding, cells were assigned to major lineages (Level 1) then via recursive top-down clustering to 64 immune populations (Level 2) spanning innate and adaptive compartments."
conditions: "Two-level hierarchical annotation (Level 1 lineages, Level 2 states)."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

A recursive, top-down clustering of the integrated embedding produced two annotation levels: major immune lineages (Level 1) and a total of 64 fine-grained immune populations (Level 2) covering innate and adaptive compartments.

## Evidence summary

Reported at p.634 with the Level 1/Level 2 annotation (Fig. 1c,d; Supplementary Table 3). High-level compositional analysis recapitulated known disease alterations (e.g. SLE, IBD, RA, sepsis lymphopenia, HIV lymphocytosis).

## Conditions and scope

Annotation depends on integration quality and marker curation; population count is dataset-specific.

## Counter-evidence

None internal; cluster granularity is a methodological choice.

## Linked ideas

- [[concepts/inflammation-atlas-circulating-immune-cells]]

## Open questions

- Stability of the 64-population definition across chemistries and centers.
