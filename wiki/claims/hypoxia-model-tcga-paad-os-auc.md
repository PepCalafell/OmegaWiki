---
title: "13-gene hypoxia model predicts OS in TCGA-PAAD with AUC 0.774 (1yr), 0.727 (2yr), 0.711 (3yr), exceeding clinicopathologic features alone"
slug: hypoxia-model-tcga-paad-os-auc
status: supported
confidence: 0.7
tags: [hypoxia,PDAC,prognostic-model,TCGA-PAAD,AUC,overall-survival]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: strong
    detail: "Quote (p.6, Results): 'time-dependent ROC curves for OS were generated. The area under the curve (AUC) values were 0.774 at 1 year, 0.727 at 2 years, and 0.711 at 3 years (Fig 3E). These values were significantly superior to those derived from clinicopathologic characteristics alone (Fig 3F)'. Multivariate Cox confirmed independence from age, sex, T/N stage, AJCC stage; similar AUCs reported on PACA-CA and PACA-AU (S1, S2 Fig)."
conditions: "TCGA-PAAD n=159 after QC for survival and clinical data; median dichotomisation of hypoxia score. ROC computed via timeROC R package. Note: training and reporting on the same cohort — no held-out split within TCGA-PAAD."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

The hypoxia score derived from the 13-gene signature stratifies TCGA-PAAD into high vs low hypoxia groups with significantly worse OS in the high group (Kaplan–Meier, log-rank p significant), and yields time-dependent AUCs of 0.774, 0.727, and 0.711 at 1, 2, and 3 years respectively. These AUCs exceed those of clinicopathologic features (age, sex, T, N, AJCC stage) used alone. Multivariate Cox confirms independence from those features. Similar magnitudes (not identical) are observed on PACA-CA and PACA-AU external cohorts.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 3D–F; S1, S2 Fig for PACA-CA and PACA-AU).

## Conditions and scope

- Training and ROC reporting are on the same TCGA-PAAD cohort; the headline AUCs are training-set numbers (the LASSO step used 10-fold CV, but ROC AUCs were not reported in a held-out partition).
- The PACA-CA / PACA-AU validation cohorts use the model frozen from TCGA training — partial external validity, but neither cohort is unseen during feature selection of the original 23-gene univariate-Cox shortlist (which used TCGA only).

## Counter-evidence

Other PDAC hypoxia signatures (refs 27–29 in the paper) report comparable or higher AUCs in their own training cohorts; head-to-head benchmarking is absent.

## Linked ideas

## Open questions

- Calibration vs discrimination: does the model predict event probabilities accurately, or only rank-order risk?
- Performance after multivariable adjustment for tumour grade, KRAS allele, or molecular subtype (Moffitt / Bailey / Collisson)?
