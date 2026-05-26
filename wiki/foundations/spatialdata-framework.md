---
title: "SpatialData — open framework for spatial omics data"
slug: spatialdata-framework
domain: "methods / spatial-omics / software"
status: mainstream
aliases:
  - SpatialData
  - Marconato SpatialData
  - scverse SpatialData
  - spatial omics data framework
  - SpatialData AnnData
  - SpatialData universal format
  - spatial omics on-disk format
first_introduced: "Marconato et al. 2025 Nature Methods"
date_updated: 2026-05-26
source_url: "https://github.com/scverse/spatialdata"
---

## Definition

SpatialData is a unified on-disk + in-memory format for spatial omics data (transcriptomics, proteomics, multiplexed imaging, H&E), extending AnnData with spatial coordinates, images, shapes, and points. Foundation of the scverse spatial-omics ecosystem.

## Strengths

- Cross-platform standard format.
- Lazy loading of large image/transcript datasets.

## Known limitations

- Adoption still growing across legacy tools.

## Relevance to active research

Native input/output format used by [[papers/novae-graph-based-foundation-model-spatial]] and the surrounding scverse spatial-omics tooling.
