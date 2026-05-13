---
title: "Seurat RPCA outperforms Scanorama and ties Harmony on iLISI for pan-cancer TAM integration; Seurat CCA fails at 1.5 TB RAM"
slug: seurat-rpca-best-pan-tam-integration
status: supported
confidence: 0.85
tags: [Seurat,RPCA,Harmony,Scanorama,iLISI,integration,benchmark]
domain: computational-biology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (Methods): 'Seurat CCA failed to run successfully, and was therefore excluded from the iLISI comparison. Scanorama produced lower iLISI scores than the unintegrated data, whilst Harmony and Seurat RPCA performed similarly'."
conditions: "Single 1.5 TB RAM node; 363,315-cell TAM atlas; iLISI benchmark with SCT-normalized counts pre-integration."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

For pan-cancer TAM scRNA-seq integration (~363k cells, mixed platforms), Seurat RPCA and Harmony perform similarly on the iLISI integration metric and outperform Scanorama (which is *worse* than no integration). Seurat CCA failed to complete on a 1.5 TB RAM node.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Methods).

## Conditions and scope

Specific to TAM-only pan-cancer data at this scale and platform mix; iLISI is one of several integration metrics.

## Counter-evidence

Scanorama performance critique is dataset-specific; other benchmarks may favour Scanorama on smaller or more-homogeneous data.

## Linked ideas

## Open questions

- Comparison with newer deep-learning integration (scVI, scANVI) on the same dataset.
