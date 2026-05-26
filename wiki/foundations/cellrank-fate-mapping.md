---
title: "cellRank — Markov-chain trajectory and fate-mapping for single-cell data"
slug: cellrank-fate-mapping
domain: "methods / trajectory-inference"
status: mainstream
aliases:
  - cellRank
  - cellRank2
  - CellRank fate mapping
  - cellRank pseudotime kernel
  - cellRank velocity kernel
  - Lange Theis cellRank
  - macrostates trajectory analysis
  - terminal state inference
  - fate probability single-cell
  - cellRank GPCCA
first_introduced: "Lange et al. 2022 *Nat Methods* — CellRank for directed single-cell fate mapping"
date_updated: 2026-05-26
source_url: "https://github.com/theislab/cellrank"
---

## Definition

cellRank is a single-cell trajectory analysis framework that builds a Markov transition matrix over a k-NN cell graph, integrating directional information (RNA velocity, pseudotime, similarity, real time). It uses generalized Perron cluster cluster analysis (GPCCA) to identify macrostates, initial / terminal states, and per-cell fate probabilities into each terminal state.

## Intuition

Trajectory inference reduces to a Markov chain: cells are states, transitions are weighted by similarity and directionality. Macrostates (sets of cells that the chain enters and leaves coherently) correspond to biological lineages; fate probabilities are absorption probabilities into terminal macrostates.

## Formal notation

Given a directed transition matrix T (n_cells × n_cells), GPCCA partitions the state space into K macrostates; terminal macrostates have absorbing-like behavior. Per-cell fate probabilities are the absorption probabilities into each terminal macrostate.

In [[papers/mapping-early-human-blood-cell-differentiation]], cellRank ran on the joint scp-MS + CITE-seq latent space with the pseudotime kernel; lineage assignment accuracy improved over single-modality fits.

## Key variants

- Velocity kernel (uses RNA velocity vectors).
- Pseudotime kernel (uses DPT / diffusion pseudotime).
- Similarity kernel.
- cellRank2 generalizes the framework to additional modalities.

## Known limitations

- Sensitive to choice of kernel and parameters.
- Macrostate decomposition is non-deterministic across runs.
- Performance degrades on poorly-clustered embeddings.

## Open problems

- Multi-trajectory inference where lineages cross or revert.
- Calibrated uncertainty on fate probabilities.

## Relevance to active research

- Core trajectory inference tool in [[papers/mapping-early-human-blood-cell-differentiation]] — runs on the GLUE joint latent space and outperforms single-modality fits for CLP/pre-pDC/MDP/pre-mDC.
