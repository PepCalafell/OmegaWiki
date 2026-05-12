---
title: "PD-L1 and SIGLEC15 are mutually exclusively expressed in human breast TAMs, enabling cluster-level dichotomization in scRNA-seq"
slug: pd-l1-siglec15-mutually-exclusive-tam-scrnaseq
status: supported
confidence: 0.85
tags:
  - PD-L1
  - SIGLEC15
  - scRNA-seq
  - TAM
  - methodological
  - breast-cancer
domain: "immunology / scRNA-seq methodology"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 1B-D, S1F: blend UMAP of PD-L1 and SIGLEC15 across 8 TAM clusters (n=2220 cells, luminal n=4) shows mutually exclusive pattern; dichotomization yields PD-L1+SIGLEC15− (39.4–73.5%) vs PD-L1−SIGLEC15+ (26.5–60.6%). Replicated in Pal 2021 TNBC scRNA-seq (n=4484 TAMs, Fig. S4A-C) and Bassez 2021 anti-PD1-treated cohort (n=12952 TAMs, Fig. S6G). Flow cytometry on the same tumors confirms PD-L1+% concordance with scRNA-seq dichotomization (Fig. 1E)."
conditions: "Human breast tumors (luminal and TNBC); 10x scRNA-seq; cluster-level (not single-cell) assignment."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

In TAMs from human breast tumors profiled by 10x scRNA-seq, expression of PD-L1 (CD274) and SIGLEC15 is mutually exclusive at the cluster level. TAM clusters can therefore be dichotomized into PD-L1+/hi (PD-L1+SIGLEC15−) and PD-L1−/lo (PD-L1−SIGLEC15+) populations using SIGLEC15 as a negative marker for PD-L1 status, circumventing PD-L1 transcript dropout.

## Evidence summary

- Wang 2024 Fig. 1B, S1F — blended UMAP across 8 TAM clusters from in-house luminal BC.
- Fig. 1C-D — quantification of cluster-level fractions.
- Fig. 1E — flow cytometry validation on same tumors.
- Fig. S4A-C, S6G — replication in Pal 2021 TNBC and Bassez 2021 anti-PD1-treated datasets.

## Conditions and scope

- Limited to human breast cancer scRNA-seq in this paper; broader applicability (lung, HCC, urothelial) requires further benchmarking.
- Cluster-level dichotomization rather than per-cell.

## Counter-evidence

- None within breast cancer; the mutual exclusivity was first proposed by Wang J et al. 2019 (Nat Med) in pan-tumor myeloid cells.

## Linked ideas

- Foundation for the downstream Wang 2024 functional analyses (PD-L1+ TAM phenotype).

## Open questions

- Single-cell-resolved (vs cluster-level) mutual exclusivity quantification.
- Whether ambient PD-L1 transcript contamination biases the partition.
