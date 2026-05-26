---
title: "Novae is orders of magnitude faster than competitors on million-cell datasets by avoiding external Harmony / Leiden / mclust"
slug: novae-runtime-orders-magnitude-faster-large-datasets
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - benchmark
  - runtime
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Fig. 3h (top): training+prediction time on 25k to 6.4M cells. Competing methods take up to several days at 6M cells (driven by Harmony + Leiden/mclust); Novae completes batch correction + domain assignment in seconds. Zero-shot Novae is fastest overall."
conditions: "All methods trained on a single A100 GPU with early stopping after ten epochs of no improvement."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

On datasets up to 6.4M cells, Novae's full pipeline (training, inference, batch correction, domain assignment) is orders of magnitude faster than STAGATE/GraphST/SpaceFlow/SEDR/NicheCompass/Scanpy combined with Harmony + Leiden/mclust — the latter bottleneck being the main source of runtime difference.

## Evidence summary

Fig. 3h top (overall runtime) and bottom (isolated batch-correction + clustering step) show ~day-scale runtimes for competitors vs second-scale for Novae at 6M cells.

## Conditions and scope

A100 GPU; standardized early stopping. Comparison includes both Harmony-based and Harmony-less downstream variants.

## Counter-evidence

None reported.

## Linked ideas

— none yet.

## Open questions

- Performance vs newer GPU-accelerated Harmony implementations.
