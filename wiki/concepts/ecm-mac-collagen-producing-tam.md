---
title: "ECM macrophage (18_ECMMac) — collagen-producing TAM associated with ICI resistance"
aliases:
  - "18_ECMMac"
  - "ECMMac"
  - "ECM macrophage"
  - "ECM-modifying TAM"
  - "collagen-producing macrophage"
  - "collagen-producing TAM"
  - "COL1A1+ macrophage"
  - "fibroblast-like macrophage"
  - "macrophage-to-myofibroblast intermediate"
  - "collagen TAM ICI resistance"
  - "ECM-remodelling tumour-associated macrophage"
  - "Coulton 18_ECMMac cluster"
tags:
  - TAM
  - 18_ECMMac
  - collagen
  - ECM
  - macrophage-fibroblast
  - ICI-resistance
  - biomarker
maturity: emerging
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
  - pd-l1-expressing-tumor-associated-macrophages
  - tumour-microenvironment-crosstalk-nsclc-progression-response
  - spatiotemporal-analyses-pan-cancer-single-cell
first_introduced: "Coulton et al. 2024 *Nature Communications* (operationalization as a discrete cluster); analogous PD-L1−/lo ECM-FA TAM phenotype in Wang L 2024 Cell Reports Medicine (breast cancer)"
date_updated: 2026-05-13
related_concepts:
  - pan-cancer-tam-atlas-23-clusters
  - tumor-associated-macrophage-immunosuppression
  - macrophage-induced-emt-tumor-invasiveness
  - m1-m2-polarization-paradigm
  - trm-bmdm-tissue-repair-fibrosis-dichotomy
  - pd-l1-immunostimulatory-tam-phenotype
---

## Definition

18_ECMMac is a tumour-associated macrophage cluster — first explicitly resolved in the Coulton 2024 pan-cancer scRNAseq atlas — defined by high co-expression of macrophage markers (CD68) with collagen genes (COL1A1, COL1A2, COL3A1) and other ECM components. The cluster is interpreted by the authors as an intermediate state on a TAM → myofibroblast differentiation trajectory and is enriched in ICI non-responders in the CPI1000+ bulk RNAseq cohort.

## Distinguishing features

- **Marker genes**: COL1A1, COL1A2, COL3A1, FN1; co-expressed with macrophage marker CD68.
- **Tumour context**: ccRCC (28.2%) > HGSOC (15.4%) > CRC (14.9%); absent in oral cancer.
- **ICI association**: enriched in non-responders (fgsea q=3.8e-5 in CPI1000+).
- **Spatial neighbours**: other TAMs followed by fibroblasts (CosMx FFPE NSCLC).
- **Not via T-cell exclusion**: T-cell signature is higher (not lower) in high-ECM CPI1000+ samples (Mann-Whitney p<0.0001).

## Mechanistic hypotheses

- **TAM → myofibroblast differentiation**: 18_ECMMac may represent an intermediate cell state during macrophage transdifferentiation toward a myofibroblast / CAF-like identity (Coulton 2024 invokes ref 105).
- **TAM-fibroblast crosstalk niche**: collagen-secreting TAMs may form a self-reinforcing ECM niche with stromal fibroblasts, restricting CD8 T cell function — analogous to the breast cancer report of collagen-producing macrophages limiting CD8 (ref 106 in Coulton 2024).
- **Cancer-type-specific induction**: certain tumour types (ccRCC, lung, CRC liver met) provide environmental cues that promote this differentiation pathway, while others (oral cancer) do not.

## Validity / limitations

- Collagen signature overlaps fibroblasts; bulk-RNAseq attribution to TAMs requires single-cell or spatial confirmation.
- Causal role in ICI resistance is associative; perturbation data lacking.
- The PD-L1−/lo TAM phenotype described in Wang L 2024 (breast cancer) shows a similar gene signature (SPP1, MMP9, FN1, COL1A1/2, COL3A1) — likely overlapping populations across atlases.

## When to use / look for

- Bulk-RNAseq stratification of ICI-treated patients: high 18_ECMMac signature predicts poor response.
- Single-cell or spatial validation of TAM-fibroblast niches in ccRCC, HGSOC, CRC, and lung tumours.
- Mechanistic studies of macrophage-to-myofibroblast transdifferentiation.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. First discrete-cluster definition and ICI-resistance association.
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — Wang et al. 2024. PD-L1−/lo TAM phenotype with overlapping ECM/collagen signature in breast cancer.
