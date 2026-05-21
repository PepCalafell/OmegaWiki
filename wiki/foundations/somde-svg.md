---
title: "SOMDE — self-organising-map Gaussian-process SVG detection"
slug: somde-svg
domain: spatial-transcriptomics-methods
status: mainstream
aliases:
  - SOMDE
  - self-organising map SVG
  - SOM-GP SVG
  - Hao et al. 2021 SOMDE
  - SOMDE scalability
first_introduced: "Hao et al. 2021 Bioinformatics"
date_updated: 2026-05-21
source_url: "https://github.com/WhirlFirst/somde"
---

## Definition

SOMDE is a Python-based SVG detection method that first clusters neighbouring spatial spots into nodes using a self-organising map (SOM), then fits a Gaussian-process model on the node-level expression to score spatial variability. This two-stage design dramatically reduces the effective number of points the GP must regress on.

## Intuition

Aggregating nearby spots into SOM nodes preserves most spatial structure while collapsing N spots to K ≪ N nodes, so the cubic-in-N GP cost becomes cubic-in-K. The trade-off is that very local sub-spot patterns may be smoothed away.

## Known limitations

- SOM aggregation discards fine sub-spot spatial structure.
- Fails on Stereo-seq datasets in Li et al. 2025 benchmark (numerical-stability errors).
- Less competitive than HVGs for spatial domain detection.

## Relevance to active research

In Li et al. 2025 Genome Biology SVG benchmark, SOMDE shows the best memory usage AND fastest running time across spot counts up to 40,000. Recommended (with SPARK-X) for high-throughput SVG analyses where scalability is the dominant constraint.
