---
title: "High PD-L1+/hi TAM gene signature correlates with better relapse-free survival in METABRIC (p=0.001) and TCGA (p=0.014) luminal breast cancer; PD-L1+/PD-L1− ratio is the strongest signal"
slug: pd-l1-pos-tam-signature-correlates-better-rfs-breast-cancer
status: supported
confidence: 0.9
tags:
  - PD-L1
  - TAM
  - prognosis
  - RFS
  - METABRIC
  - TCGA
  - breast-cancer
domain: "immuno-oncology / clinical correlation"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 3A-B: gene signatures derived from top DEGs overlapping in in-house and public scRNA-seq used to stratify METABRIC luminal BC (n=1098) into top 25% vs bottom 25% — PD-L1+/hi signature: better RFS (log rank p=0.001); PD-L1−/lo signature: worse RFS (p=0.036); PD-L1+/PD-L1− ratio: better RFS (p<0.0001). Replicated in TCGA luminal BC (n=789): PD-L1+/hi p=0.014, PD-L1−/lo p=0.036, ratio p=0.032. PD-L1+/hi TAM signature also correlates with better RFS in METABRIC TNBC (n=269, Fig. S8A). CD68 alone shows no significant prognostic correlation in either dataset (Fig. S8B-C)."
conditions: "Bulk-tumor transcriptomic data (METABRIC, TCGA); gene-signature stratification at 25% cutoffs; luminal and TNBC subtypes."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

Gene signatures derived from PD-L1+/hi vs PD-L1−/lo TAM DEGs (intersection of in-house and public scRNA-seq) stratify breast cancer patients by relapse-free survival: high PD-L1+/hi signature → better RFS; high PD-L1−/lo signature → worse RFS; PD-L1+/PD-L1− ratio is the strongest signal. Replicated across METABRIC and TCGA in luminal and TNBC subtypes. CD68 (total TAM) shows no association — the prognostic information lies in the PD-L1 axis, not in TAM burden.

## Evidence summary

- Wang 2024 Fig. 3A (METABRIC), 3B (TCGA), 3C (M1/M2 negative control), S8A (TNBC METABRIC).
- Fig. S8B-C: CD68 RFS null result.

## Conditions and scope

- Bulk-tumor transcriptomic stratification (gene signature scores).
- 25% top vs bottom cutoffs — sensitivity to alternative cutoffs not exhaustively reported.
- Independent in-house cohorts (Fig. 3F-H) further support the protein-level (mIF) finding.

## Counter-evidence

- Earlier study (Muenst 2014, ref 29) reported intratumoral PD-L1 (not TAM-resolved) correlates with poor prognosis in BC — likely captures tumor-cell-dominant PD-L1 rather than TAM PD-L1.

## Linked ideas

- Supports [[concepts/pd-l1-immunostimulatory-tam-phenotype]].
- Replicated at protein level via mIF in claim [[claims/pd-l1-pos-tam-density-ratio-multivariate-prognostic]].

## Open questions

- Whether the gene-signature stratification predicts response to ICI in immunotherapy-treated cohorts.
- Whether the prognostic effect generalizes to lung, HCC, urothelial settings where PD-L1+ TAM-prognosis correlations are reported but not signature-resolved.
