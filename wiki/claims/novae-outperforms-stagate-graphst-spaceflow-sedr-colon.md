---
title: "Novae outperforms STAGATE / GraphST / SpaceFlow / SEDR / Scanpy on FIDE and JSD for multi-panel colon spatial transcriptomics"
slug: novae-outperforms-stagate-graphst-spaceflow-sedr-colon
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - benchmark
  - methodological
  - colon
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Colon benchmark: 5 slides across 3 panels with limited gene intersection. Other methods are trained per-slide and concatenated + batch-corrected; Novae is trained jointly. Fig. 3c-d: Novae (zero-shot and fine-tuned) achieves better FIDE and JSD across 7-, 10-, 15-domain settings."
conditions: "Comparators are trained per-slide and concatenated due to limited gene intersection; Novae's joint training is a structural advantage."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

On the colon multi-panel benchmark (5 slides, 3 panels with insufficient overlap for joint training of competitors), Novae produces better spatial-domain continuity and cross-slide homogeneity than per-slide-trained STAGATE/GraphST/SpaceFlow/SEDR/Scanpy with concatenation + batch correction.

## Evidence summary

Fig. 3c-d.

## Conditions and scope

Same panel-intersection caveat as the breast benchmark.

## Counter-evidence

Comparator handicap from panel intersection / per-slide training; not a clean apples-to-apples comparison.

## Linked ideas

— none yet.

## Open questions

- Comparison fairness if alternative methods could be retrofitted with panel-invariant front-ends.
