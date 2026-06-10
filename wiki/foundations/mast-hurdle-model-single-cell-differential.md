---
title: "MAST — hurdle model for single-cell differential expression"
slug: mast-hurdle-model-single-cell-differential
domain: "methods / single-cell / differential expression"
status: mainstream
aliases:
  - MAST
  - Model-based Analysis of Single-cell Transcriptomics
  - MAST hurdle model
  - two-part hurdle model
first_introduced: "Finak et al. 2015, Genome Biology"
date_updated: 2026-06-10
source_url: "https://doi.org/10.1186/s13059-015-0844-5"
---

## Definition

MAST is a two-part generalized linear "hurdle" model for single-cell RNA-seq differential expression. It jointly models the discrete rate of expression (whether a gene is detected) and the continuous level of expression conditional on detection, treating the cellular detection rate (fraction of genes detected per cell) as a covariate to control for technical variation.

## Intuition

scRNA-seq data are bimodal: a gene is either undetected (a dropout/true zero) or expressed at some positive level. A single Gaussian or negative-binomial fit handles this poorly. MAST's hurdle splits the problem in two and recombines the components via a likelihood-ratio test.

## Known limitations

- Treating each cell as an independent sample inflates significance: very small fold-changes yield very low P values, so downstream heterogeneity filters (e.g. requiring a DEG to be significant in ≥80% of patient samples) are needed to recover biologically meaningful effects.
- Pseudobulk methods are now often preferred for multi-sample designs to respect the sample as the unit of replication.

## Open problems

- Reconciling cell-level power with sample-level replication remains an active debate in single-cell DE.

## Relevance to active research

The default `FindMarkers`/`FindAllMarkers` test option in Seurat for cluster markers and disease-vs-control DEGs; used across the single-cell corpus for marker discovery and condition comparisons.
