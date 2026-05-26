---
title: "iStar — spatial transcriptomics super-resolution"
slug: istar-spatial-resolution-enhancement
domain: spatial transcriptomics / methods
status: mainstream
aliases:
  - iStar
  - inferring super-resolution tissue architecture
  - super-pixel ST
  - spatial resolution enhancement
  - histology-guided ST super-resolution
  - Zhang et al. iStar
  - super-resolved spatial transcriptomics
  - super-pixel resolution
first_introduced: "2024"
date_updated: 2026-05-26
source_url: "https://www.nature.com/articles/s41587-023-02019-9"
---

## Definition

iStar is a deep-learning method that enhances the spatial resolution of spot-level [[foundations/10x-visium-spatial-transcriptomics]] by predicting gene expression at super-pixel resolution from paired H&E histology, transferring tissue morphology into the molecular embedding space.

## Intuition

Standard Visium spots are ~55 µm in diameter and contain mixtures of cells. iStar uses histology features as a high-resolution prior to interpolate gene expression below the spot footprint, exposing patterns (e.g., a thin band of IL1R1 at the invasive edge) that would be invisible at spot resolution.

## Relevance to active research

Used by Peng et al. 2026 ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) to map epithelial meta-programs, IL1B/IL1R1 expression, and KAC signatures at super-pixel resolution across human and mouse Visium ST data.
