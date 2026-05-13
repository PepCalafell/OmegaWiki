---
title: "Nearest-neighbour analysis shows 18_ECMMac TAMs neighbour fibroblasts while 8_IFNGMac TAMs neighbour CD4/CD8 memory T cells"
slug: ecmmac-fibroblast-ifngmac-tcell-spatial-neighbors
status: supported
confidence: 0.85
tags: [spatial,nearest-neighbor,18_ECMMac,8_IFNGMac,fibroblast,T-cell,CosMx]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: medium
    detail: "Quote (p.7, Fig. 4e): 'the closest neighbouring cells to 18_ECMMac+ TAMs were other TAMs followed by fibroblasts... the closest neighbours to 8_IFNGMac TAMs were other TAMs, followed by CD4 memory T cells, cancer cells and CD8 memory T cells'."
conditions: "CosMx FFPE NSCLC dataset (5 samples, 771,236 cells); RANN v2.6.1 nearest-neighbour; UCell threshold-based cluster assignment."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

In CosMx spatial transcriptomics of 5 NSCLC tumours, 18_ECMMac+ TAMs are most often adjacent to other TAMs followed by fibroblasts; 8_IFNGMac TAMs are most often adjacent to other TAMs followed by CD4 memory T cells, cancer cells, and CD8 memory T cells. The contrast supports cluster-specific functional niches: ECM-modifying TAM-fibroblast crosstalk vs IFN-γ-driven TAM-T cell crosstalk.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4e).

## Conditions and scope

5 NSCLC samples; transcript-level cluster assignment; cellular boundaries from CosMx segmentation.

## Counter-evidence

Nearest-neighbour proximity does not establish functional interaction.

## Linked ideas

## Open questions

- Cell-cell-communication inference (CellChat/CellPhoneDB) restricted to spatial neighbours.
