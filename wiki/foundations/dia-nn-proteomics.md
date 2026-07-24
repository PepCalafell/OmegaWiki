---
title: "DIA-NN — data-independent acquisition by neural networks"
slug: dia-nn-proteomics
domain: "proteomics / computational methods"
status: mainstream
aliases:
  - "DIA-NN"
  - "DIANN"
  - "Data-Independent Acquisition by Neural Networks"
first_introduced: "Demichev et al. 2020 (Nat Methods)"
date_updated: 2026-07-24
source_url: "https://github.com/vdemichev/DiaNN"
---

## Definition

DIA-NN is a software suite for processing data-independent acquisition (DIA) mass-spectrometry proteomics. It uses deep neural networks for peptide identification and quantification and supports library-free analysis (spectral libraries predicted in silico), enabling deep, reproducible proteome quantification from DIA runs.

## Intuition

Where DDA sequences peptides one at a time, DIA fragments everything in wide m/z windows; DIA-NN is the engine that untangles those multiplexed spectra — using neural networks and (optionally) a self-generated library — into confident, cross-run-normalized protein quantities.

## Formal notation

- Input: Orbitrap DIA raw files (e.g. Q Exactive HF-X)
- Library-free / double-pass mode: build spectral library from the DIA runs, then re-search
- Output filtered at 1% precursor FDR; protein inference at the gene level using proteotypic peptides
- MaxLFQ cross-run normalization; downstream processing in Perseus / R

## Key variants

- Alternative proteomics pipelines: MaxQuant ([[maxquant-proteomics]]) for DDA; Spectronaut for DIA
- Related DIA proteomics approaches in the vault: [[dia-ms-pan-cancer-proteomics-approach]]

## Known limitations

- DIA quantification depth depends on chromatographic gradient and instrument; low-abundance proteins still under-sampled
- Library-free predictions can miss non-canonical or heavily modified peptides
- Match-between-runs and neural-network scoring require careful FDR control

## Open problems

- Standardization of DIA-NN settings for reproducible cross-study proteome comparisons

## Relevance to active research

Analysis engine for the LC-MS/MS DIA proteomics that defined the HIF-1α-dependent protein-expression signatures in Huh7 and HeLa cells. Relevant to proteomics methodology across the vault.
