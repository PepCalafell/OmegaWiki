---
title: "Subgraph-based local microenvironment encoding for spatial GNNs"
slug: subgraph-local-microenvironment-encoding
domain: "methods / spatial-transcriptomics / graph-neural-networks"
maturity: emerging
tags: []
aliases:
  - subgraph spatial GNN
  - local neighborhood encoding spatial transcriptomics
  - mini-batch subgraph training spatial
  - lazy graph loading spatial transcriptomics
  - local subgraph attention
  - bounded receptive field spatial GNN
  - subgraph mini-batch spatial omics
  - on-the-fly subgraph generation
  - GraphSAGE-style spatial transcriptomics
  - subgraph sampling spatial GNN
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
  - "[[papers/identifying-spatial-single-cell-level-interactions]]"
date_updated: 2026-06-02
---

## Definition

A training and inference pattern for spatial graph neural networks in which the model operates on locally sampled subgraphs of the cell-proximity graph rather than the full slide. Subgraphs are generated on the fly per mini-batch, keeping VRAM bounded (per-batch size, not dataset size) and bounding the receptive field of the GNN to a true local microenvironment.

## Why it matters

Full-slide GNNs face two coupled problems: (1) GPU memory scales with cell count, limiting million-cell training; (2) deep GNNs over the full slide mix information across 100s of microns, polluting local-niche representations with distant tissue context. Subgraph training fixes both: bounded memory enables 30M-cell training on a single A100 (40 GB), and a 16-layer GNN restricted to a local subgraph stays microenvironment-faithful.

## Key open questions

- Optimal subgraph radius / hop count as a function of tissue density.
- Stitching cross-subgraph context for tissue-level analyses.

## Status today

Demonstrated in [[papers/novae-graph-based-foundation-model-spatial]]; adjacent to broader graph-sampling literature (GraphSAGE, ClusterGCN) but specifically motivated for spatial omics by VRAM / receptive-field constraints.
