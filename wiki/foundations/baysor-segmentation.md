---
title: "Baysor — transcript-based cell segmentation for imaging spatial transcriptomics"
slug: baysor-segmentation
domain: "methods / spatial-transcriptomics / cell-segmentation"
status: mainstream
aliases:
  - Baysor
  - Baysor segmentation
  - Petukhov Baysor
  - transcript-based cell segmentation
  - molecule-based segmentation MERFISH
  - cell boundary inference spatial transcriptomics
  - Baysor MRF segmentation
first_introduced: "Petukhov et al. 2022 Nature Biotechnology"
date_updated: 2026-05-26
source_url: "https://github.com/kharchenkolab/Baysor"
---

## Definition

Baysor performs cell segmentation in imaging-based spatial transcriptomics directly from transcript molecule positions, using a Markov random field that does not require a nuclear/membrane stain image. It supports priors from staining-based segmentation when available.

## Strengths

- Does not require a high-quality DAPI / membrane stain.
- Resolves cells in transcript-dense regions where staining segmentation fails.

## Known limitations

- More computationally expensive than staining-based segmentation.
- Quality depends on transcript density.

## Relevance to active research

Used to test robustness of [[papers/novae-graph-based-foundation-model-spatial]] to alternative segmentation methods (vs the default 10x Genomics staining-based pipeline); Novae recovers nearly identical spatial domains under either segmentation, supporting the claim that spatial domains are insensitive to segmentation choice.
