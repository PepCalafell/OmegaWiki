---
title: "crumblr — fast mixed-model testing of cell-composition shifts"
slug: crumblr-cell-composition
domain: methods / single-cell statistics
status: mainstream
aliases:
  - crumblr
  - crumblr mixed model
  - cell-composition mixed model
first_introduced: "2025 (Hoffman & Roussos, bioRxiv)"
date_updated: 2026-05-27
source_url: "https://doi.org/10.1101/2025.01.29.635498"
---

## Definition

crumblr is a mixed linear model framework for testing cell-type abundance shifts across conditions in single-cell or spatial datasets. It applies an asin-sqrt or CLR transform to compositional fractions and fits a linear mixed model per cell type, controlling for donor, sample and technical covariates simultaneously.

## Intuition

Single-cell composition data are compositional (fractions sum to one) and donor-structured (multiple samples per donor). Naive Wilcoxon or chi-square tests inflate type-I error. crumblr is the lightweight equivalent of dreamlet/variancePartition for the *composition* dimension.

## Key variants

- Paired with variancePartition to decompose variance attributable to anatomy, donor, sex, age, technical factors.
- Often coupled with dreamlet for differential expression on the same cohort.

## Known limitations

- Requires reasonable cell-type proportion estimates; sensitive to clustering choices upstream.

## Relevance to active research

- Applied to compositional differences across 15 anatomic sites in the human skin atlas ([[papers/single-cell-spatial-transcriptomic-analysis-human]]).
