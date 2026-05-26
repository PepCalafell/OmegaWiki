---
title: "Multimodal H&E + spatial transcriptomics fusion for spatial domain inference"
slug: multimodal-he-spatial-transcriptomics-fusion
domain: "methods / spatial-omics / multimodal-integration"
maturity: emerging
tags: []
aliases:
  - H&E spatial transcriptomics fusion
  - multimodal Novae+CONCH
  - histology spatial transcriptomics integration
  - pathology foundation model + spatial transcriptomics
  - HE+ST fused embedding
  - morphology + transcriptomics fusion
  - patch embedding fusion spatial transcriptomics
  - multimodal spatial niche inference
  - HE-aware spatial domain detection
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

A multimodal approach in which spatial-transcriptomics neighborhood embeddings are fused (typically via a multilayer perceptron or concatenation + projection) with H&E patch embeddings produced by a pathology foundation model (e.g., CONCH, UNI, Virchow). The fused representation is then used for spatial-domain assignment, leveraging morphology and molecular signals jointly.

## Why it matters

Spatial transcriptomics gives molecular state but limited morphology beyond cell-centroid geometry; H&E gives morphology and tissue architecture but no expression. Fusing both resolves cases where domains are molecularly similar but morphologically distinct (e.g., bronchus vs adjacent parenchyma in lung) and where domains differ molecularly but lie in similar tissue zones. The fused score (FIDE) exceeds either modality alone in benchmarks.

## Key open questions

- Choice of pathology foundation model (CONCH vs UNI vs Virchow) and downstream FIDE impact.
- Patch size / cell-neighborhood alignment for fusion.
- Joint pretraining (rather than late fusion) on paired H&E + ST corpora.

## Status today

Demonstrated for Xenium 5k lung slide in [[papers/novae-graph-based-foundation-model-spatial]] with CONCH; remains gated by the scarcity of paired H&E + spatial transcriptomics + spatial proteomics datasets needed for true multimodal foundation-model pretraining.
