---
title: "Projection of Luoma 2022 oral cancer TAMs onto the pan-cancer atlas validates the reference-mapping utility; 18_ECMMac is absent in oral cancer"
slug: oral-cancer-tam-projection-validates-atlas
status: supported
confidence: 0.85
tags: [reference-mapping,projection,oral-cancer,validation,18_ECMMac]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.9, Fig. 5a-b): 'TAMs classified as C1QB+ TAMs by the authors primarily mapped to our 2_C3Mac cluster... CXCL8+ TAM mapped to 6_SPP1AREGMac and SPP1+ TAMs mapped to 16_ECMHomeoMac... There were no 18_ECMMac TAMs detected in the oral cancer dataset'."
conditions: "Seurat native reference mapping; PCA structure of the integrated atlas projected onto the Luoma 2022 oral cancer query dataset."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Projection of an external oral-cancer scRNAseq dataset (Luoma et al. 2022) onto the pan-cancer TAM atlas via Seurat reference mapping yields a stable, interpretable cluster correspondence (C1QB+ → 2_C3Mac; CD14+ Mono → 19_ClassMono; CXCL8+ TAM → 6_SPP1AREGMac; SPP1+ TAM → 16_ECMHomeoMac), and reveals that 18_ECMMac is absent in oral cancer — indicating cancer-type-specific TAM differentiation programmes.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 5a-b).

## Conditions and scope

Single query dataset; sub-cluster mapping at the higher resolution of the atlas reveals biology not visible at the original author resolution (e.g., CD14+ Mono partially maps to 9_AngioMac).

## Counter-evidence

None within paper's scope.

## Linked ideas

## Open questions

- Why is 18_ECMMac absent in oral cancer? Tumour-cell-intrinsic, stromal-context, or sampling artefact?
- Performance on other cancer types (lung driver-stratified, sarcoma, glioma).
