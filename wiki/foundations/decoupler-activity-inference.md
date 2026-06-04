---
title: "decoupleR — unified framework for activity inference from omics"
slug: decoupler-activity-inference
domain: "methods / functional-genomics / activity-inference"
status: mainstream
aliases:
  - decoupleR
  - decoupler
  - decoupler-py
first_introduced: "Badia-i-Mompel et al. 2022 *Bioinformatics Advances* (decoupleR: ensemble of computational methods to infer biological activities from omics data)"
date_updated: 2026-06-04
source_url: "https://github.com/saezlab/decoupleR"
---

## Definition

decoupleR is a framework that bundles many statistical methods (ULM, MLM, WSUM, AUCell, GSEA, etc.) to infer biological activities — transcription-factor activities, pathway activities, gene-program scores — from omics data using a prior-knowledge network. It standardizes the input (signature × feature matrix + prior network) and output (source × activity matrix) so activity-inference methods are interchangeable.

## Intuition

Rather than committing to one enrichment method, decoupleR runs a chosen statistic over a prior network and returns per-sample activity scores. With the univariate linear model (ULM), the activity of a source (TF, pathway, factor) is the coefficient of a regression of the expression signature on that source's target weights.

## Formal notation

For source s with target weights w_s, the ULM activity for a sample's expression vector x is the slope of the linear fit x ~ w_s, optionally standardized into a t-value.

## Key variants

- ULM (univariate linear model), MLM (multivariate), WSUM (weighted sum), AUCell, consensus across methods.
- Pseudobulk aggregation via `get_pseudobulk` for sample/cell-type-level inference.

## Known limitations

- Inferences inherit any bias in the prior network.
- ULM assumes additive, linear target contributions.

## Open problems

- Calibrated significance for activity scores across heterogeneous datasets.
- Method-choice guidance for sparse single-cell data.

## Relevance to active research

Used (with [[collectri-tf-regulon-network]] and [[spectra-factor-analysis-gene-programs]]) to compute the ULM signature-activity and TF-activity scores underlying the inflammation landscape across circulating immune cells.
