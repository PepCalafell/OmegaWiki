---
title: "Landmark-based density estimation"
aliases:
  - landmark density quantification
  - landmark abundance matrix
first_introduced: "2025"
tags: [single-cell, density-estimation, multi-sample]
maturity: emerging
key_papers:
  - reconstructing-developmental-disease-progression-sample-level
date_updated: 2026-06-03
related_concepts: [sample-level-embedding]
---

## Definition

Landmark-based density estimation summarizes how a sample's cells are distributed across a high-dimensional embedding by quantifying, for a fixed set of reference "landmark" cells, how densely each sample's cells fall in the neighbourhood of each landmark. The result is a sample-by-landmark matrix of local densities.

## Intuition

Estimating a full continuous density in high dimensions is intractable, so instead we anchor on a representative set of landmark points spanning the manifold and just count how concentrated each sample is around each anchor. The vector of densities over landmarks becomes a fingerprint of the sample's cellular distribution.

## Formal notation

Select L landmark cells (via [[geometric-sketching]]). For each cell, find its k-nearest landmarks; aggregate across all cells of sample s to get raw abundance `A_{s,l}`. Normalize with a chi-square-style transform: `R_{s,l} = (A_{s,l} - E_{s,l}) / sqrt(E_{s,l})`, where `E_{s,l}` is the expected count from row/column marginals — yielding relative-density residuals.

## Variants

- Choice of landmark count (scSLIDE uses ~5,000; robust across a range).
- Kernel/KDE-based density ([[gaussian-kernel-density-estimation]]) vs nearest-landmark counting.

## Comparison

Related to KDE but made scalable by restricting evaluation to a sketched landmark set; related to [[milo-differential-abundance-testing]]'s neighbourhood density but used to *summarize* a sample rather than test conditions.

## When to use

As the bridge step that turns a cell-level embedding into a [[sample-level-embedding]].

## Known limitations

- Density estimate inherits the quality and supervision of the underlying embedding.
- Landmark coverage of rare states depends on the sketching method.

## Open problems

- Principled landmark-count selection; robustness to extreme compositional outliers.

## Key papers

- [[reconstructing-developmental-disease-progression-sample-level]] — landmark relative-density matrix as the core of scSLIDE.

## My understanding

A pragmatic, scalable substitute for full high-dimensional density estimation. The chi-square residual normalization is what makes the resulting profiles comparable across samples of differing size and composition.
