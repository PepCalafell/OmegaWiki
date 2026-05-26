---
title: "SpaceFlow — spatiotemporal patterns from spatial transcriptomics"
slug: spaceflow-spatial
domain: "methods / spatial-transcriptomics / graph-neural-networks"
status: mainstream
aliases:
  - SpaceFlow
  - Ren SpaceFlow
  - spatiotemporal spatial transcriptomics
  - SpaceFlow GNN
  - SpaceFlow Cang Nie
  - pseudo-spatiotemporal map SpaceFlow
first_introduced: "Ren, Walker, Cang & Nie 2022 Nature Communications"
date_updated: 2026-05-26
source_url: "https://github.com/hongleir/SpaceFlow"
---

## Definition

SpaceFlow learns embeddings that capture both spatial and gene-expression structure of spatial transcriptomics data via deep graph networks with a pseudo-spatiotemporal map for trajectory analysis, enabling identification of multicellular spatiotemporal organization.

## Strengths

- Provides both clustering and trajectory inference.
- Built-in spatial regularization terms.

## Known limitations

- Single-panel assumption; cross-technology applicability limited.
- Needs external clustering and batch correction.

## Relevance to active research

Benchmark comparator in [[papers/novae-graph-based-foundation-model-spatial]] across breast, colon, synthetic, and mouse-brain datasets.
