---
title: "scProtVelo explains ~50% of protein variance vs ~36% under a linear mRNA-protein assumption — a 40% relative improvement"
slug: scprotvelo-40pct-improvement-over-linear
status: supported
confidence: 0.9
tags: [scProtVelo, translation-dynamics, quantitative, model-comparison, R-squared]
domain: methods / multi-omics
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.8): 'scProtVelo resulted in more accurate modeling for almost all genes (except anti-correlated mRNA-protein pairs) (Fig. 7, E and F, and fig. S25B). Overall, accounting for translation dynamics when modeling protein abundance changes from mRNA levels led to a 40% increase in explained protein variance as compared to the simple assumption of a linear relationship (median R2 values of 36% for the linear model and 50% for scProtVelo, respectively) (Fig. 7G).'"
conditions: "scProtVelo applied to erythroid and pre-mDC trajectories; comparison to linear baseline."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

scProtVelo's explicit modeling of translation kinetics yields a 40% relative gain in explained protein variance over the naive linear mRNA-protein assumption (R² 36% → 50% median).

## Evidence summary

Direct R² comparison across genes within the erythroid and pre-mDC trajectories. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. 7 E-G).

## Conditions and scope

Healthy adult human BM CD34+ HSPC trajectories with sufficient mRNA + protein coverage.

## Counter-evidence

Anti-correlated mRNA-protein pairs are not better explained by scProtVelo than by the linear model.

## Linked ideas

## Open questions

- Generalization to other tissue systems and disease states.
