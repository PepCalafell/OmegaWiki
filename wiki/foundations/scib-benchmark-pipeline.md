---
title: "scIB — single-cell Integration Benchmark Python module and Snakemake pipeline"
slug: scib-benchmark-pipeline
domain: "methods / benchmarking / single-cell-integration"
status: mainstream
aliases:
  - scIB
  - scIB pipeline
  - scIB benchmark
  - single-cell integration benchmark
  - scib python module
  - scib-pipeline Snakemake
  - Luecken scIB
  - Theis lab integration benchmark
  - scib-reproducibility
  - atlas-level integration benchmark suite
  - scib metrics
  - scib 14 metrics
first_introduced: "Luecken et al. 2022 *Nat. Methods* (Benchmarking atlas-level data integration in single-cell genomics)"
date_updated: 2026-05-22
source_url: "https://github.com/theislab/scib"
---

## Definition

scIB (single-cell Integration Benchmark) is the open-source Python module and Snakemake pipeline that operationalizes the Luecken et al. 2022 benchmark of 16 integration methods × 13 atlas tasks. It exposes 14 integration metrics (5 batch removal + 5 label-based bio-conservation + 3 label-free bio-conservation + 1 graph connectivity) with a consistent interface across graph / embedding / gene-matrix outputs, and aggregates them via a 40/60 batch/bio score.

## Strengths

- Reference benchmark resource for the field — see [[claims/scib-pipeline-reproducible-benchmark-resource]].
- Metric aggregation validated for robustness (Spearman > 0.96 vs alternative aggregations from Saelens 2019).
- Reproducible Snakemake pipeline reruns full benchmark.
- Used as release-validation suite by downstream method papers (totalVI, MultiVI, scArches).

## Known limitations

- Covers RNA + ATAC only; no multimodal (CITE-seq, RNA+ATAC) integration benchmark.
- Reference-mapping (scArches, Azimuth) reformulation not covered.
- Methods released after November 2020 not included in the original benchmark; community contributions extend coverage.

## Relevance to active research

scIB is the canonical benchmark resource for scRNA-seq integration method selection; its 40/60 batch/bio score is the de-facto standard. The next-generation living benchmark is Open Problems ([[foundations/openproblems-benchmark]]). See [[papers/benchmarking-atlas-level-data-integration-single]].
