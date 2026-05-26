---
title: "Novae outperforms STAGATE / GraphST / SpaceFlow / SEDR / Scanpy on FIDE and JSD for multi-panel breast spatial transcriptomics"
slug: novae-outperforms-stagate-graphst-spaceflow-sedr-breast
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - benchmark
  - methodological
  - breast-cancer
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Breast dataset: 2 slides, 2 distinct panels (185 common genes). Novae (zero-shot and fine-tuned) beats per-method baselines on both FIDE (continuity) and JSD (cross-slide homogeneity) across 7-, 10-, and 15-domain settings (Fig. 3a-b)."
conditions: "Per-method baselines trained on intersection of 185 common genes, with Harmony+mclust downstream; Novae trained on both full panels simultaneously."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

On the breast multi-panel benchmark (2 slides, 2 panels, 185 common genes), Novae achieves better FIDE and JSD than STAGATE, GraphST, SpaceFlow, SEDR, and Scanpy in both zero-shot and fine-tuning modes across multiple domain counts.

## Evidence summary

Fig. 3a-b: schematic and FIDE/JSD bar plots for 7, 10, 15 domains.

## Conditions and scope

Comparison favored Novae by design — competitors lose information through panel intersection, while Novae trains on both panels jointly. Benchmark uses Harmony+mclust as the downstream for comparators.

## Counter-evidence

Authors acknowledge that competitors' constraint (panel intersection) limits the fairness of the comparison — the result is best read as evidence that Novae's panel-invariant design produces a real practical advantage, not as an apples-to-apples ranking.

## Linked ideas

— none yet.

## Open questions

- Whether the advantage persists when comparators are given access to full panels via concatenation rather than intersection.
