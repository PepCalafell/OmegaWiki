---
title: "SIGLEC15/PD-L1 mutual exclusivity as a scRNA-seq TAM dichotomization strategy"
aliases:
  - "SIGLEC15 PD-L1 dichotomization"
  - "PD-L1 dropout workaround"
  - "SIGLEC15 surrogate for PD-L1"
  - "mutually exclusive immune checkpoint expression TAM"
  - "PD-L1 SIGLEC15 cluster partition"
  - "S15-PD-L1 scRNA-seq dichotomy"
  - "low-abundance transcript proxy"
  - "checkpoint ligand mutual exclusivity TAM"
tags:
  - scRNA-seq
  - methodological
  - macrophage
  - PD-L1
  - SIGLEC15
  - dropout
maturity: emerging
key_papers:
  - pd-l1-expressing-tumor-associated-macrophages
first_introduced: "Wang J et al. 2019 Nat Med (SIGLEC15 immune suppressor concept); operationalized as a TAM cluster dichotomization tool by Wang L et al. 2024 Cell Reports Medicine"
date_updated: 2026-05-12
related_concepts:
  - pd-l1-immunostimulatory-tam-phenotype
  - tumor-associated-macrophage-immunosuppression
---

## Definition

A scRNA-seq analytical strategy in which TAM clusters are dichotomized into PD-L1+/hi (PD-L1+SIGLEC15−) vs PD-L1−/lo (PD-L1−SIGLEC15+) populations using SIGLEC15 expression as a proxy for PD-L1 status. The strategy circumvents the well-known PD-L1 gene dropout problem in droplet-based scRNA-seq: PD-L1 (CD274) is a low-abundance transcript that frequently fails to be detected even when surface protein is present, while SIGLEC15 — being mutually exclusive with PD-L1 in tumor-infiltrating myeloid cells — is more reliably captured and can serve as a negative marker for PD-L1.

## Workflow (Wang 2024)

1. Sub-cluster myeloid compartment from scRNA-seq; identify TAM clusters (excluding mast cells, DCs, monocytes).
2. Visualize PD-L1 and SIGLEC15 expression as blended UMAP features across TAM clusters.
3. Assign clusters with predominant PD-L1 expression (high PD-L1 fraction, low SIGLEC15 fraction) to PD-L1+/hi; clusters with the inverse pattern to PD-L1−/lo.
4. Validate by flow cytometry of PD-L1 protein on CD14+HLA-DR+ TAMs from the same tumors (Wang 2024 reports good agreement between scRNA-seq dichotomization and flow PD-L1+%).

## Validity

- Mutual exclusivity replicated across in-house breast tumors (n=4 luminal) and two public datasets (Pal 2021 TNBC, n=8; Bassez 2021 anti-PD1 treated, n=19).
- PD-L1+ TAM fractions identified by the dichotomization track flow cytometry-quantified PD-L1+ protein percentage.
- Down-stream gene signatures (maturation, pro-inflammatory in PD-L1+; pro-tumor in PD-L1−) replicate across datasets, suggesting the dichotomization recovers biologically coherent populations.

## Limitations

- SIGLEC15 mutual exclusivity is established empirically (Wang J 2019 Nat Med) but its mechanistic basis is unclear; rare double-positive or double-negative TAMs are not analyzed.
- Cluster-level assignment may mis-classify minor subpopulations within a cluster.
- Cell ambient transcript contamination and ambient PD-L1 dropout may bias the partition; spike-in controls are not standard.
- Not validated outside of human breast cancer in the Wang 2024 paper; generalizability to lung, HCC, urothelial settings requires additional benchmarking.

## When to use

- Whenever analyzing low-PD-L1-coverage human TAM scRNA-seq datasets where direct PD-L1 gating fails.
- As a pre-processing step before differential expression to identify PD-L1+ vs PD-L1− TAM signatures.
- To replicate the Wang 2024 dichotomization on new tumor types or treatment contexts.

## Key papers

- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — Wang et al. 2024 Cell Reports Medicine. First explicit operationalization of this dichotomization on human breast cancer TAMs.
