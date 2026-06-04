---
title: "Inflammation atlas of circulating immune cells"
aliases:
  - inflammation atlas
  - Inflammation Atlas
tags:
  - scRNA-seq
  - atlas
  - inflammation
  - PBMC
  - immunology
maturity: emerging
key_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
first_introduced: "Jiménez-Gracia et al. 2026 Nature Medicine (Inflammation Atlas)"
date_updated: 2026-06-04
related_concepts:
  - circulating-immune-cells-living-biomarkers
  - atlas-level-data-integration
---

## Definition

A cross-disease single-cell atlas of peripheral blood mononuclear cells (PBMCs) built to chart inflammatory processes of circulating immune cells across many diseases simultaneously. Rather than profiling one disease in isolation, it integrates dozens of studies into one harmonized embedding so that disease-specific and shared inflammatory cell states can be compared on common ground.

## Intuition

Inflammation is studied disease-by-disease, producing incompatible cell-state definitions. A single integrated atlas of circulating immune cells across infections, immune-mediated inflammatory diseases (IMIDs), chronic inflammation and solid tumors lets one ask which inflammatory programs are disease-specific and which are shared — and turns blood, a routinely sampled tissue, into a readout of systemic inflammation.

## Formal notation

Cells are embedded via a probabilistic generative model (scVI/scANVI) conditioned on diagnosis, sex and age; lineages and states are resolved by recursive top-down clustering into hierarchical annotation levels (Level 1 lineages, Level 2 states).

## Variants

- Main atlas versus held-out validation sets (unseen patients, unseen studies).
- Centralized single-center / single-chemistry subset for reduced batch confounding.

## Comparison

Distinct from tumor-microenvironment atlases and from cytokine-perturbation atlases: the unit of analysis here is the patient's circulating immune compartment across a broad disease spectrum, not a tissue or a perturbation panel.

## When to use

When the question is cross-disease comparison of systemic immune states, or when using circulating cells as a diagnostic substrate.

## Known limitations

- Most samples are of European ancestry.
- Nested batch effects (chemistry, center) confound cross-study generalization.

## Open problems

- Linking circulating immune states to tissue-resident inflammation.
- Building a single-chemistry, multi-center training atlas for clinical use.

## Key papers

- [[papers/interpretable-inflammation-landscape-circulating-immune-cells]] — defines the atlas (6.3M PBMCs, 1,047 patients, 19 diseases).

## My understanding

The durable contribution is treating the circulating immune compartment as a single, comparable system across diseases — a substrate for both biology (shared vs specific inflammatory programs) and diagnostics (living biomarkers). Its value scales with how well batch confounding can be controlled.
