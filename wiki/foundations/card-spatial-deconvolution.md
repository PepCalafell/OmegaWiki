---
title: "CARD — Conditional autoregressive deconvolution for ST spots"
slug: card-spatial-deconvolution
domain: methods/spatial-transcriptomics
status: mainstream
aliases:
  - CARD
  - CARD deconvolution
  - CARD_deconvolution
  - spatial spot cell-type deconvolution
  - conditional autoregressive ST
  - reference-based ST deconvolution
  - CARD R package
first_introduced: "Ma 2022 Nat Biotechnol"
date_updated: 2026-05-22
source_url: "https://yma-lab.github.io/CARD/"
---

## Definition
CARD performs cell-type deconvolution of spatial transcriptomics spots by combining a single-cell reference with a conditional autoregressive prior that explicitly models spatial autocorrelation between neighbouring spots.

## Intuition
Adjacent ST spots usually share cell-type composition; a spatial prior reduces noise and produces smoother, biologically plausible deconvolution maps relative to spot-independent methods.

## Key variants
- Reference-based CARD (default)
- Reference-free CARDfree
- Single-cell resolution variant CARD-SR

## Known limitations
- Sensitive to reference choice and annotation granularity
- Computationally expensive on large tissue sections
- Strong spatial prior can smooth away genuinely rare local cell types

## Open problems
- Joint deconvolution across multiple slides without batch confounding
- Quantitative comparison against newer probabilistic ST deconvolution methods

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] uses CARD to call malignant spots (proportion > 0.99) and to assign non-cancer cell types to neighbouring spots for niche analysis.
