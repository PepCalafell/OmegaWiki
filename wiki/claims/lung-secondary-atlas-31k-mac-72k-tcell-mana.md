---
title: "A 7-study lung secondary atlas of 31,598 macrophages and 72,585 T cells enables per-sample MANA-score stratification of TAM composition"
slug: lung-secondary-atlas-31k-mac-72k-tcell-mana
status: supported
confidence: 0.9
tags: [lung-cancer,scRNA-seq,atlas,MANA-score,TAM,T-cell,methodological]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (Methods): 'we combined a second, smaller atlas of lung cancers from 7 studies, consisting of 31598 macrophages and 72585 T cells'."
conditions: "7 lung studies (refs 25, 30, 35, 39, 41, 48); MANA scores per CD8 T cell via Seurat AddModuleScore on the 14-gene MANA signature."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

To investigate TAM-T cell crosstalk in the context of neoantigen response, the authors assemble a secondary lung-only atlas of 31,598 macrophages and 72,585 T cells from 7 studies, enabling per-sample stratification by MANA score quartile.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Methods).

## Conditions and scope

Lung-only; auxiliary to the main 363k-cell atlas.

## Counter-evidence

None within paper's scope.

## Linked ideas

## Open questions

- Generalize the secondary-atlas construction to other tumour types with neoantigen profiling.
