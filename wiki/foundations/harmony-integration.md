---
title: "Harmony — fast iterative integration via soft clustering"
slug: harmony-integration
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - Harmony
  - Harmony integration
  - HarmonyPy
  - harmony batch correction
  - Korsunsky Harmony
  - iterative soft clustering integration
  - PCA-based batch correction
  - linear batch integration
  - fast scRNA-seq integration
  - Harmony embedding
  - harmonypy package
  - Harmony Raychaudhuri
first_introduced: "Korsunsky et al. 2019 *Nat. Methods* (Fast, sensitive and accurate integration of single-cell data with Harmony)"
date_updated: 2026-05-22
source_url: "https://github.com/immunogenomics/harmony"
---

## Definition

Harmony iteratively corrects PCA embeddings of single-cell data by soft-clustering cells, computing per-cluster batch-correction shifts, and re-projecting. It is fast, easy to use, and one of the most cited single-cell integration methods. It works in PCA space (no gene-level correction) and is sensitive to the user-provided PCA dimensionality.

## Strengths

- Excellent usability (high score on scIB usability axis).
- Fast on RNA tasks.
- Top performer on scATAC-seq integration in peak/window space (paired with LIGER) — see [[claims/liger-harmony-best-scatac-integration]].
- Good for simple RNA integration tasks with distinct biological signal.

## Known limitations

- Ranks outside the top third on complex atlas-scale RNA tasks — see [[claims/harmony-simple-tasks-only]].
- Linear method; cannot capture nonlinear batch effects of nested/confounded atlases.
- Performance on isolated rare cell states is poor (low isolated label F1 in scIB).

## Relevance to active research

Harmony is the workhorse for small/simple integration tasks but is increasingly replaced by scVI / scANVI on atlas-scale work. Still the default in many Seurat-pipeline single-tissue analyses. Recommended for scATAC-seq integration. See [[papers/benchmarking-atlas-level-data-integration-single]] for the benchmark.
