---
title: "Simple baselines outperform complex single-cell methods"
aliases:
  - simple baselines win
  - strong simple baselines
tags:
  - benchmarking
  - single-cell
  - baselines
maturity: active
key_papers:
  - defining-benchmarking-open-problems-single-cell
first_introduced: "Open Problems in Single-Cell Analysis (Luecken et al., Nat. Biotechnol. 2025)"
date_updated: 2026-06-15
related_concepts:
  - static-versus-living-benchmark-paradigm
---

## Definition

The recurring empirical observation that, across several single-cell analysis tasks, simple models (e.g. logistic regression) and careful preprocessing match or beat more complex methods that explicitly model batch effects or use deep architectures.

## Intuition

Complex models add capacity to fit nuisance structure (batch, noise) but also more ways to overfit or to depend on brittle assumptions. When tasks are evaluated neutrally, the marginal benefit of complexity often fails to materialise, and a well-chosen simple baseline becomes a strong, hard-to-beat reference.

## Variants

Observed across distinct Open Problems tasks: label projection (logistic regression), denoising (variance-stabilizing preprocessing over fancy models), and perturbation prediction (simple over complex models).

## Comparison

This is the empirical complement to [[concepts/benchmark-self-assessment-bias]]: neutral evaluation tends to deflate the apparent advantage of complex, developer-promoted methods, surfacing simple baselines as competitive.

## When to use

When selecting a method for a new single-cell task: include and seriously tune a simple baseline before adopting a complex model, and demand that complexity be justified on neutral benchmarks.

## Known limitations

"Simple wins" is task- and dataset-scoped, not universal; complex models may dominate in regimes (cross-modality, large diverse perturbation data) not yet represented in the benchmark.

## Open problems

Identifying which task regimes genuinely reward model complexity rather than careful preprocessing.

## Key papers

- [[defining-benchmarking-open-problems-single-cell]] — reports the pattern across multiple tasks.

## My understanding

A useful prior for method selection in my own single-cell work: budget effort on preprocessing and a strong baseline first. Supported by [[claims/logistic-regression-outperforms-complex-batch-modeling]], [[claims/denoising-methods-perform-best-variance-stabilizing]] and [[claims/simple-models-outperform-complex-models-perturbation]].
