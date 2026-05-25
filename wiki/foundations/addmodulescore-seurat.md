---
title: "AddModuleScore (Seurat) — per-cell gene-set average expression score"
slug: addmodulescore-seurat
domain: "methods / scRNA-seq"
status: mainstream
aliases:
  - "AddModuleScore"
  - "Seurat AddModuleScore"
  - "module score Seurat"
  - "gene module score scRNA"
  - "Tirosh module score"
first_introduced: "Tirosh et al. 2016 Science (melanoma scRNA-seq); implemented in Seurat as `AddModuleScore`"
date_updated: 2026-05-25
source_url: "https://satijalab.org/seurat/reference/addmodulescore"
---

## Definition

A per-cell gene-set scoring function in the Seurat package: average expression of the gene set in each cell is corrected by subtracting the mean expression of a matched random control gene set (typically 100 control sets matched on expression bin), yielding a centred per-cell score.

## Intuition

A simple mean expression of a gene set is biased by per-cell depth and by gene expression-level distribution. Subtracting the average of expression-matched random controls removes most of this bias and produces a centred score interpretable as "above or below background for this signature."

## Formal notation

- For gene set S in cell c: score(c) = mean(expr(S, c)) − mean(expr(control_set, c)).
- Control set: 100 (default) randomly sampled, expression-bin-matched genes.

## Key variants

- AUCell, UCell, VISION — alternative single-cell gene-set scoring methods.
- ssGSEA on pseudo-bulks — coarser but related.

## Known limitations

- Sensitive to control-set composition; results vary slightly across random seeds.
- Does not normalise to a calibrated effect size.

## Open problems

- Calibrated significance testing for AddModuleScore.

## Relevance to active research

AddModuleScore is one of two methods (alongside AUCell) used to compute per-cell hypoxia scores from the MSigDB Hallmark Hypoxia gene set in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]], underpinning the identification of the hypoxia-responsive macrophage subcluster.
