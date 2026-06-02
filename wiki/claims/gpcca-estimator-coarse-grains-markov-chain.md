---
title: "GPCCA coarse-grains the cell–cell Markov chain into macrostates, terminal states and fate probabilities"
slug: gpcca-estimator-coarse-grains-markov-chain
status: supported
confidence: 0.85
tags:
  - trajectory-inference
  - gpcca
  - markov-chain
  - cellrank
domain: "methods / Markov-chain coarse-graining"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: strong
    detail: "GPCCA estimator coarse-grains the transition matrix via Schur decomposition to define macrostates; terminal states and per-cell fate probabilities follow."
conditions: "Requires a (possibly non-reversible) cell–cell transition matrix from any kernel."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank's default estimator, **GPCCA** (Generalized Perron Cluster Cluster Analysis), coarse-grains the cell–cell transition matrix via a Schur decomposition into a small set of **macrostates**; terminal states are then automatically inferred or manually set, and per-cell **fate probabilities** are computed as absorption probabilities toward terminal states.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.3–4, Fig.1b): "our generalized Perron cluster cluster analysis (GPCCA) estimator coarse grains the transition matrix to define macro states … thereby defining terminal states and fate probabilities."

## Conditions and scope

Uses [[gpcca-generalized-perron-cluster-cluster-analysis]] over a [[markov-chain-trajectory-model]]; macrostate count guided by the Schur/eigengap.

## Counter-evidence

Macrostate decomposition is non-deterministic across runs and the number of macrostates can be ambiguous (see Limitations).

## Linked ideas

(none yet)

## Open questions

- Automatic, stable selection of the number of macrostates.
