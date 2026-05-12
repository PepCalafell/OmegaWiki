---
title: "PD-L1+/hi vs PD-L1−/lo TAM dichotomy is orthogonal to the canonical M1/M2 polarization scheme"
slug: pd-l1-tam-dichotomy-orthogonal-to-m1-m2
status: supported
confidence: 0.85
tags:
  - PD-L1
  - TAM
  - M1
  - M2
  - polarization
  - orthogonality
  - breast-cancer
domain: "immunology"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 1F, S2B, S7: M1 and M2 signature genes (Table S1) are commonly expressed in both PD-L1+/hi and PD-L1−/lo TAMs; intersection of DEGs with M1/M2 gene sets shows very limited overlap. Survival analyses using M1, M2, or M1/M2 ratio gene signatures in METABRIC luminal BC (n=1098) show no significant correlation with RFS (Fig. 3C) — unlike PD-L1+/hi TAM gene signatures which do correlate."
conditions: "Human breast tumors (luminal + TNBC); cluster-level DEG analysis; gene-signature-based survival analysis in METABRIC."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

In human breast cancer TAMs, the PD-L1+/hi vs PD-L1−/lo partition does not align with the canonical M1 vs M2 dichotomy: both PD-L1+/hi and PD-L1−/lo TAMs express M1 and M2 signature genes; DEGs distinguishing the two subsets show limited overlap with M1/M2 gene sets; and M1/M2 gene signatures (or their ratio) do not predict relapse-free survival in METABRIC luminal BC while PD-L1+ TAM signatures do.

## Evidence summary

- Wang 2024 Fig. 1F (overlay of M1/M2 signature genes on PD-L1+/− subsets).
- Fig. S2B-D (hallmark pathway enrichment, GSEA).
- Fig. S7 (DEG–M1/M2 overlap analysis across in-house and public datasets).
- Fig. 3C (M1/M2 RFS survival analysis, METABRIC).

## Conditions and scope

- Cluster-level dichotomization; gene signature definitions follow Martinez 2006 (M1/M2).
- Conclusion limited to human breast cancer; not tested across all tumor types.

## Counter-evidence

- Authors note (citing refs 14,19,26) that individual TAMs from human tumors generally co-express both M1 and M2 genes — supporting the orthogonality conclusion rather than contradicting it.

## Linked ideas

- Supports [[concepts/pd-l1-immunostimulatory-tam-phenotype]] as a phenotypic axis independent of M1/M2.
- Methodological caveat for any study still using M1/M2 framing in human TAM analysis.

## Open questions

- Whether the PD-L1 axis aligns better with the pan-cancer "mature antigen-presenting" vs "tissue-remodeling SPP1/TREM2" axis (Cheng 2021).
