---
title: "Houseman cell-composition deconvolution"
slug: houseman-methylation-cell-composition-deconvolution
domain: methods
status: mainstream
aliases: ["Houseman method", "Houseman deconvolution", "reference-based cell-type estimation"]
first_introduced: "2012"
date_updated: 2026-06-12
source_url: "https://doi.org/10.1186/1471-2105-13-86"
---

## Definition

The Houseman method estimates the proportions of constituent cell types in a heterogeneous sample (e.g. whole blood) from its DNA-methylation profile, using a reference of cell-type-specific methylation signatures via constrained projection/regression.

## Intuition

It treats bulk methylation as a mixture of pure cell-type signatures and solves for the mixing weights, providing surrogate cell-count estimates to control EWAS confounding.

## Formal notation

Constrained (non-negative) quadratic programming projecting sample β-values onto a reference signature matrix.

## Key variants

Reference-based (Houseman) vs reference-free (RefFreeEWAS) deconvolution; extended panels (EpiDISH).

## Known limitations

Depends on reference quality and matching tissue; coarse cell-type resolution.

## Open problems

Accurate estimation of rare and activated immune subsets.

## Relevance to active research

Provided the estimated blood cell proportions used as covariates throughout the 300BCG EWAS models.
