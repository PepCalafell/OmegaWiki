---
title: "Cross-prediction between single-cell perturbation signatures yields a functional similarity graph of regulators that recovers known protein interactions and reveals novel similarities"
slug: cross-prediction-perturbation-signatures-functional-similarity
status: supported
confidence: 0.8
tags: [crispr-screen, machine-learning, perturbation, functional-similarity, methodology, string]
domain: methods
source_papers:
  - integrated-time-series-analysis-high-content
evidence:
  - source: integrated-time-series-analysis-high-content
    type: supports
    strength: strong
    detail: "Leave-one-group-out cross-prediction of KO identity from single-cell profiles built a similarity graph; >80% (24/29) of edges were supported by STRING protein-protein interactions, while novel edges (e.g. Ep300-Smc1a-Myd88-Runx1, Yeats2-Dnttip2) lacked STRING/Mixscape support."
conditions: "RAW 264.7-Cas9 macrophages; 135-gene upscaled CROP-seq; cross-prediction across 25-58 nodes over time points."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement
A machine-learning cross-prediction approach — predicting each cell's knockout identity from its transcriptome after removing the true class from training — produces a functional similarity graph of regulators. Most edges (>80%) coincide with STRING protein-protein interactions, validating the approach, while a minority capture novel functional similarities invisible to interaction databases or to Mixscape clustering.

## Evidence summary
Functional similarity graphs at single and multiple time points; STRING corroboration ([[papers/integrated-time-series-analysis-high-content]], Figures 5D-E, 6B; defines [[concepts/perturbation-cross-prediction-functional-similarity-graph]]; uses [[foundations/mixscape-crispr-perturbation-analysis]]).

## Conditions and scope
Macrophage cell line; method presented as broadly applicable.

## Counter-evidence
None; novel edges remain to be experimentally validated.

## Linked ideas

## Open questions
Are the STRING-independent functional similarities (e.g. Ep300/Smc1a) reproducible in other systems?
