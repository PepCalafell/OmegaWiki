---
title: "Metacell granularity optimization via DubRate/ZeroRate Score"
aliases:
  - DubRate
  - ZeroRate
  - mcRigor Score
  - granularity optimization
tags: [single-cell, metacell, hyperparameter-optimization, sparsity, benchmarking]
maturity: emerging
key_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
first_introduced: "Liu & Li 2025 (Nature Communications)"
date_updated: 2026-06-02
related_concepts: [dubious-versus-trustworthy-metacell-statistical-definition, metacell-divergence-score-mcdiv-double-permutation]
---

## Definition

A criterion for choosing the metacell granularity level γ (average cells per metacell) — and, simultaneously, for selecting the metacell method itself — by balancing two competing factors:

- **DubRate** ∈ [0,1]: proportion of single cells assigned to dubious metacells (proxy for signal distortion). Rises as γ increases.
- **ZeroRate** ∈ [0,1]: proportion of zeros in the M × p metacell expression matrix (proxy for remaining sparsity). Falls as γ increases.

```
Score = 1 − w·DubRate − (1 − w)·ZeroRate ∈ [0,1]   (default w = 0.5)
```

The γ (and method) maximizing Score is optimal. Because Score is on a common [0,1] scale, it is comparable across methods, making mcRigor a task-agnostic, prior-free benchmarking and method-selection tool.

## Intuition

γ = 1 keeps single cells (no distortion but full sparsity); large γ resolves sparsity but risks merging different states (distortion). The optimum aggregates as many cells as possible while keeping only homogeneous cells together — exactly the sparsity-vs-distortion trade-off.

## Formal notation

γ = n / M (single cells per metacell). Default candidate grid γ ∈ {2,…,100} across four methods (SEACells, MetaCell, MetaCell2, SuperCell). DubRate is computed from the dubious-metacell detector (see [[metacell-divergence-score-mcdiv-double-permutation]]); ZeroRate from the aggregated metacell-by-feature matrix.

## Variants

- Adjustable weight w to emphasize distortion vs sparsity.
- In principle other hyperparameters (kNN k, number of PCs) can be optimized, but γ is prioritized as it is universally required and most impactful.

## Comparison

Unlike fixed-heuristic granularity (e.g. γ = 30 or γ = 75 defaults), Score is data-driven. The paper shows simply lowering γ to avoid dubious metacells leaves sparsity unresolved and loses statistical power — a coarse partition + mcRigor filtering beats a naively fine partition.

## When to use

To pick γ and the metacell method for a specific dataset before downstream co-expression, regulatory inference, DGE, integration, or trajectory analysis.

## Known limitations

- Optimal γ recovery degrades for methods that produce mostly dubious metacells even at small γ (SuperCell, MetaCell2 — mcRigor picked γ = 4 for both, far from the true γ*).
- Single-modality; integrating modalities into one Score is future work.

## Open problems

- Joint multi-hyperparameter and multi-modality optimization.
- Granularity selection tuned for cross-cohort integration specifically.

## Key papers

- [[mcrigor-statistical-method-enhance-rigor-metacell]] — defines DubRate, ZeroRate, and Score.

## My understanding

This turns mcRigor from a filter into an optimizer/benchmarker. The common-scale Score is what lets it answer the practitioner's real question — "which method and which γ for *my* data?" — without ground truth.
