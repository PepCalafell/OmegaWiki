---
title: "Partial Least Squares (PLS)"
slug: partial-least-squares-pls
domain: statistics
status: mainstream
aliases:
  - PLS
  - PLS regression
  - partial least squares regression
  - projection to latent structures
first_introduced: "1975"
date_updated: 2026-06-03
source_url: ""
---

## Definition

Partial Least Squares (PLS) is a supervised dimensional-reduction technique that finds low-dimensional projections of a predictor matrix X which maximize covariance with one or more outcome variables Y. Unlike PCA, which maximizes variance within X alone, PLS orients its latent components toward directions that are predictive of Y.

## Intuition

PCA asks "where does X vary most?"; PLS asks "where does X vary most *in a way that tracks the outcome*?". This makes PLS well-suited to surfacing weak, outcome-associated signal that unsupervised methods would bury under dominant but irrelevant variance.

## Formal notation

PLS iteratively extracts latent vectors `t = Xw` and `u = Yc` such that the weights `w, c` maximize `cov(t, u)`, deflating X and Y after each component.

## Key variants

- PLS1 (single response) vs PLS2 (multiple responses)
- sparse PLS (sPLS) for feature selection
- PLS-DA for classification outcomes

## Known limitations

- Supervision toward Y can discard fine-grained structure unrelated to the outcome (e.g. cell-type identity in single-cell data).
- Requires meaningful outcome labels; uninformative Y yields uninformative components.

## Open problems

- Choosing the number of latent components without overfitting in high-dimensional settings.

## Relevance to active research

In single-cell genomics, PLS supplies the supervised "state"-focused embedding in semi-supervised frameworks such as scSLIDE, separating cells by phenotype metadata (disease status, severity) while remaining tractable at atlas scale.
