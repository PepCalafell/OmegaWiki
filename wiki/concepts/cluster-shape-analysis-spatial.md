---
title: "Cluster shape characterization in spatial omics (curl, elongation, linearity, purity)"
aliases:
  - cluster shape analysis
  - spatial cluster morphology
  - cluster shape descriptors
  - curl elongation linearity purity
  - cluster boundary shape
  - cluster component shape descriptors
  - tissue niche morphology
  - cluster shape comparison
  - spatial cluster shape comparison
  - cluster shape disease vs healthy
maturity: emerging
tags:
  - spatial-omics
  - morphology
  - methodology
  - tissue-architecture
key_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
first_introduced: "Varrone et al. 2024 *Nat. Genet.* (CellCharter)"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/cluster-neighborhood-enrichment-spatial]]"
---

## Definition

A family of geometric descriptors of spatial-cluster connected components: **curl** (degree of twisting), **elongation** (ratio of major to minor axis of the bounding box), **linearity** (how well the component approximates a linear path), and **purity** (fraction of cells inside the cluster boundary that actually belong to that cluster).

## Intuition

Combinations of these four scores classify cluster components as linear (e.g., vessels, trabeculae), round (germinal centres), circular (rings), or irregular (disrupted architecture). Comparing the same cluster across conditions surfaces tissue remodelling — e.g., loss of linearity and gain of curl in lupus spleen indicates loss of normal anatomical architecture.

## Use

- Distinguish anatomically defined niches that share cell-type composition but differ in geometry.
- Quantify tissue remodelling between conditions (healthy vs disease, untreated vs treated).
- Complement cluster cell-type enrichment and cluster NE with shape-level evidence.

## Known limitations

- Definitions depend on a robust boundary / bounding-box estimator; small components are noisy.
- Less interpretable in 3D / volumetric tissue slabs.

## Relevance to active research

[[papers/cellcharter-reveals-spatial-cell-niches-associated]] uses these four descriptors to show that B-PALS boundary and B-follicle clusters significantly gain curl and lose linearity in MRL-lupus mouse spleen, providing a quantitative readout of tissue-architecture disruption beyond cluster proportions.
