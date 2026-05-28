---
title: "RCTD — Robust Cell Type Decomposition for spatial transcriptomics"
slug: rctd-deconvolution
domain: methods
status: mainstream
aliases:
  - RCTD
  - Robust Cell Type Decomposition
first_introduced: "2022"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1038/s41587-021-00830-w"
---

## Definition

RCTD decomposes cell-type mixtures at each spatial transcriptomics location (or bulk pixel) using a single-cell reference, modelling counts with a Poisson/negative-binomial likelihood and explicitly estimating and correcting platform-specific effects between reference and spatial data.

## Intuition

Spatial spots contain mixtures of cells; RCTD fits a probabilistic mixture model per spot while accounting for systematic platform differences, yielding robust proportion estimates even when the reference and target come from different technologies.

## Formal notation

Maximum-likelihood estimation of cell-type weights per pixel under a (negative-binomial) count model with a learned platform-effect term.

## Key variants

- Doublet mode (≤2 cell types per spot) vs. full mode (many cell types).

## Known limitations

- Built around count-based likelihoods, ill-suited to proteomic/metabolomic data.
- Spatial deconvolution methods can misattribute non-spatial biological variability to spatial effects when applied outside spatial contexts.

## Open problems

Generalizing the platform-effect correction to non-count omics.

## Relevance to active research

A standard spatial deconvolution baseline; compared against by universal frameworks such as DECODE on both spatial and non-spatial tasks.
