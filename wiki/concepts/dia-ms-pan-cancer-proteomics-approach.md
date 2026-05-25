---
title: "Single-shot DIA-MS as a pan-cancer proteomics approach"
aliases:
  - DIA-MS proteomics
  - data-independent acquisition mass spectrometry
  - single-shot LC-MS proteomics
  - single-shot proteomics
  - DIA mass spectrometry
  - SWATH-MS pan-cancer
  - DIA proteome profiling
  - label-free DIA proteomics
  - bulk-tissue DIA-MS
  - pan-cancer mass spectrometry
  - DIA-PASEF proteomics
tags: [proteomics, dia-ms, methods, pan-cancer, single-shot]
maturity: active
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: ""
date_updated: 2026-05-25
related_concepts: []
---

## Definition
Single-shot data-independent acquisition mass spectrometry (DIA-MS) is a label-free, multiplexing-free proteomic acquisition strategy in which precursor windows are sequentially co-isolated and fragmented, allowing reproducible quantification of ~5,000–8,000 proteins per sample from a single LC-MS run.

## Intuition
DIA-MS replaces the stochastic peptide selection of DDA with deterministic window scanning. Compared to TMT-based multiplexing, DIA removes the constraint that all multiplexed samples must be batched together — a critical enabler for pan-cancer or cross-cohort designs where balanced batching is infeasible.

## Formal notation
- Acquisition: precursor windows scanned sequentially across the m/z range
- Quantification: chromatogram-based extraction against a spectral library (or in-silico predicted library)
- Throughput: ~30–60 min per sample with standard nanoflow LC

## Variants
- Library-based vs library-free DIA
- DIA-PASEF (Bruker timsTOF) for ion-mobility-enhanced DIA
- SWATH-MS (Sciex) — early DIA implementation

## Comparison
- vs **TMT**: deeper proteomes per batch, but multiplexing limits group balance for many cohorts.
- vs **DDA**: more reproducible peptide identifications across samples, lower missingness.
- vs **RPPA**: orders of magnitude more proteins, but requires more sample input.

## When to use
- Cross-cohort, cross-tissue, large-scale proteomic studies
- When sample groups exceed the number of available TMT channels
- When inter-batch comparability is critical (e.g., pan-cancer atlases)

## Known limitations
- Per-sample depth is below fractionated TMT workflows.
- Library quality determines coverage of low-abundance proteins in some DIA pipelines.

## Open problems
- Standardisation of DIA pipelines across labs.
- Direct DIA on FFPE / formalin-fixed inputs at full sensitivity.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
DIA-MS is the natural fit for atlas-scale proteomics: single-shot, label-free, comparable across batches. The TPCPA paper demonstrates that cancer-type biology survives the depth–multiplexing tradeoff.
