---
title: "18_ECMMac proportion anticorrelates with MANA score (q=0.078) and 8_IFNGMac correlates with MANA score (q=0.060) in lung cancer"
slug: 18-ecmmac-anticorrelates-mana-score-lung
status: supported
confidence: 0.75
tags: [MANA-score,neoantigen,18_ECMMac,8_IFNGMac,lung-cancer,TAM-T-cell-crosstalk]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: medium
    detail: "Quote (p.7, Fig. 4c): 'We observed significantly higher proportions of 18_ECMMac in samples in the lower quartile of MANA scores compared to the upper quartile... 8_IFNGMac was significantly enriched in the upper quartile'."
conditions: "Lung secondary atlas: 7 studies, 31,598 macrophages + 72,585 T cells; MANA score via Seurat AddModuleScore with 14-gene CD8 signature; quartile comparison via Propeller with FDR correction. q-values 0.07801182 (18_ECMMac) and 0.05962064 (8_IFNGMac)."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

In lung cancer samples stratified by per-sample MANA (mutation-associated neoantigen) score in CD8 T cells, the 18_ECMMac proportion is enriched in low-MANA samples (Propeller q=0.078) while 8_IFNGMac is enriched in high-MANA samples (q=0.060), linking TAM compositional state to neoantigen-reactive T-cell activation.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4c).

## Conditions and scope

Lung secondary atlas only; effect is marginal (q just below 0.1 threshold) — should be treated as hypothesis-generating rather than definitive.

## Counter-evidence

q-values are above the strict 0.05 threshold; sample size per quartile not stratified by study or driver mutation.

## Linked ideas

## Open questions

- Replication in independent lung neoantigen-profiled cohorts.
- Whether MANA-TAM coupling generalizes beyond lung cancer.
