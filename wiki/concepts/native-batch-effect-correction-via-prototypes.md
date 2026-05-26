---
title: "Native batch-effect correction via shared prototypes / optimal transport"
slug: native-batch-effect-correction-via-prototypes
domain: "methods / spatial-transcriptomics / batch-correction"
maturity: emerging
tags: []
aliases:
  - native batch correction spatial transcriptomics
  - prototype-based batch correction
  - optimal-transport batch correction spatial
  - in-model batch correction
  - integrated batch-effect correction
  - SwAV-style spatial batch correction
  - relaxed equipartition batch correction
  - within-model multi-slide alignment
  - cross-slide spatial integration
  - prototype-anchored slide alignment
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

Batch-effect correction that is built into the embedding model itself via shared learnable prototypes and an optimal-transport-based swapped-assignment objective, rather than applied as a post hoc correction by a separate tool (Harmony, BBKNN, ComBat, scVI's batch covariate). The same prototype set is shared across slides; per-slide optimal-transport assignments tolerate prototype absence, which prevents over-correction without forcing prototype presence.

## Why it matters

External batch correction (Harmony + Leiden / mclust) is the time bottleneck for million-cell spatial datasets; it also operates blind to spatial structure. Embedding batch correction inside the encoder using shared anchors (prototypes) and an OT assignment yields integrated cross-slide embeddings, drops the runtime by orders of magnitude, and lets domain-specific prototypes remain slide-private when biology demands.

## Key open questions

- How robust is relaxed-equipartition OT under extreme batch composition imbalance?
- Can the prototype space be reused across modalities (spatial transcriptomics + spatial proteomics + H&E)?
- How to design test-time refresh of prototypes when adding new tissues or technologies without full retraining?

## Status today

Demonstrated in [[papers/novae-graph-based-foundation-model-spatial]] on Xenium/MERSCOPE/CosMx; integrates conceptually with the wider [[concepts/batch-removal-vs-bioconservation-tradeoff]] debate by offering a third path that is neither external soft clustering (Harmony) nor mutual-nearest-neighbor matching but in-model prototype-anchored alignment.
