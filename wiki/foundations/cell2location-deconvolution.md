---
title: "cell2location — Bayesian deconvolution for spatial transcriptomics"
slug: cell2location-deconvolution
domain: "methods / spatial-transcriptomics / deconvolution"
status: mainstream
aliases:
  - "cell2location"
  - "Cell2location"
  - "Cell2loc"
first_introduced: "Kleshchevnikov et al. Nat Biotechnol 2022"
date_updated: 2026-05-27
source_url: "https://github.com/BayraktarLab/cell2location"
---

## Definition

cell2location is a hierarchical Bayesian (PyTorch/Pyro) model that estimates absolute cell-type abundances per spatial spot from spatial transcriptomics data using an scRNA-seq reference. Originally designed for sequencing-based platforms (Visium, ST), it can also be applied to imaging-based, single-cell-resolution data after cell segmentation by treating each segmented cell as a unit.

## Intuition

Spot-deconvolution methods place cell types into Visium-style multi-cell spots; cell2location additionally calibrates absolute cell abundance and accounts for technology-specific count distributions. Strong when scRNA-seq reference is comprehensive and matches the spatial tissue.

## Known limitations

- Slow on large datasets (e.g. ~2 days for ~400k cells MERSCOPE liver in NiCo's benchmark).
- High memory footprint.
- Designed for spot deconvolution; performance on single-cell-resolution imaging data can be sub-optimal for fine-grained sub-states (e.g. zonated hepatocytes).

## Relevance to active research

State-of-the-art baseline for spatial cell-type abundance. Routinely benchmarked against newer tools (TACCO, Tangram, uniPort, NiCo).
