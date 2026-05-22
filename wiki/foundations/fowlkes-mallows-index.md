---
title: "Fowlkes–Mallows Index (FMI) — clustering similarity metric"
slug: fowlkes-mallows-index
domain: "methods / clustering / statistics"
status: mainstream
aliases:
  - FMI
  - Fowlkes Mallows
  - Fowlkes-Mallows
  - FM index
  - clustering stability FMI
  - cluster agreement Fowlkes-Mallows
first_introduced: "Fowlkes & Mallows 1983 *J. Am. Stat. Assoc.* 78:553–569"
date_updated: 2026-05-22
---

## Definition

FMI is the geometric mean of pairwise precision and recall between two clusterings: FMI = √(TP/(TP+FP) · TP/(TP+FN)), where TP/FP/FN count pairs of points placed in the same / different clusters across the two partitions. It ranges in [0,1]; higher is better.

## Use

Used as a clustering-similarity score for ground truth comparison (analog to ARI) and — across multiple stochastic clustering runs — as a stability measure for selecting the number of clusters. A solution with n clusters is considered "stable" when assignments agree across runs at n, n−1, n+1.

## Relevance to active research

[[papers/cellcharter-reveals-spatial-cell-niches-associated]] uses FMI as the stability criterion to auto-select stable cluster counts in spatial omics datasets — e.g., n=9 stable for DLPFC (12 and 42 samples), n=4 and n=11 for mouse spleen, n=3/8/20 for the NSCLC CosMx cohort.
