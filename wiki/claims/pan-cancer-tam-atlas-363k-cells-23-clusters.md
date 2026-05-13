---
title: "Pan-cancer TAM atlas integrates 363,315 cells from 32 studies and 17 cancer types into 23 Louvain clusters"
slug: pan-cancer-tam-atlas-363k-cells-23-clusters
status: supported
confidence: 0.95
tags: [TAM,scRNA-seq,pan-cancer,atlas,clustering,Seurat]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.1-2): 'The total dataset includes 363,315 TAMs or macrophage-like cells (i.e. monocytes)... resulting in 23 clusters in total, visualized as a 2-dimensional UMAP'."
conditions: "Seurat v4.2.0; SCT normalization; RPCA integration; Louvain clustering at tuned resolution; 32 input studies obtained via literature + GEO search; mixed 10x Genomics / MARS-seq / GEXSCOPE / In-Drop / Smart-Seq2 + 2 snRNAseq studies."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Coulton et al. (Nat Commun 2024) integrate 32 published scRNA-seq studies covering 17 human cancer types into a TAM-only atlas of 363,315 macrophages/monocytes (279,104 tumour, 74,982 adjacent normal, 9,229 other), clustered into 23 Louvain clusters after Seurat RPCA integration.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024); cluster counts cross-checked against Fig. 1c and Fig. 2a-b.

## Conditions and scope

Pan-cancer human TAMs; clustering resolution tuned heuristically; 23 clusters reflect both established subsets (alveolar, IFN, proliferating, M2-like) and previously-undescribed states.

## Counter-evidence

None within paper's scope. Alternative atlases (Cheng 2021, Nieto 2021, Mulder 2021) use different scopes and produce different cluster counts — not directly comparable.

## Linked ideas

## Open questions

- Cluster identity stability under different resolution / integration choices.
