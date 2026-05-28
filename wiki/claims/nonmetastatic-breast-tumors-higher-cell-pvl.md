---
title: "Nonmetastatic breast tumors have higher T-cell and PVL and lower B-cell abundance than metastatic"
slug: nonmetastatic-breast-tumors-higher-cell-pvl
status: weakly_supported
confidence: 0.55
tags: [breast-cancer, tumor-microenvironment, metastasis, deconvolution-derived]
domain: oncology
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "DECODE on 238 multiomics samples: T cells 1.14-fold higher vs metastatic (P=1.17e-2) and 1.23-fold vs brain mets (P=4.19e-6); PVL 1.48/1.64-fold higher; B cells 1.70/1.47-fold lower (P=6.79e-21, 3.28e-11)."
conditions: "Abundances inferred via deconvolution of cohort multiomics data, not direct single-cell measurement; observational association."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

In a breast cancer multiomics cohort, nonmetastatic primary tumors show higher T-cell and perivascular-like (PVL) cell abundance and lower B-cell abundance than metastatic tumors and brain metastases, suggesting protective roles for T and PVL cells and an association of elevated B cells with metastatic progression.

## Evidence summary

DECODE on 238 transcriptomic+proteomic samples (99 nonmetastatic, 45 metastatic, 94 brain-met): T cells 1.14-fold (P=1.17×10⁻²) and 1.23-fold (P=4.19×10⁻⁶) higher; PVL 1.48-/1.64-fold higher (P=3.38×10⁻⁹, 2.85×10⁻²⁰); B cells 1.70-/1.47-fold lower (P=6.79×10⁻²¹, 3.28×10⁻¹¹) (Fig. 6e). Authors align this with prior reports that intratumoral T-cell enrichment predicts favorable prognosis and PVL deficiency links to metastasis.

## Conditions and scope

Abundances are deconvolution-inferred from cohort data using a single-cell reference (Wu et al. 2021), not directly measured; causality not established.

## Counter-evidence

B-cell roles in the TME are context-dependent (anti- and pro-tumor); plasmablasts showed inconsistent trends across stages.

## Linked ideas

## Open questions

Whether the inferred shifts reflect causal immune mechanisms or deconvolution artifacts; subtype-level validation.
