---
title: "Symphony — compressed-reference single-cell mapping"
slug: symphony-reference-mapping
domain: "methods / single-cell / reference-mapping"
status: mainstream
aliases:
  - Symphony
  - symphonypy
  - Symphony reference mapping
first_introduced: "Kang et al. 2021 *Nature Communications* (Efficient and precise single-cell reference atlas mapping with Symphony)"
date_updated: 2026-06-04
source_url: "https://github.com/immunogenomics/symphony"
---

## Definition

Symphony builds a compressed representation of a Harmony-integrated reference atlas (cluster centroids and per-cluster linear-mixture parameters) and then maps new query cells into that same harmonized embedding without re-running integration on the full reference. A Python re-implementation, symphonypy, exposes the same workflow in the scanpy ecosystem.

## Intuition

Harmony integration is expensive and stochastic; Symphony freezes the reference geometry once and projects query cells onto it deterministically, enabling fast, reproducible label transfer and cell-type prediction against a fixed atlas.

## Formal notation

The reference is summarized by soft-cluster assignments and per-cluster batch-correction terms; a query cell's corrected coordinates are obtained by applying the precomputed linear mixture model to its initial PCA loadings.

## Key variants

- symphonypy (Python) versus the original R implementation.
- Downstream k-NN label transfer for cell-type prediction.

## Known limitations

- Inherits Harmony's linear-correction assumptions; cannot recover query-only cell states absent from the reference.
- Quality degrades when query batches differ strongly from the reference (chemistry/center shift).

## Open problems

- Calibrated uncertainty for mapped labels under large domain shift.
- Extending compressed mapping to nonlinear (VAE) references.

## Relevance to active research

Evaluated as a Harmony-based baseline for the reference-mapping patient classifier; representative of linear reference-mapping methods that proved more robust than VAEs on unseen-study generalization. Related to [[harmony-integration]], [[azimuth-reference-mapping]], [[scpoli-prototype-reference-mapping]].
