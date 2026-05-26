---
title: "Novae's relaxed-OT batch correction simultaneously avoids over-correction and under-correction in the missing-domain benchmark"
slug: novae-relaxed-ot-avoids-over-and-under-correction
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - batch-correction
  - robustness
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Mouse-brain missing-domain benchmark (split slide A vs complete slide B; Fig. 4a-b) and Xenium v1 vs Xenium Prime 5k benchmark (Fig. 4c-d): Novae achieves both high FIDE (continuity) and low post-crop JSD (no over-correction, no under-correction). GraphST, SpaceFlow, STAGATE, Scanpy show high JSD (under-correction)."
conditions: "Benchmark designed to expose over vs under correction by removing a region from one slide before training and then evaluating proportions on matched halves."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

In benchmarks designed to expose batch-effect over- or under-correction (artificially removed regions in one slide, paired with a complete reference slide), Novae's relaxed-OT prototypes simultaneously achieve high domain continuity (FIDE) and low post-crop JSD, beating GraphST/SpaceFlow/STAGATE/Scanpy (which under-correct).

## Evidence summary

Fig. 4a-b: mouse-brain split slide vs complete slide; Fig. 4c-d: Xenium v1 split vs Xenium Prime 5k.

## Conditions and scope

Two benchmark configurations; results extrapolate from imaging-based spatial transcriptomics under controlled domain-removal perturbations.

## Counter-evidence

No formal performance characterisation under realistic missing-tissue patterns (e.g., systematically biased dropout vs random crop).

## Linked ideas

— none yet.

## Open questions

- Whether the result extends to NGS-based platforms (Visium).
