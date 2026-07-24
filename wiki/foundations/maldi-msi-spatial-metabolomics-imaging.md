---
title: "MALDI-MSI — matrix-assisted laser desorption/ionization mass spectrometry imaging (spatial metabolomics)"
slug: maldi-msi-spatial-metabolomics-imaging
domain: "spatial metabolomics / mass spectrometry imaging"
status: mainstream
aliases:
  - MALDI-MSI
  - matrix-assisted laser desorption/ionization mass spectrometry imaging
  - MALDI mass spectrometry imaging
  - MALDI imaging metabolomics
first_introduced: ""
date_updated: 2026-07-24
source_url: "https://doi.org/10.1016/j.cmet.2026.05.005"
---

## Definition

MALDI-MSI applies a chemical matrix to a tissue section and uses a rastered laser to desorb and ionize molecules from each pixel, reconstructing spatially resolved ion maps of metabolites, lipids, and other small molecules. Applied to metabolomics, it reports where specific low-mass metabolites (e.g. itaconate, ribose-5-phosphate, glutathione) physically localize within a tissue without prior tissue dissociation.

## Intuition

It is a metabolite camera: instead of a bulk average, it shows that a metabolite is enriched in one histological region and depleted in another. Overlaid on H&E, it can reveal that itaconate is confined to non-tumor lung tissue while PPP intermediates concentrate in tumor regions.

## Formal notation

Ion intensities are acquired per m/z per pixel, normalized to total ion count, and mapped with intensity color scales (low→high). Metabolic segmentation clusters pixels by spectral similarity to define tumor vs non-tumor metabolic regions.

## Key variants

- MALDI-MSI for glycomics ([[maldi-msi-spatial-glycomics]]) — same ionization, glycan coverage.
- AFADESI-MSI ([[afadesi-msi-spatial-metabolomics]]) — ambient ionization, no matrix.
- Single-cell / mass-guided MALDI imaging for higher spatial resolution.

## Known limitations

- Matrix choice biases which metabolite classes are detected.
- Spatial resolution and absolute quantification are limited relative to targeted LC-MS.
- Isobaric species require high mass resolution to disambiguate.

## Open problems

- Cell-type-resolved metabolite attribution within heterogeneous tissue.
- Registration of metabolite maps with adjacent-section transcriptomics.

## Relevance to active research

MALDI-MSI provided the founding observation of this study — the spatial depletion of endogenous itaconate within lung tumors and its restoration by 4-octyl itaconate — and mapped the mutually exclusive spatial distributions of itaconate and PPP metabolites ([[papers/irg1-itaconate-rewires-macrophage-lung-tumor]]).
