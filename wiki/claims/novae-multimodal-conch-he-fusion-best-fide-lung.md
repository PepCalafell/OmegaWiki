---
title: "Novae + CONCH multimodal fusion (transcriptomics + H&E) achieves the highest FIDE on the human-lung Xenium 5k slide and resolves additional bronchus / parenchyma domains"
slug: novae-multimodal-conch-he-fusion-best-fide-lung
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - multimodal
  - histopathology
  - lung-cancer
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Fig. 5d-e: on a Xenium 5k human-lung slide with pre-aligned H&E (10x Genomics), Novae+CONCH multimodal fusion achieves higher FIDE than CONCH alone or Novae alone. Multimodal separates D2032 (bronchus) and D2027 vs the merged D2037 from Novae alone."
conditions: "Single tissue (human lung Xenium 5k); pre-aligned H&E required. CONCH used as patch embedder, fused via MLP."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Fusing Novae's transcriptomics neighborhood embedding with CONCH H&E patch embeddings via a multilayer perceptron achieves the highest FIDE on a human-lung Xenium 5k slide, outperforming CONCH alone and Novae alone, and resolves bronchus / parenchyma domain pairs that Novae alone collapses.

## Evidence summary

Fig. 5d-e + Supplementary Fig. 16.

## Conditions and scope

One human-lung Xenium 5k slide with pre-aligned H&E; CONCH as pathology foundation model.

## Counter-evidence

Single slide / single tissue; no multi-patient benchmark.

## Linked ideas

— none yet.

## Open questions

- Performance with alternative pathology foundation models (UNI, Virchow).
- Late fusion vs joint pretraining on paired data.
