---
title: "Sci-Plex — massively multiplex chemical transcriptomics at single-cell resolution"
slug: sci-plex-chemical-transcriptomics
domain: data / single-cell
status: mainstream
aliases:
  - Sci-Plex
  - SciPlex
  - sci-Plex
first_introduced: "Srivatsan et al. 2020 Science (sci-Plex)"
date_updated: 2026-05-28
source_url: "https://www.science.org/doi/10.1126/science.aax6234"
---

## Definition

Sci-Plex is a single-cell combinatorial-indexing method ("nuclear hashing") that enables massively multiplexed chemical screens, profiling thousands of independent drug/dose perturbations across cell lines in a single experiment at single-cell resolution. It is a widely used benchmark for single-cell perturbation-response prediction.

## Intuition

Barcode each well/condition into the nuclei themselves, then pool everything for sequencing — so one run captures a whole chemical screen, cell by cell.

## Formal notation

n/a (assay/dataset).

## Key variants

- Different cell lines and compound/dose panels across sci-Plex releases.

## Known limitations

- Chemical perturbation effects are often subtle and hard to distinguish from batch noise (low signal-to-noise), making it a stringent prediction benchmark.

## Open problems

- Recovering subtle, dose-dependent regulatory shifts above technical noise.

## Relevance to active research

Used both as Flow-Model training data and as the low-signal benchmark where AlphaCell reports its largest fidelity advantage over VAE and set-based baselines (see [[claims/sciplex-baselines-fail-exceed-pearson-15]]).
