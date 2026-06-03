---
title: "MALDI-MSI spatial glycomics"
slug: maldi-msi-spatial-glycomics
domain: spatial metabolomics
status: mainstream
aliases: ["MALDI-MSI", "MALDI imaging mass spectrometry", "spatial glycomics", "MALDI-TOF spatial glycomics", "mass spectrometry imaging glycans"]
first_introduced: "2017"
date_updated: 2026-06-03
source_url: "https://en.wikipedia.org/wiki/Mass_spectrometry_imaging"
---

## Definition

Matrix-Assisted Laser Desorption/Ionization Mass Spectrometry Imaging (MALDI-MSI) applied to glycans (spatial glycomics) measures the spatial distribution of N-linked glycans (and other metabolites) directly on a tissue section. A laser raster-scans the matrix-coated tissue; at each pixel a mass spectrum is acquired, yielding a spatially resolved map of glycan/metabolite abundances that can be co-registered with histology and other spatial omics modalities.

## Intuition

It adds a metabolite/glycan modality to spatial multiomics: where transcriptomics and proteomics report genes and proteins, MALDI-MSI reports the actual small-molecule and glycan landscape — capturing metabolic states (e.g. altered tyrosine/pyrimidine metabolism) that transcript abundance alone cannot reveal.

## Formal notation

Output is a pixel × m/z intensity tensor; glycan species are assigned by accurate mass and reference databases.

## Key variants

- N-glycan imaging (PNGase F on-tissue release)
- Lipid / metabolite MALDI-MSI
- Glycomics combined with on-tissue enzymatic digestion

## Known limitations

- Lower spatial resolution than imaging-based single-cell platforms; cell-type assignment is coarse
- Annotation of glycan species from m/z is non-trivial
- Sensitive to matrix application and tissue preparation

## Open problems

- Integrating glycan/metabolite layers with single-cell-resolution RNA/protein spatial data
- Standardised glycan identification and quantification

## Relevance to active research

Provides the metabolite/glycan arm of spatial multiomics, enabling joint pathway analysis (e.g. with MetaboAnalyst) to show enrichment of tyrosine and pyrimidine metabolism in melanoma communities.
