---
title: "A 13-gene hypoxia-responsive macrophage signature (LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5) trained by LASSO-Cox on TCGA-PAAD"
slug: 13-gene-hypoxia-prognostic-model-pdac
status: supported
confidence: 0.7
tags: [hypoxia,PDAC,prognostic-model,LASSO-Cox,gene-signature,TCGA-PAAD]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: strong
    detail: "Quote (p.5–6, Results + Methods): '882 DEGs were discerned... univariate Cox regression analysis, identifying 23 genes... Lasso Cox regression analysis... optimal Lambda is 0.0432, and 13 hypoxia-related genes were finally included... including LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5'. Pipeline: macrophage-cluster1 PDAC-vs-normal DEGs (|log2FC|>0.25, p<0.05) → univariate Cox on TCGA-PAAD OS → 10-fold cross-validated LASSO (glmnet)."
conditions: "Training cohort: TCGA-PAAD (n=159 after QC); validation cohorts: PACA-CA (n=142), PACA-AU (n=76). Hypoxia score = ssGSEA of the 13-gene signature; patients dichotomised at median."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

A 13-gene hypoxia-related prognostic signature for PDAC was constructed by (i) identifying 882 DEGs between PDAC and normal pancreas within the hypoxia-responsive macrophage subcluster, (ii) keeping 23 genes prognostic for OS by univariate Cox, and (iii) shrinking to 13 genes via 10-fold cross-validated LASSO-Cox (λ=0.0432, glmnet). The 13 genes are LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 3A–B; S1 Table for coefficients). External validation on PACA-CA and PACA-AU (S1, S2 Fig).

## Conditions and scope

- The signature is *constructed from single-cell macrophage DEGs* but *scored at bulk-tissue level* via ssGSEA — the standard idiom for scRNA-derived bulk-applied signatures.
- LYZ and PLAU are macrophage / myeloid markers and not hypoxia-canonical; the signature is thus a hypoxia-responsive-myeloid composite, not a pure hypoxia signature.
- Signature genes partially overlap with prior PDAC hypoxia signatures (PLAU recurs across refs 27–29), but the 13-gene combination is novel.

## Counter-evidence

None within paper scope. No independent external re-derivation; validation cohorts use the same gene weights, not an independent training pass.

## Linked ideas

## Open questions

- How does this 13-gene signature compare quantitatively to Buffa-72 or Winter-99 generic hypoxia signatures on TCGA-PAAD survival?
- Are LYZ and PLAU sufficient to explain most of the prognostic variance (i.e., is the signature a thinly disguised myeloid-infiltration score)?
