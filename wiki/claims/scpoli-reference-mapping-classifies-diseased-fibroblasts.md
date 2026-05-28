---
title: "scPoli reference mapping assigned 121,167/190,756 diseased fibroblasts to F1–F5; 69,589 uncertain cells revealed novel disease states"
slug: scpoli-reference-mapping-classifies-diseased-fibroblasts
status: supported
confidence: 0.8
tags: [skin, fibroblast, scpoli, reference-mapping, disease]
domain: methods
source_papers:
  - single-cell-spatial-genomics-atlas-human
evidence:
  - source: single-cell-spatial-genomics-atlas-human
    type: supports
    strength: strong
    detail: "Of 190,756 diseased fibroblasts, 121,167 confidently assigned F1–F5; 69,589 flagged uncertain by scPoli and re-clustered into two disease-adapted and three disease-specific subtypes."
conditions: "Diseased human skin fibroblasts mapped to healthy reference."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Using scPoli to map diseased fibroblasts onto the healthy F1–F5 reference, 121,167 of 190,756 cells were confidently labeled, and the 69,589 uncertain cells resolved into disease-adapted (F1-like, F3-like) and disease-specific (F6, F7, F8) subtypes.

## Evidence summary

scPoli uncertainty mechanism + manual re-annotation by DE and pathway analysis (Fig. 3b; Extended Data Fig. 5).

## Conditions and scope

Depends on scPoli uncertainty thresholds.

## Counter-evidence

Authors note reliance on scPoli's uncertainty mechanism as a limitation.

## Linked ideas

## Open questions

Robustness of uncertain-cell discovery across reference choices.
