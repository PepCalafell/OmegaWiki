---
title: "CellTypist"
slug: "celltypist"
domain: "single-cell genomics / cell-type annotation"
status: mainstream
aliases:
  - CellTypist
  - Immune_All_High
  - Immune_All_Low
first_introduced: "Domínguez Conde et al., Science 2022"
date_updated: 2026-06-03
source_url: "https://www.celltypist.org/"
---

## Definition

CellTypist is a logistic-regression-based automated cell-type annotation tool for single-cell transcriptomes that assigns labels by predicting from pre-trained immune and tissue reference models (e.g. `Immune_All_High`, `Immune_All_Low`).

## Intuition

Rather than clustering then manually annotating, CellTypist transfers labels from large curated references with calibrated probabilities, enabling fast, reproducible, multi-resolution annotation across datasets.

## Formal notation

Per-cell label = argmax of an L2-regularized multinomial logistic-regression model trained on a reference; optional majority-voting over over-clustered neighborhoods refines noisy single-cell predictions.

## Key variants

- `Immune_All_High` (coarse immune labels) and `Immune_All_Low` (fine-grained immune labels).
- Tissue-specific and custom user-trained models.

## Known limitations

- Predictions are bounded by reference coverage; novel states are forced into the nearest known label.
- Immune-focused default models under-resolve stromal/epithelial compartments.

## Open problems

- Calibrating confidence for out-of-reference cell states.

## Relevance to active research

Used as a supervised annotation/validation layer in large pan-cancer single-cell atlases, including label assignment for scIB benchmarking and cross-resolution validation of fine-grained clusters.
