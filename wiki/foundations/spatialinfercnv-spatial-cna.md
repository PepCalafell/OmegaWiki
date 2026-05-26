---
title: "SpatialInferCNV — spatial copy number alteration inference"
slug: spatialinfercnv-spatial-cna
domain: spatial genomics / methods
status: mainstream
aliases:
  - SpatialInferCNV
  - spatial inferCNV
  - spot-level CNA inference
  - ST CNA inference
  - Visium-based CNV calling
  - spatial copy number alterations
  - spatial phylogeny from ST
first_introduced: "2023"
date_updated: 2026-05-26
source_url: "https://github.com/aerickso/SpatialInferCNV"
---

## Definition

SpatialInferCNV adapts [[foundations/infercnv-cnv-scrna]] to [[foundations/10x-visium-spatial-transcriptomics]] data, inferring genome-wide copy number alterations per spot and enabling reconstruction of spatially resolved clonal architectures and phylogenies.

## Known limitations

Visium spots are mixtures of tumor and non-tumor cells, lowering signal-to-noise of CNA calls and risking clonal misassignment. Peng et al. 2026 ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) cross-validate inferred CNAs against paired snRNA-seq and WES.

## Relevance to active research

Provides the spatial backbone for clonal-architecture analyses that link genomic evolution (CNAs, KRAS/EGFR/MET driver mutations) to tissue topology in lung precursor lesions.
