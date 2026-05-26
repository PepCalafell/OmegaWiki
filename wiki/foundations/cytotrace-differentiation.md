---
title: "CytoTRACE — single-cell differentiation state predictor"
slug: cytotrace-differentiation
domain: single-cell genomics / methods
status: mainstream
aliases:
  - CytoTRACE
  - cellular trajectory reconstruction
  - differentiation score scRNA-seq
  - gene-count-based stemness
  - Gulati et al. CytoTRACE
  - Stanford CytoTRACE
  - CytoTRACE 2
first_introduced: "2020"
date_updated: 2026-05-26
source_url: "https://cytotrace.stanford.edu/"
---

## Definition

CytoTRACE is an unsupervised method that ranks single cells by predicted differentiation state using gene count diversity per cell as a proxy for transcriptional plasticity / stemness.

## Intuition

Less-differentiated cells tend to express a broader repertoire of transcripts than terminally differentiated ones. CytoTRACE leverages this rank-order signal without requiring known markers, complementing pseudotime methods that need a root cell.

## Relevance to active research

Used by Peng et al. 2026 ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) to position KACs/RPII between AT2 and invasive tumor cells along the LUAD differentiation continuum, supporting their progenitor role.
