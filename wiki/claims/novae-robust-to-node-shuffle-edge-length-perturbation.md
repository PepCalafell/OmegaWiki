---
title: "Novae outputs are robust to input-graph perturbations (node shuffling, edge-length reduction); errors concentrate at domain interfaces and stromal/sparse regions"
slug: novae-robust-to-node-shuffle-edge-length-perturbation
status: supported
confidence: 0.75
tags:
  - spatial-transcriptomics
  - robustness
  - perturbation
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Fig. 4f: Novae's relative sensitivity to node shuffle and to edge-length reduction (set to 0.01) over breast and colon slides shows that perturbations primarily affect domain interfaces (node shuffle) and stromal/sparse regions (edge-length reduction)."
conditions: "Two tissues (breast, colon); perturbations applied at inference time on pretrained model."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Under input-graph perturbations — node shuffling and large edge-length reductions — Novae's spatial-domain output degrades primarily at domain interfaces (for node shuffle) and stromal / sparse regions (for edge-length drop), preserving core domain assignments elsewhere.

## Evidence summary

Fig. 4f.

## Conditions and scope

Two tissues, inference-time perturbations. Performance on more severe perturbations is reported in Supplementary Fig. 17/19.

## Counter-evidence

Supplementary Fig. 17 shows a sharp performance drop at ~60% cell-loss degradation.

## Linked ideas

— none yet.

## Open questions

- Robustness to systematic spatial offsets vs random noise.
