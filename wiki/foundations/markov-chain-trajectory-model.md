---
title: "Markov chain (cell-state trajectory model)"
slug: markov-chain-trajectory-model
domain: "methods / probabilistic dynamics"
status: mainstream
aliases:
  - Markov chain
  - cell-cell transition matrix
  - absorbing Markov chain
  - random walk on cell graph
first_introduced: "Markov 1906 (Markov chains); applied to single-cell fate by La Manno et al. 2018 and CellRank (Lange et al. 2022)"
date_updated: 2026-06-02
source_url: "https://en.wikipedia.org/wiki/Markov_chain"
---

## Definition

A Markov chain models a dynamic process as a set of states connected by transition probabilities, where the next state depends only on the current state (memoryless property). In single-cell fate mapping, the states are sequenced cells and the transition probabilities quantify how likely one cell is the ancestor (or future) state of another, collected in a cell–cell transition matrix.

## Intuition

If differentiation proceeds in small incremental steps, a cell's near-future is well approximated by a probabilistic hop to a similar neighboring state. Iterating these hops (a random walk) simulates the long-term trajectory; absorbing states correspond to terminal cell fates.

## Formal notation

Transition matrix T (n×n), row-stochastic. Fate (absorption) probabilities into a terminal-state set are solutions of (I − Q)X = R, where Q is the sub-matrix over transient states and R the transitions into absorbing states. Stationary distribution π satisfies πT = π.

## Key variants

- Discrete-time vs continuous-time chains.
- Reversible vs non-reversible (directed) chains — single-cell dynamics are non-reversible.
- Absorbing chains (terminal states as absorbing).

## Known limitations

- Memorylessness misses long-term/delayed effects (e.g. accumulated proteins) and rare states.
- Models average behavior, not individual most-probable paths.

## Open problems

- Recovering most-probable paths and non-tree-like (convergent) dynamics.

## Relevance to active research

- The mathematical backbone of CellRank: kernels build T and an estimator analyzes the induced chain. See [[papers/cellrank-consistent-data-view-agnostic-fate]] and [[cellrank-fate-mapping]]; coarse-grained via [[gpcca-generalized-perron-cluster-cluster-analysis]].
