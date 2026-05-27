---
title: "ResolVI — deep-learning correction of transcript misassignment in subcellular spatial transcriptomics"
slug: resolvi-spatial-transcript-correction
domain: "computational-biology / methods / spatial-omics"
status: mainstream
aliases:
  - "ResolVI"
first_introduced: "Boyeau et al. 2024 (preprint); scVI-tools spatial extension"
date_updated: 2026-05-27
source_url: "https://github.com/scverse/scvi-tools"
---

## Definition

ResolVI is a deep-learning model that corrects for transcript diffusion and segmentation errors in subcellular-resolution spatial transcriptomics platforms (MERFISH, CosMx, Xenium). It probabilistically reassigns wrongly attributed transcripts back to their most likely cell-of-origin, improving cell-type annotation accuracy in dense or noisy regions.

## Intuition

In imaging-based spatial transcriptomics, transcripts near a cell boundary can be assigned to the wrong cell due to optical and segmentation noise. ResolVI uses neighbourhood gene-expression context to "denoise" the transcript-to-cell mapping.

## Key variants

- Plug-in for MERFISH / CosMx / Xenium pipelines
- Companion to ResolVI-trained downstream cell-type classifiers

## Known limitations

- Requires reasonable initial segmentation to bootstrap
- Trade-off between aggressive reassignment and signal smoothing
- Less validated on lower-plex panels (<200 genes)

## Relevance to active research

Applied in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]] on a 1.86 M-cell MERFISH atlas of breast, lung, colorectal and ovarian tumors to correct mis-assigned transcripts and derive accurate immune-cell-type spatial maps for TAM-T proximity analyses.
