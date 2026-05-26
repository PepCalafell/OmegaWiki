---
title: "Across human HSPC differentiation, the overall mRNA-protein correlation vector is below 0.25"
slug: mrna-protein-vector-correlation-below-025
status: supported
confidence: 0.9
tags: [mRNA-protein-discordance, correlation, quantitative, HSPC]
domain: single-cell proteomics / translation regulation
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.6): 'Comparison between the full correlation vectors on mRNA and protein level revealed an overall weak correlation below 0.25 between these vectors (Fig. 5B). Moreover, this difference in the correlation vectors also resulted in the enrichment of gene sets that were not enriched on mRNA level (Fig. 5C and table S1).'"
conditions: "Correlation vectors of mRNA / protein abundance against pseudotime / fate probability across HSPC trajectories."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Across the HSPC differentiation continuum, mRNA and protein correlation vectors agree at <0.25 — quantifying single-cell mRNA-protein discordance for the first time across a human in vivo differentiation system.

## Evidence summary

Cross-vector comparison reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. 5B).

## Conditions and scope

Healthy adult human BM CD34+ HSPCs; GLUE-integrated joint latent space.

## Counter-evidence

Replicated in an external bulk dataset of 59 breast cancer cell lines (rank correlation 0.35) — value differs but supports the general phenomenon.

## Linked ideas

## Open questions

- Which gene classes drive the discordance most strongly?
