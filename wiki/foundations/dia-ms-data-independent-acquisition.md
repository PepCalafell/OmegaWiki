---
title: "DIA-MS — Data-Independent Acquisition Mass Spectrometry"
slug: dia-ms-data-independent-acquisition
domain: proteomics
status: mainstream
aliases:
  - DIA-MS
  - data-independent acquisition
  - DIA
  - SWATH-MS
  - DIA-PASEF
  - single-shot DIA proteomics
  - label-free DIA
first_introduced: "Venable et al. 2004; Gillet et al. 2012 SWATH"
date_updated: 2026-05-25
source_url: ""
---

## Definition
A mass spectrometry acquisition mode in which precursor ion windows of fixed width are sequentially co-isolated and fragmented, generating composite MS2 spectra that are deconvoluted post-acquisition against a spectral library to yield reproducible, label-free quantification of thousands of proteins per LC-MS run.

## Intuition
Unlike data-dependent acquisition (DDA), where only the most intense precursors are fragmented stochastically, DIA scans the full m/z range deterministically. The same peptides are interrogated in every run, eliminating much of the missing-value problem that plagues DDA proteomics.

## Formal notation
- Precursor window width: typically 10–25 m/z
- Cycle time: ~3 s for ~30–60 min gradients
- Quantification: chromatographic feature extraction against (real or predicted) DIA library

## Key variants
- Library-based DIA (Spectronaut, OpenSWATH)
- Library-free DIA via in-silico prediction (DIA-NN, MSFragger-DIA)
- DIA-PASEF on Bruker timsTOF — adds ion-mobility separation

## Known limitations
- Co-fragmented spectra reduce specificity; deconvolution depends on library quality.
- Per-sample depth typically below fractionated TMT workflows.
- FFPE inputs require optimised digestion to match FF performance.

## Open problems
- Universal cross-instrument DIA libraries.
- DIA at single-cell input level.

## Relevance to active research
DIA-MS is the workflow of choice for large-scale, cross-cohort proteomic studies including pan-cancer atlases (e.g., TPCPA), plasma biomarker discovery, and clinical-grade proteomics where reproducibility and throughput are prioritised over maximal depth.
