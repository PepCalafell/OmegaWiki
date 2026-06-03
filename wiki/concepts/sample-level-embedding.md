---
title: "Sample-level embedding"
aliases:
  - sample-level representation
  - sample embedding
first_introduced: "2025"
tags: [single-cell, multi-sample, representation-learning, translational]
maturity: emerging
key_papers:
  - reconstructing-developmental-disease-progression-sample-level
date_updated: 2026-06-03
related_concepts: [landmark-based-density-estimation, continuous-disease-progression-modeling]
---

## Definition

A sample-level embedding is a representation in which the fundamental unit of analysis is an entire sample (a patient, donor, or specimen) rather than an individual cell. Each sample's single-cell data is collapsed into a compact vector summarizing the distribution of its cells across cell-state space, so that distances between samples reflect differences in composition and cellular state.

## Intuition

Most single-cell pipelines embed *cells* and then compare groups of cells. But many translational questions — patient stratification, disease trajectory, treatment response — are about *samples*. A sample-level embedding answers "how does this whole patient's cellular landscape compare to others?" by treating the cloud of a sample's cells as one object.

## Formal notation

Given samples `s = 1..S`, each represented by a set of cells in a shared latent space, a sample-level embedding maps each sample to a vector `v_s ∈ R^d` such that a distance `D(v_i, v_j)` captures compositional and state differences. In scSLIDE, `v_s` is a normalized landmark-density profile and `D` is cosine distance.

## Variants

- Density-based (scSLIDE: landmark relative-density profile)
- Optimal-transport based ([[pilot-optimal-transport-patient-trajectory]])
- Cell-type proportion vectors (baseline)
- Latent variational ([[mrvi-multi-resolution-variational-inference]], [[scpoli-prototype-reference-mapping]])

## Comparison

Differs from per-cell embeddings (Seurat/scVI), which keep the cell as the unit, and from differential-abundance testing ([[milo-differential-abundance-testing]]), which performs binary condition contrasts rather than producing a reusable per-sample representation.

## When to use

When the dataset has many samples and the biology of interest lives at the sample level: patient clustering, continuous disease trajectories, outlier-sample detection, developmental pseudostage.

## Known limitations

- Sample-level batch effects (tissue handling, dissociation) are not yet corrected by current methods.
- Requires enough samples for sample-space structure to be meaningful.

## Open problems

- Cross-cohort/atlas integration at the sample level; scaling to tens of millions of cells.

## Key papers

- [[reconstructing-developmental-disease-progression-sample-level]] — introduces scSLIDE, a semi-supervised sample-level embedding framework.

## My understanding

This reframes single-cell analysis around the sample as the analytic atom. It is the natural complement to cell-level atlases now that datasets routinely contain hundreds of donors, and it is directly relevant to disease-progression and patient-stratification questions central to translational single-cell work.
