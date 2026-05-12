---
title: "Density ratio of PD-L1+/PD-L1− TAMs is an independent prognostic factor for RFS in luminal breast cancer (multivariate p=0.0099, n=142)"
slug: pd-l1-pos-tam-density-ratio-multivariate-prognostic
status: supported
confidence: 0.85
tags:
  - PD-L1
  - TAM
  - prognosis
  - multivariate
  - RFS
  - mIF
  - breast-cancer
domain: "clinical / prognostic biomarker"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 3D-I: two independent in-house cohorts of luminal BC patients with archival FFPE tissue, ≥36 month follow-up. Cohort 1 (n=49, whole-slide mIF for PD-L1/CD68/DAPI) — below-median PD-L1+ TAM density associates with worse RFS (p=0.038); above-median PD-L1− TAM density worse RFS (p=0.046). Cohort 2 (n=93, TMA-based) replicates both signals (p=0.02 and p=0.01). Combined cohorts (n=142) — above-median PD-L1+/PD-L1− TAM density ratio better RFS (p=0.0003) and trend better OS (p=0.08). Multivariate analysis adjusting for age, tumor stage, grade, nodal status retains the density ratio as independent prognostic factor (p=0.0099). Total TAM density (no PD-L1 stratification) has no correlation with outcome in either cohort."
conditions: "Luminal BC FFPE tissues; PD-L1+CD68+ and PD-L1−CD68+ definitions; median split."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

In two independent FFPE cohorts of luminal breast cancer patients (n=49 + n=93), histological quantification of PD-L1+ vs PD-L1− TAM density by multiplex immunofluorescence shows that the *ratio* of PD-L1+/PD-L1− TAM density is an independent prognostic factor for relapse-free survival (multivariate Cox p=0.0099, adjusting for age, tumor stage, grade, nodal status). The signal is absent when total TAM density (CD68 alone) is examined — the prognostic information resides in the PD-L1 axis, not in TAM burden.

## Evidence summary

- Wang 2024 Fig. 3D-I (cohort schematic, mIF staining, Kaplan-Meier curves, multivariate analysis).
- Table S3 (cohort clinicopathological characteristics).

## Conditions and scope

- Luminal BC only — TNBC not included in this protein-level multivariate analysis (but signal replicates in TNBC METABRIC at signature level).
- Median split for high vs low — sensitivity to alternative cutoffs not exhaustively reported.

## Counter-evidence

- Earlier studies on intratumoral PD-L1 (not TAM-resolved) report poor prognosis in BC (Muenst 2014, ref 29) — consistent if interpreted as tumor-cell PD-L1 (rather than TAM PD-L1) being the dominant prior signal.

## Linked ideas

- Protein-level corroboration of [[claims/pd-l1-pos-tam-signature-correlates-better-rfs-breast-cancer]].
- Operationalizable biomarker derived from [[concepts/pd-l1-immunostimulatory-tam-phenotype]].

## Open questions

- Whether the PD-L1+/PD-L1− ratio improves on TILs and other established prognostic biomarkers in head-to-head comparison.
- Whether the ratio is predictive (not just prognostic) for ICI response.
- Whether automated mIF quantification platforms can deliver clinically robust cutoffs.
