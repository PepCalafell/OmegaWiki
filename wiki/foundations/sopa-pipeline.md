---
title: "Sopa — technology-invariant pipeline for image-based spatial omics"
slug: sopa-pipeline
domain: "methods / spatial-omics / software"
status: mainstream
aliases:
  - Sopa
  - SOPA pipeline
  - Blampey Sopa
  - technology-invariant spatial omics pipeline
  - Sopa Xenium MERSCOPE CosMx
  - Sopa segmentation pipeline
  - scverse Sopa
first_introduced: "Blampey et al. 2024 Nature Communications"
date_updated: 2026-05-26
source_url: "https://github.com/gustaveroussy/sopa"
---

## Definition

Sopa is a unified, technology-invariant pipeline for image-based spatial omics, handling segmentation, transcript assignment, and downstream analysis across Xenium, MERSCOPE, CosMx, and related platforms. It is part of the scverse ecosystem and serves as the upstream data layer for downstream tools like Novae.

## Strengths

- Single API across multiple imaging-based platforms.
- scverse / SpatialData compatible.

## Known limitations

- Imaging-based only — does not cover NGS spatial transcriptomics (Visium).

## Relevance to active research

Authored by the same group as [[papers/novae-graph-based-foundation-model-spatial]] and used as the upstream preprocessing pipeline for many of Novae's training datasets.
