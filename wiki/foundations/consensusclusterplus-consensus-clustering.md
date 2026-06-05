---
title: "ConsensusClusterPlus — consensus clustering for subtype discovery"
slug: "consensusclusterplus-consensus-clustering"
domain: "methods / unsupervised clustering"
status: mainstream
aliases:
  - ConsensusClusterPlus
  - consensus clustering
first_introduced: "2010"
date_updated: 2026-06-05
source_url: ""
---

## Definition

ConsensusClusterPlus is an R package that performs resampling-based consensus clustering to determine the number of stable clusters (k) and assign samples to subtypes, widely used for molecular subtype discovery in bulk omics cohorts.

## Intuition

By repeatedly subsampling and re-clustering, it asks how consistently sample pairs land in the same cluster; subtypes that survive resampling are deemed stable rather than artefacts of a single clustering run.

## Formal notation

data matrix → repeated subsample + cluster → consensus matrix → stability metrics (CDF, delta area) → chosen k and assignments.

## Key variants

- Pairs with various base clustering algorithms (k-means, hierarchical, PAM) and distance metrics.

## Known limitations

- Choice of k remains partly subjective; stability does not guarantee biological meaning.

## Open problems

- Reconciling consensus-cluster subtypes across cohorts and platforms.

## Relevance to active research

Used to derive five stable immune-based bladder cancer subtypes (Classes A–E) in the IMvigor210 cohort, with Class E enriched for Macro-CXCL9.
