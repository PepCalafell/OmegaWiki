---
title: "gsMAP — genetics-to-spatial heritability mapping"
slug: gsmap-spatial-heritability
domain: statistical genetics
status: mainstream
aliases: ["gsMAP", "gsMap", "spatial heritability mapping", "GSS gene specificity score", "spatially-aware GWAS cell-type mapping"]
first_introduced: "2024"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1038/s41586-024-08223-0"
---

## Definition

gsMAP (Song et al., 2024) maps GWAS heritability of a trait onto spatial transcriptomics data, attributing genetic association signal to specific cell types and spatial domains. For each spot/cell it computes Gene Specificity Scores (GSS) — genes highly and specifically expressed in the local spatial neighbourhood — maps SNPs to those genes by linkage-disequilibrium distance to transcription start sites, and tests the cumulative heritability captured (via stratified LD score regression and Cauchy P-value aggregation) relative to baseline SNPs.

## Intuition

A GWAS tells you which SNPs associate with a disease but not *where in the tissue* or *in which cells* that risk is realised. gsMAP overlays population-scale genetic association onto deeply profiled spatial maps, so heritability can be assigned to, e.g., melanocytes, dysplastic keratinocytes, or fibroblasts at specific tissue locations — connecting heritability to cellular mechanism.

## Formal notation

For each spot s: GSS(s,g) for genes g; SNPs mapped to g by LD/distance; heritability enrichment τ(s) estimated by S-LDSC; region/cell-type significance by Cauchy-aggregated P over constituent spots/cells.

## Key variants

- Cell-type-level vs spatial-domain-level aggregation
- Correlation of GSS with per-cell-type GWAS P to nominate genetic ligand–receptor pairs

## Known limitations

- Depends on spatial reference quality and marker-gene specificity
- LD-based SNP-to-gene mapping inherits assignment errors
- Requires well-powered GWAS summary statistics

## Open problems

- Causal interpretation beyond enrichment
- Integration with chromatin/regulatory annotations for mechanism

## Relevance to active research

Bridges population genetics and spatial single-cell biology, allowing heritability of complex traits (e.g. cSCC, BCC, melanoma risk) to be localised to spatial cell types and even to ligand–receptor interactions.
