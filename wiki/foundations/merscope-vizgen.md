---
title: "MERSCOPE — Vizgen MERFISH-based commercial spatial transcriptomics platform"
slug: merscope-vizgen
domain: "technologies / spatial-transcriptomics / imaging-based"
status: mainstream
aliases:
  - MERSCOPE
  - Vizgen MERSCOPE
  - MERFISH commercial
  - Chen Boettiger MERFISH
  - Vizgen platform
  - MERSCOPE imaging spatial transcriptomics
  - 500-plex MERSCOPE
  - subcellular spatial transcriptomics MERSCOPE
first_introduced: "Chen, Boettiger, Moffitt, Wang & Zhuang 2015 Science (MERFISH); Vizgen commercial release MERSCOPE 2021"
date_updated: 2026-05-26
source_url: "https://vizgen.com/products/"
---

## Definition

MERSCOPE is Vizgen's commercial implementation of MERFISH (multiplexed error-robust fluorescence in situ hybridization), an imaging-based spatial transcriptomics platform delivering subcellular resolution across hundreds of genes (currently up to ~500-plex). It is one of the three main imaging-based subcellular spatial transcriptomics technologies, alongside [[foundations/xenium-in-situ-spatial-transcriptomics]] and [[foundations/cosmx-spatial-transcriptomics]].

## Strengths

- Subcellular resolution; preserves true single-cell spatial context.
- Robust to optical errors via barcoded sequential hybridization.

## Known limitations

- Limited panel size compared to NGS-based spatial transcriptomics (Visium).
- Panel locking introduces cross-platform / cross-panel batch effects motivating panel-invariant methods like Novae.

## Relevance to active research

Together with Xenium and CosMx, MERSCOPE forms the foundation-model training corpus of [[papers/novae-graph-based-foundation-model-spatial]] (78 slides, ~30M cells, 18 tissues across the three platforms).
