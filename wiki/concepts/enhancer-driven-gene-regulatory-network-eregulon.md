---
title: "Enhancer-driven gene regulatory network (eRegulon)"
aliases:
  - eRegulon
  - enhancer-driven GRN
tags: []
maturity: active
key_papers:
  - chinese-immune-multi-omics-atlas
first_introduced: ""
date_updated: 2026-06-04
related_concepts:
  - cell-type-specific-genetic-regulation-immune
---

## Definition

An enhancer-driven gene regulatory network models cell identity as a set of enhancer-linked regulatory units (eRegulons): a transcription factor, the accessible enhancer regions it binds, and the target genes whose expression correlates with that accessibility, inferred by integrating scRNA-seq and scATAC-seq.

## Intuition

Unlike expression-only TF–target regulons, eRegulons require both a chromatin-accessibility link (TF motif in an accessible enhancer) and a region-to-gene expression correlation, yielding more mechanistically grounded, cell type–specific networks.

## Formal notation

For a TF, eRegulon membership requires (i) motif enrichment in accessible regions and (ii) positive region-to-gene correlation; regions with negative correlations are removed. Activity per cell is scored by enrichment (e.g. AUC / regulon-specificity score, RSS).

## Variants

- Cell type–specific eRegulons (lineage TFs: PAX5/BACH2 in B cells, SPI1/CEBPB in monocytes, RUNX3/STAT4 in T cells)
- Age-associated GRNs (TFs whose activity rises with age)
- Sex-biased GRNs

## Comparison

Extends expression-only regulon inference ([[foundations/scenic-tf-regulon-inference]]) by adding the chromatin-accessibility layer; relies on motif analysis ([[foundations/homer-motif-enrichment-analysis]]) and RNA-ATAC integration ([[foundations/glue-multiomics-integration]]).

## When to use

To identify the TFs that encode immune cell identity and to track regulatory dynamics across differentiation, age, or sex.

## Known limitations

Inference from unpaired RNA/ATAC aliquots can introduce integration bias; region-to-gene links are correlational.

## Open problems

Validation against paired multiome and perturbation data.

## Key papers

- [[papers/chinese-immune-multi-omics-atlas]] — 404 eRegulons (237 high-quality) linking 84,625 regulatory regions to 13,645 target genes across 73 immune cell types.

## My understanding

The accessibility-grounded GRN is the bridge between the static cCRE catalog and the functional, cell type–specific regulatory logic of immune cells.
