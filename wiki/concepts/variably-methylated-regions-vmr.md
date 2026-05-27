---
title: "Variably Methylated Regions (VMRs)"
aliases:
  - "VMR"
  - "VMRs"
  - "variably methylated region"
  - "variably-methylated regions"
tags:
  - DNA-methylation
  - epigenetics
  - methylome-analysis
maturity: stable
key_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
first_introduced: "Kremer et al. *Nat. Methods* 2024 (MethSCAn)"
date_updated: 2026-05-27
related_concepts:
  - spatial-dmt-method
  - methylation-positive-coupling-gene-expression
---

## Definition

Variably Methylated Regions are genomic intervals whose CpG methylation level varies substantially across cells, pixels, samples, or conditions in a methylation dataset. VMRs are identified by computing per-region variance (or related dispersion statistic) of methylation and selecting the top-variable subset, analogous to highly variable genes (HVGs) in scRNA-seq.

## Intuition

In a methylome, most CpGs are either constitutively methylated (heterochromatin, gene bodies) or constitutively unmethylated (CpG-island promoters). The biologically informative signal lives in the small fraction of regions where methylation switches across conditions — VMRs. Restricting analysis to VMRs is the methylome analogue of HVG selection ([[foundations/hvg-selection-scrna]]): it suppresses constant background and exposes regulatory dynamics.

## Formal notation

- Per-region methylation: mean β over CpGs in window w (typical w = 1–3 kb).
- Variance / dispersion statistic across cells / pixels.
- Top-N VMRs by variance fed into PCA / UMAP / clustering.
- Tools: MethSCAn (Kremer 2024), methylpy, smfishtools.

## Variants

- **scVMR**: single-cell variable-methylation region, computed across cells in scBS-seq / sciMETv2 datasets.
- **Spatial VMR**: same logic applied to spatial pixels — used in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] to identify regions whose methylation differentiates anatomical clusters.
- **Tissue-comparison VMR**: identifies regions whose methylation varies between tissues / developmental stages.

## Comparison

- vs **DMR** (differentially methylated region): DMRs compare two predefined groups (case vs control). VMRs are computed agnostic to group labels — the variance is what defines the region.
- vs **CpG island / shore annotation**: anatomical / sequence-based, not data-driven.
- vs **HVG**: same statistical logic on a different modality.

## When to use

- Clustering single-cell / spatial methylomes.
- Identifying regulatory elements whose methylation marks cell-type identity.
- Pre-filtering for downstream motif enrichment / TF-binding analyses (HOMER on hypomethylated VMRs).

## Known limitations

- Definition is heuristic — choice of window size, dispersion metric, top-N cutoff all affect outputs.
- Coverage bias: VMRs are easier to call where CpG coverage is dense; sparse regions are systematically excluded.

## Open problems

- Statistical model for VMR significance (rather than top-N heuristic).
- Joint VMR / variable-accessibility / variable-gene region calling in spatial multi-omics data.

## Key papers

- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Lee et al. *Nature* 2025; uses spatial VMRs to define spatial methylome clusters, identify TF-motif enrichment at hypomethylated VMRs, and identify positive/negative VMR–gene-expression couplings.

## My understanding

VMRs are the practical entry point into any methylome analysis. In spatial-DMT they double as the bridge to mechanism: hypomethylated VMRs are enriched for TF-binding motifs corresponding to TFs actually expressed in that pixel cluster, providing direct in-tissue evidence of TF-driven local hypomethylation. The same regions can be tested for positive vs negative coupling to nearby gene expression — surfacing the canonical repressive coupling and the less-recognised positive coupling at enhancers / gene bodies / Polycomb targets.
