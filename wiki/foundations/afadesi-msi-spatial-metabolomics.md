---
title: "AFADESI-MSI — air flow-assisted desorption electrospray ionization mass spectrometry imaging"
slug: "afadesi-msi-spatial-metabolomics"
domain: "spatial metabolomics / mass spectrometry imaging"
status: mainstream
aliases:
  - "AFADESI-MSI"
  - "air flow-assisted desorption electrospray ionization"
  - "AFADESI mass spectrometry imaging"
first_introduced: "2013"
date_updated: 2026-07-23
source_url: "https://doi.org/10.1021/ac400009s"
---

## Definition

AFADESI-MSI is an ambient mass-spectrometry-imaging technique that sprays a charged solvent onto a tissue section and uses an assisting air flow to transport desorbed ions into the mass spectrometer, generating spatially resolved metabolite maps without matrix application. It captures small molecules (metabolites, lipids, drugs) across a tissue while preserving their spatial coordinates.

## Intuition

Where transcriptomics tells you which genes are on in a spot, AFADESI-MSI tells you which metabolites are physically present there. Run on an adjacent section and aligned to spatial transcriptomics, it lets one overlay "lactic acid and PGE2 are high here" onto "angiogenic TAM signature is high here."

## Formal notation

Ion images are reconstructed per m/z; abundances are total-ion-count normalised per pixel and compared across spatial clusters by log fold-change with Wilcoxon/Benjamini–Hochberg testing.

## Key variants

- DESI-MSI (classic, no assisting air flow).
- MALDI-MSI ([[maldi-msi-spatial-glycomics]]) — matrix-based, higher spatial resolution, different molecular coverage.
- Positive- and negative-ion acquisition modes capture complementary metabolite classes.

## Known limitations

- Spatial resolution (~100 µm scan step) is coarser than imaging transcriptomics.
- Ambient ionisation biases toward readily desorbed/ionised species; absolute quantification is difficult.
- Requires an adjacent-section alignment step to pair with transcriptomics, introducing registration error.

## Open problems

- Robust point-to-point registration of metabolomic and transcriptomic sections.
- Cell-type-resolved metabolite attribution within a heterogeneous spot.

## Relevance to active research

AFADESI-MSI supplied the spatial-metabolomics arm that linked FAO intermediates to MHC-II+ TAM niches and lactic acid / prostaglandins to angiogenic TAM niches in human NSCLC, integrated with Visium transcriptomics via [[multivi-multimodal-integration]] and [[cellcharter-framework]].
