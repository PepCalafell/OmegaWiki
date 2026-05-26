---
title: "Novae natively corrects batch effects via shared prototypes and a relaxed optimal-transport assignment"
slug: novae-native-batch-correction-via-relaxed-ot-prototypes
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - batch-correction
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Adapts SwAV's optimal-transport assignment so each mini-batch corresponds to one biological batch, with relaxation that allows a subset of prototypes to remain unused per slide. Eliminates the need for external Harmony / Leiden / mclust steps and demonstrably reduces JSD across slides (Fig. 3i)."
conditions: "Works under imaging-based spatial transcriptomics; relies on relaxed equipartition that tolerates slide-specific absence of prototypes."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Novae integrates batch-effect correction inside the encoder via shared learnable prototypes and a relaxed (non-equipartitioned) Sinkhorn-Knopp optimal-transport swapped-assignment objective, replacing external batch-correction tools (Harmony) for spatial transcriptomics.

## Evidence summary

Methods sections "Prototypes and swapped assignment task" + "Batch-effect correction"; Fig. 3i shows superior batch alignment in UMAP space vs Harmony-post-corrected SpaceFlow/STAGATE/GraphST/SEDR/NicheCompass on the breast Xenium+MERSCOPE benchmark.

## Conditions and scope

Per-mini-batch correspondence to a single biological slide is required for the assignment formulation; relaxation parameter must allow prototype absence per slide.

## Counter-evidence

Performance under extreme batch composition imbalance not exhaustively characterised — discussed only qualitatively.

## Linked ideas

— none yet.

## Open questions

- Robustness of relaxed-OT under heavily skewed batch composition.
- Whether prototypes can be safely shared across modalities (transcriptomics + proteomics + H&E).
