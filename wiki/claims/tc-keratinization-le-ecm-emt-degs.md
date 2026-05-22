---
title: "TC is enriched for keratinization programs; LE is enriched for ECM and EMT initiation"
slug: tc-keratinization-le-ecm-emt-degs
status: supported
confidence: 0.85
tags: [DEG, keratinization, ECM, EMT, OSCC]
domain: oncology/spatial-transcriptomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "TC top DEGs include SPRR2D, SPRR2E, SPRR2A, DEFB4A, LCN2 (keratinization, EMT inhibition); LE top DEGs include COL1A1, FN1, COL1A2, TIMP1, COL6A2, LAMC2, ITGA5 (ECM, p-EMT); transitory cluster mixes both."
conditions: "Two-sided Wilcoxon rank sum with Bonferroni correction; logFC>0.25; adj. p<0.001"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The OSCC TC differentially upregulates keratinization and epithelial-differentiation genes (SPRR2D/E/A, CRCT1, CNFN, SPRR1A, CLDN4, SPRR1B); the LE differentially upregulates ECM/collagen remodelling (COL1A1, COL1A2, FN1, TIMP1, LAMC2, ITGA5) and EMT-initiation genes (MT2A, NME2, IFITM3).

## Evidence summary
Consensus DGEA plot of top 25 DEGs differentially expressed in >9/12 samples; functional annotation maps each gene to keratinization, ECM remodelling or EMT.

## Conditions and scope
HPV-negative OSCC, ST spot-level DGEA across malignant spots.

## Counter-evidence
Only 40 epithelial-differentiation DEGs and 7 p-EMT DEGs overlap with the Puram et al. 2017 HNSCC scRNA-seq study — the rest of the LE signature is novel relative to prior work.

## Linked ideas

## Open questions
Whether the TC/LE DEG split persists at single-cell resolution within Visium spots.
