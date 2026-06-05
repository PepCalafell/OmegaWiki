---
title: "Mscore is an independent prognostic indicator (HR=1.92) inversely correlated with TMB and TNB"
slug: mscore-independent-prognostic-indicator-inversely-correlated
status: weakly_supported
confidence: 0.55
tags: [Mscore, Cox-regression, TMB, TNB, AUC, prognostic, bladder-cancer]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.6): 'Multivariate Cox regression analysis identified Mscores (Cox P-value = 0.01, Hazard Ratio = 1.92) ... as independent prognostic indicators ... significant inverse correlations between Mscore and both TMB (P < 0.001, r = -0.28) and TNB (P < 0.001, r = -0.36). Integrating the Mscore with TMB and TNB achieved the highest area under the curve (AUC) value of 0.7758.'"
conditions: "IMvigor210; multivariate Cox adjusting for TMB, TNB, IC, immune phenotype, ECOG; combined Mscore+TMB+TNB AUC=0.7758."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

In multivariate Cox regression on IMvigor210, Mscore is an independent prognostic indicator (HR=1.92, P=0.01) alongside ECOG; it is inversely correlated with tumour mutational burden (r=-0.28) and tumour neoantigen burden (r=-0.36), and combining Mscore with TMB and TNB yields the best response-prediction AUC of 0.7758.

## Evidence summary

Quantitative prognostic evidence from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]; strengthens [[claims/five-gene-mscore-predicts-immune-checkpoint]].

## Conditions and scope

Single cohort; AUC of 0.7758 indicates moderate discrimination; inverse TMB/TNB correlation is weak (|r|<0.4).

## Counter-evidence

Modest effect sizes; no independent validation cohort for the multivariate model.

## Linked ideas

## Open questions

- Is the incremental AUC gain from adding Mscore to TMB+TNB significant and reproducible?
