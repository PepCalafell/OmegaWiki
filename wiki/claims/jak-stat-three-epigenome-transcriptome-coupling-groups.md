---
title: "JAK-STAT mutants partition into three epigenome–transcriptome coupling groups in homeostatic immune cells"
slug: jak-stat-three-epigenome-transcriptome-coupling-groups
status: supported
confidence: 0.8
tags: [atac-seq, rna-seq, jak-stat, epigenome, transcriptome-coupling, gene-regulatory-classification]
domain: immunology
source_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
evidence:
  - source: jak-stat-signaling-maintains-homeostasis-cells
    type: supports
    strength: strong
    detail: "Fig. 5d: across all 12 mutants × 2 cell types, percentage of DE genes, percentage of differentially accessible regions, and Pearson correlation between log2FCs in expression and promoter accessibility yields three qualitatively distinct groups."
conditions: "Mouse spleen CD8+ T cells and macrophages."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

JAK-STAT mutant–WT comparisons across homeostatic CD8+ T cells and macrophages stratify into three groups based on epigenome and transcriptome effect sizes and their correlation:
- **Group 1** (low/low): Stat1, Stat1a-only, Stat1b-only, Stat4 (both cell types), Stat6 in T, Tyk2-K923E in T — <2.5% DA regions, <4.5% DE genes, Pearson r < 0.2.
- **Group 2** (high transcript / low epigenome): Stat2, Stat3, Irf9 (both cell types) — many DE genes but few epigenome changes, low correlation.
- **Group 3** (strong epigenome, stronger correlation): Stat5-hyp in T, Stat5, Stat6 in Mac, Tyk2 in both, Tyk2-K923E in Mac — >2.5% DA regions, often >4.5% DE genes, higher correlation between transcript and accessibility changes.
