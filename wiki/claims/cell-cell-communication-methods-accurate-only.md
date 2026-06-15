---
title: "Cell–cell communication methods are reliable only for their top-ranked interactions"
slug: cell-cell-communication-methods-accurate-only
status: supported
confidence: 0.75
tags:
  - cell-cell-communication
  - benchmarking
  - interpretation
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Odds-ratio metric over the top 5% of predicted pairs; methods do well there but become noisy over full rankings."
conditions: "Inference drawn from the CCC task's top-5% odds-ratio behaviour."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

CCC inference methods are better at prioritising a small fraction of relevant interactions but become noisy when their full interaction rankings are considered; analysts should focus on the highest-scoring predictions.

## Evidence summary

"methods are better at prioritizing a small fraction of relevant interactions while being prone to noise when their full interaction rankings are considered" — leading to the practical recommendation that "analysts interpreting CCC results may likewise want to focus only on the most high-scoring predictions" (p.1038). The odds-ratio metric is computed over the top 5% of predicted pairs.

## Conditions and scope

A usage guideline derived from benchmark behaviour, not a hard cutoff; the exact reliable fraction is task- and dataset-dependent.

## Counter-evidence

Restricting to top predictions risks discarding genuine weaker interactions; the "top 5%" threshold is a metric design choice, not a biological boundary.

## Linked ideas

Explains why [[claims/max-aggregation-ligand-receptor-scores-outperforms]]; practical guidance for users of [[foundations/liana-cell-cell-interaction-inference]].

## Open questions

What principled threshold separates reliable from noise-dominated CCC predictions per dataset.
