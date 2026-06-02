---
title: "GPCCA (Generalized Perron Cluster Cluster Analysis)"
slug: gpcca-generalized-perron-cluster-cluster-analysis
domain: "methods / Markov-chain coarse-graining"
status: mainstream
aliases:
  - GPCCA
  - G-PCCA
  - generalized PCCA
  - Schur-vector coarse-graining
first_introduced: "Reuter et al. 2018 *J. Chem. Theory Comput.* — Generalized Markov state modeling / GPCCA"
date_updated: 2026-06-02
source_url: "https://doi.org/10.1021/acs.jctc.8b00079"
---

## Definition

GPCCA coarse-grains a (possibly non-reversible) Markov chain into a small number of metastable/macro states by projecting onto a basis of real Schur vectors of the transition matrix and optimizing a fuzzy membership (crisp/soft) assignment. Unlike classical PCCA+, it handles non-reversible transition matrices, which is essential for directed single-cell dynamics.

## Intuition

A noisy cell–cell Markov chain has a few coherent "basins" the chain enters and leaves slowly. GPCCA finds these basins (macrostates) from the leading Schur vectors and produces a coarse transition matrix between them, exposing initial and terminal (near-absorbing) states.

## Formal notation

Given transition matrix T, compute a real Schur decomposition T = QRQᵀ, retain the m leading Schur vectors, and solve for a membership matrix χ (n×m) maximizing crispness subject to χ being a stochastic, near-invariant projection. Macrostate transition matrix is the coarse-grained projection of T.

## Key variants

- Reversible PCCA+ (special case).
- Soft vs crisp macrostate assignment.

## Known limitations

- Choice of macrostate count m (eigengap/Schur-gap heuristics).
- Non-deterministic optimization can vary across runs.

## Open problems

- Automatic, stable selection of the number of macrostates.

## Relevance to active research

- The estimator at the core of CellRank: it turns the cell–cell transition matrix into macrostates, terminal states and fate probabilities. See [[papers/cellrank-consistent-data-view-agnostic-fate]] and [[cellrank-fate-mapping]].
