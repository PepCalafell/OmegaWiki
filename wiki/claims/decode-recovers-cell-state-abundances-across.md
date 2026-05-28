---
title: "DECODE recovers cell-state abundances across pseudotime, cell-cycle and drug-response"
slug: decode-recovers-cell-state-abundances-across
status: supported
confidence: 0.75
tags: [cell-state, deconvolution, multiomics]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Best CCC on monocyte pseudotime (10 states), cell-cycle (G1/S/G2, 3 states) and drug-treatment (4 states) datasets across three omics (Fig. 4d)."
conditions: "Three curated datasets; MeDuSA comparison only on the continuous-pseudotime dataset."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE recovers cell-state abundances — pseudotime trajectories, cell-cycle phases and drug-response time points — and outperforms baselines across all three state datasets and omics.

## Evidence summary

Best CCC on the monocyte pseudotime dataset (10 states, from MeDuSA), the cell-cycle dataset (G1/S/G2) and the drug-treatment dataset (4 time points) (Fig. 4d). MeDuSA was only comparable on the continuous-pseudotime dataset since it requires continuous labels.

## Conditions and scope

Instance of [[cell-state-deconvolution]]; CIBERSORTx failed on the discrete-state datasets 2 and 3.

## Counter-evidence

None reported.

## Linked ideas

## Open questions

Generalization to other state continua and joint type+state deconvolution.
