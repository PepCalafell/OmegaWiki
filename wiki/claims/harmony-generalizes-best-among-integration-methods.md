---
title: "Harmony generalizes best among integration methods on unseen studies"
slug: harmony-generalizes-best-among-integration-methods
status: weakly_supported
confidence: 0.7
tags:
  - data-integration
  - Harmony
  - generalization
  - benchmarking
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "Comparing scANVI, Harmony/Symphony, scGen and scPoli, all lost predictive power on unseen studies (Scenario 3) but Harmony performed best (BAS 0.24 / WF1 0.47); linear methods are less prone to overfitting and more robust to hyperparameter choice without query labels."
conditions: "Scenario 3 unseen-study patient classification; integration-method comparison."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

In the unseen-study scenario, although all integration backbones lost predictive power, the linear method Harmony generalized best (BAS 0.24 / WF1 0.47), suggesting that simpler linear approaches — less prone to overfitting and to hyperparameter sensitivity — can be preferable to VAEs when query labels for tuning are unavailable.

## Evidence summary

Integration-method comparison across Scenarios 2 and 3 (Fig. 5d,e; Extended Data Figs. 9-10; p.641).

## Conditions and scope

Specific to the no-label, cross-study deployment regime.

## Counter-evidence

In Scenario 2 (unseen patients) all methods including VAEs performed comparably and well; scANVI is the within-atlas choice.

## Linked ideas

- [[claims/scanvi-generative-integration-outperforms-alternatives-annotated]]
- [[concepts/patient-classification-reference-embedding-projection]]
- Foundations: [[foundations/harmony-integration]] · [[foundations/symphony-reference-mapping]]

## Open questions

- Can VAEs be regularized to match linear robustness under domain shift?
