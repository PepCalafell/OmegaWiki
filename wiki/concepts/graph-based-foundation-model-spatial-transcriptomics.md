---
title: "Graph-based foundation model for spatial transcriptomics"
slug: graph-based-foundation-model-spatial-transcriptomics
domain: "methods / spatial-transcriptomics / foundation-models"
maturity: emerging
tags: []
aliases:
  - graph foundation model spatial transcriptomics
  - foundation model for spatial omics
  - pretrained spatial transcriptomics model
  - panel-invariant spatial foundation model
  - zero-shot spatial transcriptomics
  - large-scale pretrained spatial GNN
  - cross-tissue spatial transcriptomics model
  - cross-technology spatial foundation model
  - reusable spatial transcriptomics representation
  - spatial transcriptomics pretrain-then-finetune
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

A pretrained graph neural network trained on a large multi-tissue, multi-technology spatial transcriptomics corpus that produces transferable cell-neighborhood embeddings usable across new tissues, gene panels, and imaging platforms — without retraining (zero-shot) or with light fine-tuning. Analogous in spirit to vision/language foundation models (e.g., CLIP, BERT) and to scRNA-seq foundation models (e.g., scFoundation, scGPT) but built for spatially resolved data.

## Why it matters

Conventional spatial-clustering methods (STAGATE, GraphST, SpaceFlow, SEDR, NicheCompass) require either a single shared gene panel across slides or per-slide training; both are limiting as panel sizes and platforms multiply. A graph foundation model trained on diverse tissues, technologies, and panels generalises across the field without retraining, lowers compute cost for users, and supports cross-cohort comparisons.

## Key open questions

- How does scaling laws apply to spatial transcriptomics foundation models — cells, slides, gene panels, or tissues as the relevant axis?
- How to handle very small (≤50 gene) panels at inference time without panel-invariant embeddings collapsing?
- Mixture-of-experts to unify spot (Visium) and single-cell (Xenium/MERSCOPE/CosMx) resolutions.

## Status today

[[papers/novae-graph-based-foundation-model-spatial]] is the first large-scale instance (~30M cells, 18 tissues, 78 slides, three imaging-based platforms); zero-shot inference across new tissues and panels is demonstrated, but coverage of NGS-based platforms (Visium) and spatial proteomics multimodal training are open.
