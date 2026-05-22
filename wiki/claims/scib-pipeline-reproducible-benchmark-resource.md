---
title: "The scIB Python module and Snakemake pipeline establish a reproducible benchmark resource for scRNA-seq integration"
slug: scib-pipeline-reproducible-benchmark-resource
status: supported
confidence: 0.95
tags:
  - benchmarking
  - reproducibility
  - data-integration
  - infrastructure
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "The paper releases (a) an scIB Python module exposing all 14 metrics with consistent interfaces across graph/embedding/gene-matrix outputs and (b) an scIB Snakemake pipeline that reproduces the full benchmark. Both are open source. The framework's metric-aggregation robustness is validated (Spearman rank correlation > 0.96 vs alternative aggregations from Saelens 2019)."
conditions: "Resource has become the canonical benchmark for scRNA-seq integration (≥1000 citations by 2024); continues to be used by method developers as a release-validation suite."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

The scIB Python module (https://github.com/theislab/scib) and Snakemake pipeline (https://github.com/theislab/scib-pipeline) released alongside this paper establish the standard reproducible benchmark resource for scRNA-seq integration. The framework computes 14 metrics across graph / embedding / gene-matrix outputs with a 40/60 batch/bio aggregate score, validated for ranking-aggregation robustness (Spearman > 0.96 vs alternative aggregations).

## Evidence summary

Quote (p.49): "the reproducible scIB-pipeline Snakemake pipeline and the scIB python module for users to easily benchmark their particular integration scenario. In addition, we expect that this work will become a reference for method developers, who can build on the presented scenarios and metrics to assess the performance of their newly developed methods on atlas-level data integration tasks."

## Conditions and scope

- Resource is open-source, continuously maintained on GitHub.
- Citations as of 2024: ≥1000, with downstream method papers (totalVI, MultiVI, scArches) using scIB metrics for validation.

## Counter-evidence

- (none in this paper; this is largely a forward-looking claim that has been validated by subsequent adoption)

## Linked ideas

(none yet)

## Open questions

- Has the field migrated to Open Problems (open-problems.bio) as the next-generation living benchmark?
