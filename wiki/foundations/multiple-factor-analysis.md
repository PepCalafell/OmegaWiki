---
title: "Multiple Factor Analysis (MFA)"
slug: multiple-factor-analysis
domain: "statistics / multivariate analysis / methods"
status: mainstream
aliases:
  - "MFA"
  - "Multiple Factor Analysis"
  - "MFA compromise"
first_introduced: "Escofier and Pagès 1990; Abdi, Williams & Valentin 2013 *WIREs Comp Stat*"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1002/wics.1246"
---

## Definition

Multiple Factor Analysis is a multi-table dimensionality-reduction method that analyzes several groups of variables (tables) measured on the same observations. Each table is first analyzed by its own generalized PCA, then normalized by the inverse of its first singular value so that no single table dominates the global solution, after which the normalized tables are concatenated and a final GPCA produces a common low-dimensional representation called the *MFA compromise*.

## Intuition

MFA answers "what structure is shared across many related measurement blocks?" while letting each block contribute on a comparable scale. The first-singular-value normalization prevents a high-variance table from swamping the rest, so tables with different scales or numbers of variables can be combined fairly.

## Formal notation

- Inputs: K tables X₁…X_K, each observations × variables, sharing the same rows.
- Step 1: GPCA of each Xₖ → first singular value σₖ.
- Step 2: rescale each table by 1/σₖ.
- Step 3: concatenate rescaled tables → global table.
- Step 4: GPCA of the global table → compromise factor scores.
- Component significance assessed by column-wise permutation testing.

## Key variants

- STATIS / DISTATIS — related multi-table methods using cross-product matrices.
- Generalized PCA (GPCA) — the single-table building block.
- Procrustes / consensus PCA — alternative multi-block consensus approaches.

## Known limitations

- Linear method; will not capture non-linear structure.
- Interpretation of compromise dimensions requires careful back-projection to original variables.
- Sensitive to how tables are defined (grouping choice changes the solution).

## Open problems

- Principled, automatic selection of the number of retained compromise dimensions.
- Robust multi-table integration in the presence of missing blocks.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] uses MFA to integrate ~600 H3K27ac ChIP-seq datasets structured into 59 tables (58 CKIs + DMSO), where the compromise dimensions recover H3K27ac temporal kinetics and a per-CRE perturbation likelihood is derived from CKI-vs-DMSO distances in significant MFA components.
