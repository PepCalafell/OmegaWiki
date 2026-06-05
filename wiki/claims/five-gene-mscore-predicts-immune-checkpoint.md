---
title: "A five-gene Mscore (CXCL9, C3, CTSC, CAPG, CTSB) predicts ICB efficacy in bladder cancer"
slug: five-gene-mscore-predicts-immune-checkpoint
status: weakly_supported
confidence: 0.5
tags: [Mscore, risk-model, biomarker, ICB, bladder-cancer, machine-learning]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.6): 'we identified a set of five genes to construct a risk assessment model ... Mscore = -0.1463152×Exp.CXCL9 + 0.1018251×Exp.C3 + 0.1316632×Exp.CTSC - 0.1869480×Exp.CAPG + 0.1556237×Exp.CTSB.'"
conditions: "Multivariate Cox model selected by AIC on the IMvigor210 cohort using Macro-CXCL9 marker genes; not validated in a phase 3 trial."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

A five-gene risk score, Mscore — a weighted combination of CXCL9, C3, CTSC, CAPG, and CTSB expression — was constructed from Macro-CXCL9 marker genes via AIC-selected multivariate Cox regression on IMvigor210 to predict immune checkpoint blockade efficacy in bladder cancer.

## Evidence summary

Risk-model construction from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]. Defines the concept [[concepts/mscore-cxcl9-macrophage-marker-gene-icb]].

## Conditions and scope

Derived and evaluated on retrospective bulk cohorts; CXCL9 carries a protective (negative) coefficient while C3/CTSC/CTSB are risk-increasing.

## Counter-evidence

No prospective/phase-3 validation; marker-gene biology in bladder cancer cells not experimentally tested (author-acknowledged limitation).

## Linked ideas

## Open questions

- Does Mscore outperform simpler single-marker (CXCL9, PD-L1, TMB) predictors prospectively?
