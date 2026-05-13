---
title: "Cluster 8_IFNGMac is defined by CXCL9/CXCL10/MMP9/VAMP5 upregulation, consistent with an IFN-γ-driven T-cell-recruiting TAM phenotype"
slug: 8-ifngmac-cxcl9-cxcl10-tcell-recruiting
status: supported
confidence: 0.9
tags: [TAM,8_IFNGMac,CXCL9,CXCL10,IFN-gamma,T-cell-recruitment]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.2): 'Top upregulated genes in cluster 8 include CXCL9, CXCL10, MMP9, which is required for ECM remodeling... VAMP5, which is an interferon-induced gene'."
conditions: "Atlas DEGs from FindMarkers (Seurat). CXCL9 is the most highly upregulated gene; T-cell recruitment role inferred from prior literature (ref 97)."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

8_IFNGMac is a TAM cluster defined by IFN-γ-driven chemokines CXCL9 and CXCL10, MMP9 (ECM remodelling), and the interferon-induced gene VAMP5 — a phenotype consistent with T-cell recruitment to tumours.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 2c). Spatial nearest-neighbour validation: 8_IFNGMac neighbours other TAMs, then CD4/CD8 memory T cells (Fig. 4e) — see [[claims/ecmmac-fibroblast-ifngmac-tcell-spatial-neighbors]].

## Conditions and scope

Pan-cancer TAMs; cluster signature derived from RPCA-integrated 23-cluster atlas.

## Counter-evidence

None within paper's scope.

## Linked ideas

## Open questions

- Direct functional validation of T-cell recruitment by 8_IFNGMac TAMs (e.g., transwell migration, in vivo perturbation) is not performed.
