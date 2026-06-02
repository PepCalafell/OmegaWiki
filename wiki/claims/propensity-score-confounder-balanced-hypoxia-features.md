---
title: "A propensity score algorithm balances clinical confounders to isolate hypoxia-associated molecular features"
slug: propensity-score-confounder-balanced-hypoxia-features
status: supported
confidence: 0.8
tags:
  - methodology
  - propensity-score
  - confounders
  - hypoxia
  - pancancer
domain: "cancer-genomics / biostatistics / hypoxia"
source_papers:
  - characterization-hypoxia-associated-molecular-features-aid
evidence:
  - source: characterization-hypoxia-associated-molecular-features-aid
    type: supports
    strength: moderate
    detail: "Authors used logistic-regression propensity scores with matching weights to reweight hypoxia score-high vs score-low samples, requiring standardized weighted-propensity difference <10% for confounders (sex, age, ethnicity, smoking, stage, histology, tumour purity). Quote (p.442): 'we identified hypoxia-biased molecular signatures that are largely independent from the potential confounders across 21 cancer types.' Permutation tests (100×, P<0.05) controlled false detection."
conditions: "Confounders balanced: sex, ethnicity, age at diagnosis, smoking status, tumour stage, histological type, tumour purity. Significance thresholds per layer: mRNA/miRNA FC>2 & FDR<0.05; protein/methylation difference>0.2 & FDR<0.05; mutation/SCNA FDR<0.05."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Comparing molecular features between hypoxia score-high and score-low groups within each cancer type, after propensity-score reweighting to balance clinical confounders, yields hypoxia-associated signatures that are largely independent of confounding clinical variables. This methodological framework is what distinguishes hypoxia-driven molecular differences from those attributable to stage, purity, sex, or other covariates.

## Evidence summary

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — propensity-score matching weights + permutation testing across 21 cancer types.

## Conditions and scope

- Statistical balancing, not causal proof; identifies association under balanced confounders.

## Counter-evidence

- Authors acknowledge that which alterations are *directly* caused by hypoxia remains unresolved (limitations).

## Linked ideas

(none yet)

## Open questions

- How sensitive are the identified features to the choice of confounders included in the propensity model?
