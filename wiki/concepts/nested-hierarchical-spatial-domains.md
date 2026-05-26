---
title: "Nested hierarchical spatial domains"
slug: nested-hierarchical-spatial-domains
domain: "methods / spatial-transcriptomics / clustering"
maturity: emerging
tags: []
aliases:
  - nested spatial domains
  - hierarchical spatial domain assignment
  - multi-resolution spatial niches
  - hierarchical spatial niche detection
  - tree of spatial domains
  - prototype hierarchy spatial
  - resolution-controlled spatial domains
  - cluster hierarchy spatial transcriptomics
  - multi-scale spatial domain
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

A representation in which spatial domains are organised as a nested hierarchy, so that the same underlying model can deliver coarse-to-fine spatial labels by collapsing or expanding the hierarchy without re-running clustering. Distinct from running a flat clustering at multiple resolutions because the hierarchy is built once and consistent across resolutions.

## Why it matters

Spatial-omics studies routinely require multi-resolution analysis: large compartments (tumor, stroma, immune) at coarse level, microenvironments at intermediate, niches at fine. Flat methods (Leiden, mclust) require re-clustering at each resolution, breaking consistency and adding compute. A nested hierarchy lets the user switch resolution at near-zero cost while keeping label consistency.

## Key open questions

- Optimal branching factor and depth as a function of dataset diversity.
- Stability of the hierarchy under fine-tuning / new-tissue addition.

## Status today

Implemented in [[papers/novae-graph-based-foundation-model-spatial]] via clustering of learnt prototypes; complementary to flat stability-based hierarchies in [[concepts/spatial-domain-detection-from-svg]] and to the n=3/8/20 stable-solution hierarchy used by [[foundations/cellcharter-framework]].
