---
title: "In vivo Perturb-seq"
aliases:
  - "Perturb-seq"
  - "in vivo CRISPR scRNA-seq"
  - "CRISPR-Cas9 scRNA screening"
  - "single-cell CRISPR screening in vivo"
  - "Perturb-seq dual-gRNA"
  - "scCRISPR-seq"
  - "perturbation single-cell sequencing"
  - "in vivo pooled CRISPR scRNA-seq"
  - "guide RNA scRNA-seq readout"
tags: [methods, crispr, single-cell, functional-genomics, immunology]
maturity: active
key_papers: [atlas-guided-discovery-transcription-factors-cell]
first_introduced: "2016"
date_updated: 2026-05-22
related_concepts: [taiji-tf-activity-pipeline]
---

## Definition

Pooled CRISPR-Cas9 screening assay in which each cell carries a barcoded gRNA recovered alongside its full transcriptome by droplet scRNA-seq. The in vivo variant transduces Cas9+ donor T cells with the gRNA library, transfers them into recipient animals (infected or tumour-bearing), and later sequences donor cells from target tissues so that perturbation effects are read out in the native immune environment.

## Intuition

Bulk CRISPR screens measure abundance only; Perturb-seq measures **state**: which transcriptional program a perturbed cell adopts. Combining a TF gRNA library with in vivo chronic and acute infection lets you ask, per TF, whether KO depletes a specific differentiation state (TEXterm) while sparing another (TRM).

## When to use

When you need to causally link a TF (or other gene) to a **specific transcriptional state** rather than to overall fitness, and the relevant state requires the native tissue or disease context.

## Known limitations

- Library complexity is limited by sequencing depth and gRNA recovery; dual-gRNA vectors (4 gRNAs/target as in Chung et al.) increase potency at the cost of throughput.
- KO efficacy varies across TFs and timepoints; partial KO can blunt phenotypes.
- Multiplexed analysis still requires careful UMAP cluster annotation and gScramble normalization.

## Key papers

- [[atlas-guided-discovery-transcription-factors-cell]] — Chung et al. 2025: in vivo Perturb-seq of 19 TF genes in chronic LCMV-Clone 13 and acute LCMV-Armstrong, 17,257 and 15,211 cells respectively.
