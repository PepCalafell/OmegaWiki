---
title: "AUCell — per-cell gene set activity scoring"
slug: aucell-gene-set-activity
domain: "methods / scRNA-seq"
status: mainstream
aliases:
  - "AUCell"
  - "AUCell R package"
  - "per-cell AUC gene-set scoring"
  - "AUCell SCENIC"
  - "single-cell gene set activity AUC"
first_introduced: "Aibar et al. 2017 Nature Methods (SCENIC); AUCell distributed in the SCENIC toolkit"
date_updated: 2026-05-25
source_url: "https://bioconductor.org/packages/release/bioc/html/AUCell.html"
---

## Definition

An R/Bioconductor package that scores per-cell activity of a gene set by computing the area under the recovery curve (AUC) of the gene set against the per-cell gene ranking. Originally distributed with SCENIC for regulon activity scoring; widely adopted for arbitrary gene-set scoring (hypoxia, IFN response, exhaustion, etc.).

## Intuition

Rather than summing or averaging expression across a gene set, AUCell uses each cell's *gene ranking* and asks: how high in this cell's transcriptome do the gene-set members concentrate? This is robust to per-cell sequencing depth differences.

## Formal notation

- Inputs: per-cell expression matrix; one or more gene sets.
- For each cell: rank all genes by expression; compute AUC of the recovery curve over the top X% of genes (typically top 5–10%).
- Outputs: cell × gene-set AUC matrix; optional binarisation by AUC threshold.

## Key variants

- AUCell vs `AddModuleScore` (Seurat): different scoring rules but used interchangeably for hypoxia / IFN signatures.
- AUCell vs UCell: UCell uses Mann–Whitney U on ranks.

## Known limitations

- Sensitive to gene-set size and per-cell depth distribution.
- Threshold-based binarisation is heuristic.

## Open problems

- Calibrated per-cell p-values for AUCell scores.

## Relevance to active research

AUCell is one of two methods (alongside `AddModuleScore`) used to compute per-cell hypoxia scores in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] for identifying the hypoxia-responsive macrophage subcluster.
