---
title: "Metacell divergence score (mcDiv) and the double permutation null"
aliases:
  - mcDiv
  - metacell divergence score
  - double permutation
  - double permutation scheme
tags: [single-cell, metacell, statistics, permutation-test, feature-correlation]
maturity: emerging
key_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
first_introduced: "Liu & Li 2025 (Nature Communications)"
date_updated: 2026-06-02
related_concepts: [dubious-versus-trustworthy-metacell-statistical-definition, metacell-granularity-optimization-dubrate-zerorate-score]
---

## Definition

The **metacell divergence score (mcDiv)** is a feature-correlation-based test statistic that quantifies the internal heterogeneity of a single metacell. For metacell *k* with an *m_k × p* cell-by-feature matrix, mcDiv is the Frobenius-norm deviation of the within-metacell feature correlation matrix *R_k* from the identity matrix *I*, normalized by the same deviation computed on a within-feature-permuted copy of the matrix:

```
mcDiv_k = ‖R_k − I‖_F / ‖R̃_k − I‖_F
```

A larger mcDiv indicates greater within-metacell feature correlation, hence greater heterogeneity (more "dubious"). The premise is that within a trustworthy metacell — cells sharing the same biological state — features should be nearly pairwise uncorrelated, with only minimal correlation induced by the simplex constraint Σλ_j = 1 (which vanishes as the number of features p grows large).

## Intuition

If all cells in a metacell are resamples of the same underlying cell, the only thing varying across them is multinomial sampling noise at fixed feature probabilities λ. Sampling noise does not create feature-feature correlation. So genuine, structured feature correlation inside a metacell is evidence that the cells are NOT in the same state — they carry biological variation that should not have been averaged away.

## Formal notation

The null hypothesis for each metacell is that observed counts follow a shared multinomial:
`(y_i1,…,y_ip) | λ, y_i+ ∼ Mult(y_i+, λ_1,…,λ_p)` for all cells i in the metacell.

The **double permutation** builds the null divergence score `mcDiv_null`:
1. **Within-cell permutation** (row-wise): independently shuffle the p feature values within each cell, preserving each cell's library size y_i+ while destroying biological feature correlations. Yields correlation matrix Π_k.
2. **Within-feature permutation** (column-wise) applied to the already within-cell-permuted matrix, yielding Π̃_k.

```
mcDiv_null_k = ‖Π_k − I‖_F / ‖Π̃_k − I‖_F
```

Both numerator and denominator must be recomputed because mcDiv and mcDiv_null involve different feature sets and require different normalization factors.

## Variants

- Standard mcRigor uses a single double-permutation realization per metacell. The authors flag multiple-rounds double permutation (multiple null draws per metacell) as a possible robustness improvement.
- The relaxed-threshold "mcRigor two-step" extension uses the 85th percentile of mcDiv_null (vs default 95th) to re-partition dubious metacells rather than discard them.

## Comparison

High-dimensional covariance tests (testing whether a feature covariance matrix deviates from diagonal) appear superficially relevant but are inapplicable here: metacell size is typically <100, too small for the asymptotic null distributions to hold, and their nulls do not condition on cell library size. Within-cell permutation is what makes the mcRigor null library-size-aware.

## When to use

To flag heterogeneous ("dubious") metacells in any metacell partition before downstream analysis (co-expression, regulatory inference, DGE, trajectory).

## Known limitations

- Within-feature permutation alone is an invalid null: it does not preserve library-size-driven correlations, sets the threshold too low, and misclassifies many trustworthy metacells as dubious (see [[dubious-versus-trustworthy-metacell-statistical-definition]]).
- The double permutation is performed only once per metacell in standard mcRigor.

## Open problems

- Whether multiple double-permutation rounds yield more robust detection.
- Extending the statistic to integrate multiple modalities (RNA + ATAC) jointly rather than one modality at a time.

## Key papers

- [[mcrigor-statistical-method-enhance-rigor-metacell]] — introduces mcDiv and the double permutation.

## My understanding

This is the statistical engine of mcRigor. The clever bit is the library-size-preserving within-cell permutation: it builds a per-metacell negative control that respects the multinomial measurement model, so "structured correlation = mixed biological states" becomes a calibrated test rather than a heuristic.
