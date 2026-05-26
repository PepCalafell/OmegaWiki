---
title: "Novae's lazy subgraph loading bounds GPU VRAM to model + mini-batch size, independent of dataset size"
slug: novae-lazy-loading-gpu-vram-bounded-not-dataset-size
status: supported
confidence: 0.9
tags:
  - spatial-transcriptomics
  - infrastructure
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Subgraphs are generated on the fly per mini-batch (2-20 MB) on top of a 128 MB model on Hugging Face; AnnData remains on CPU. Enabled 30M-cell training on a single A100 (40 GB VRAM)."
conditions: "Imaging-based spatial transcriptomics with cell-level proximity graphs."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Novae uses on-the-fly subgraph sampling so GPU VRAM is bounded by the model (~128 MB) plus the size of a single mini-batch (~2-20 MB), independent of the underlying AnnData / slide size. This enabled training on ~30M cells with a single 40 GB A100.

## Evidence summary

Methods section "Implementation and training details" + Time/memory efficiency results section.

## Conditions and scope

Architectural design choice; bounded VRAM holds regardless of dataset size, but disk I/O remains a function of dataset size.

## Counter-evidence

None reported.

## Linked ideas

— none yet.

## Open questions

- Inference throughput vs preprocessed-graph baselines on small datasets.
