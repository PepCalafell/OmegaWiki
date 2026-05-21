---
title: "10x Genomics Visium — sequencing-based spatial transcriptomics"
slug: 10x-visium-spatial-transcriptomics
domain: spatial-transcriptomics
status: mainstream
aliases:
  - Visium
  - 10x Visium
  - 10x Genomics Visium
  - spatial Visium
  - Visium platform
  - sequencing-based spatial transcriptomics
  - barcoded spot ST
  - ST array
first_introduced: "Ståhl et al. 2016 Science / 10x Genomics 2019"
date_updated: 2026-05-21
source_url: "https://www.10xgenomics.com/products/spatial-gene-expression"
---

## Definition

10x Visium is a commercial sequencing-based spatial transcriptomics platform. It deposits a tissue section onto a slide tiled with barcoded capture spots (~55 µm diameter, ~100 µm centre-to-centre), polyadenylated mRNAs hybridise to spot-specific spatial barcodes, and downstream sequencing reconstructs a (spot × gene) count matrix with paired x-y coordinates.

## Intuition

Spots contain multiple cells (typically 1–10), so Visium provides spot-resolution (not single-cell) expression with whole-transcriptome coverage. This complements imaging-based platforms (MERFISH, seqFISH) which are subcellular but limited to 30–300 gene panels.

## Key variants

- Visium FFPE — formalin-fixed paraffin-embedded compatibility (probe-based).
- Visium HD — finer resolution barcoded grid (2 µm).
- DLPFC dataset (Maynard et al.), HER2-positive breast tumour dataset (Andersson et al.), and HPV-negative OSCC datasets are common Visium benchmarks for spatial-domain detection.

## Known limitations

- Sub-single-cell resolution requires paired scRNA-seq deconvolution.
- Capture efficiency lower than scRNA-seq; many lowly expressed genes show zeros at most spots.

## Relevance to active research

Visium is the dominant sequencing-based ST platform in the [[papers/systematic-benchmarking-computational-methods-identify-spatially]] SVG benchmark (20 of 50 datasets) and is the standard input for SVG detection and spatial-domain-detection pipelines.
