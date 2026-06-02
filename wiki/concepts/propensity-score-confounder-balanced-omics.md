---
title: "Propensity-score confounder balancing for omics group comparison"
aliases:
  - "propensity score matching weights"
  - "matching-weights confounder adjustment"
tags:
  - methodology
  - biostatistics
  - confounders
  - cancer-genomics
  - causal-inference
maturity: active
key_papers:
  - characterization-hypoxia-associated-molecular-features-aid
first_introduced: "Rosenbaum & Rubin 1983 (propensity score); applied to pan-cancer hypoxia omics by Ye et al. 2019"
date_updated: 2026-06-02
related_concepts: []
---

## Definition

Propensity-score confounder balancing is a statistical strategy for comparing molecular features between two observational groups (e.g. hypoxia score-high vs score-low tumours) while removing the influence of measured clinical confounders. A propensity score — the probability of group membership given covariates — is estimated by logistic regression, then used (via matching weights) to reweight samples so the two groups have balanced covariate distributions before any molecular feature is tested.

## Intuition

In observational omics cohorts like TCGA, groups defined by a biological state of interest also differ systematically in sex, age, stage, histology, ethnicity, and tumour purity. Naively testing molecular differences confounds the biological signal with these covariates. Reweighting by the propensity score makes the two groups "look alike" in their confounders, so the residual molecular differences are more plausibly attributable to the state of interest.

## Formal notation

Propensity score *e(x) = P(group=1 | covariates x)*; matching weights reweight each sample toward covariate balance; balance accepted when the standardized weighted-propensity difference < 10%. Significance assessed per feature with permutation testing.

## Variants

- Inverse-probability-of-treatment weighting (IPTW).
- Propensity-score matching (pairing rather than weighting).

## Comparison

An observational-data analogue to randomization; weaker than experimental control but applicable to large retrospective cohorts.

## When to use

When comparing molecular profiles between observationally defined groups in cohorts with known clinical confounders and no randomization.

## Known limitations

- Balances only *measured* confounders; unmeasured confounding remains.
- Balancing yields association, not causation.

## Open problems

- Robustness to confounder selection and model misspecification.

## Key papers

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — applies matching-weights propensity scoring across 21 cancer types to isolate hypoxia-associated features.

## My understanding

The methodological backbone that lets Ye et al. claim their hypoxia-associated signatures are "largely independent from the potential confounders" — a transferable pattern for any TCGA-style two-group molecular comparison.
