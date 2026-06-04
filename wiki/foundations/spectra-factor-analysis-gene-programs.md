---
title: "Spectra — supervised factor analysis of single-cell gene programs"
slug: spectra-factor-analysis-gene-programs
domain: "methods / single-cell / gene-programs"
status: mainstream
aliases:
  - Spectra
  - SPECTRA
  - supervised factor analysis single-cell
first_introduced: "Kunes et al. 2024 *Nature Biotechnology* (Supervised discovery of interpretable gene programs from single-cell data)"
date_updated: 2026-06-04
source_url: "https://github.com/dpeerlab/spectra"
---

## Definition

Spectra is a supervised factor-analysis method for single-cell RNA-seq that takes a set of user-provided gene programs (knowledge-based gene sets) as priors and refines them into data-supported, cell-type-specific factors. Each factor is a weighted gene set whose per-cell activity can be scored, letting curated immunological signatures be tailored to the actual transcriptional structure of a dataset rather than used as fixed lists.

## Intuition

Standard gene-set scoring applies a fixed list regardless of dataset; Spectra instead "lets the data move the list" — it starts from a curated prior and learns the factor that best explains co-expression in each cell type, splitting or pruning genes that do not behave coherently. This yields signatures that are both interpretable (anchored in prior knowledge) and faithful to the dataset.

## Formal notation

Spectra factorizes the expression matrix into cell-by-factor and factor-by-gene matrices under a penalty that pulls factor gene weights toward the prior gene-set graph, with cell-type-specific factor sets.

## Key variants

- Global (cell-type-agnostic) factors versus cell-type-specific factors.
- Use with knowledge-based immune priors (e.g. Cytopus) as the initialization graph.

## Known limitations

- Output quality depends on the quality and granularity of the input gene-program priors.
- Factor interpretation still requires manual inspection; factors can absorb technical structure if batch effects are uncorrected.

## Open problems

- Principled selection of factor number and prior weight.
- Integration with batch-corrected latent spaces versus raw counts.

## Relevance to active research

Used to refine inflammation-related immune signatures into 119 cell-type-specific factors for atlas-scale disease characterization, a building block of interpretable inflammation profiling across circulating immune cells.
