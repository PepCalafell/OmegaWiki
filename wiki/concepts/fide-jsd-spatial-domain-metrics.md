---
title: "FIDE and JSD metrics for spatial-domain continuity and cross-slide homogeneity"
slug: fide-jsd-spatial-domain-metrics
domain: "methods / spatial-transcriptomics / benchmarking"
maturity: emerging
tags: []
aliases:
  - FIDE score
  - F1-score of inter-domain edges
  - Jensen-Shannon divergence spatial
  - JSD spatial domain proportion
  - cross-slide homogeneity metric
  - domain continuity metric
  - spatial benchmarking metrics
  - FIDE JSD spatial benchmark
  - inter-domain edge F1
  - post-crop JSD over/under correction metric
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

Two complementary metrics for benchmarking spatial-domain assignment without external ground truth:
- **FIDE (F1-score of inter-domain edges)**: measures spatial continuity — high FIDE means cells of the same domain tend to be neighbors in the proximity graph, low FIDE means fragmented domains.
- **JSD (Jensen-Shannon divergence)**: measures cross-slide homogeneity — JSD between domain-proportion distributions across slides; low JSD means similar slides yield similar domain proportions (good integration), high JSD means slide-specific assignments dominate (under-correction).

A "post-crop" variant of JSD evaluates over/under correction: artificially remove a region from one slide, retrain, then split the matched slide identically; high post-crop JSD indicates the model fails to recover the cropped-region domain proportions (either over-correcting by spreading domains uniformly, or under-correcting by hallucinating slide-specific domains).

## Why it matters

Spatial-domain ground truth is scarce (DLPFC layer annotations being a notable exception). FIDE+JSD provide an evaluation framework that requires neither manual annotations nor synthetic ground truth, enabling fair comparison across tissues, panels, and platforms. The pairing captures the two failure modes of multi-slide spatial clustering: discontinuity and over/under correction.

## Key open questions

- Calibration of FIDE/JSD across tissues with different intrinsic cellular density.
- Combined single-number scores that balance continuity vs homogeneity.

## Status today

Adopted in [[papers/novae-graph-based-foundation-model-spatial]] as the primary benchmark metrics, complementing ARI (used when ground truth exists, e.g., synthetic datasets) and FIDE-on-synthetic-ARI in DLPFC-style benchmarks.
