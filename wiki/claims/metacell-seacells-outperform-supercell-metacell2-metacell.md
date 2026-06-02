---
title: "MetaCell and SEACells produce more trustworthy partitions than SuperCell and MetaCell2"
slug: metacell-seacells-outperform-supercell-metacell2-metacell
status: supported
confidence: 0.75
tags: [single-cell, metacell, benchmarking, mcRigor]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "At true γ=50 on semi-synthetic data, dubious-metacell proportions were 0.4% (MetaCell), 10.1% (SEACells), 28.4% (SuperCell), 7.8% (MetaQ); dubious rates 0.003, 0.161, 0.453, 0.092. Maximal Score: MetaCell 0.692 > SEACells 0.642 > SuperCell 0.537 > MetaCell2 0.528."
conditions: "Semi-synthetic and several real datasets; MetaCell/SEACells incur longer runtimes."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Among existing metacell partitioning methods, MetaCell and SEACells consistently yield fewer dubious metacells and higher mcRigor Scores than SuperCell and MetaCell2, at the cost of longer runtimes.

## Evidence summary

On semi-synthetic data at the true granularity γ = 50, MetaCell/SEACells/SuperCell/MetaQ produced 0.4%/10.1%/28.4%/7.8% dubious metacells (dubious rates 0.003/0.161/0.453/0.092). Maximal Scores were MetaCell 0.692, SEACells 0.642, SuperCell 0.537, MetaCell2 0.528. Consistent rankings were observed across real datasets.

## Conditions and scope

Benchmarking is via mcRigor's own Score; MetaCell tends to assign fewer single cells to metacells (trade-off). MetaQ was added during revision.

## Counter-evidence

SuperCell/MetaCell2 produce mostly dubious metacells even at low γ, so mcRigor's optimal γ for them (γ = 4) is far from the truth — a method-specific limitation rather than counter-evidence to the ranking.

## Linked ideas

(none yet)

## Open questions

How the ranking generalizes to data modalities and tissues beyond those tested.
