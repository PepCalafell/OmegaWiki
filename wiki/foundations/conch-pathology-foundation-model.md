---
title: "CONCH — pathology vision-language foundation model"
slug: conch-pathology-foundation-model
domain: "methods / digital-pathology / foundation-models"
status: mainstream
aliases:
  - CONCH
  - CONtrastive learning from Captions for Histopathology
  - Lu CONCH
  - Mahmood CONCH
  - pathology foundation model
  - vision-language histopathology
  - CONCH patch embedding
  - H&E foundation model embeddings
  - histopathology contrastive learning
first_introduced: "Lu et al. 2024 Nature Medicine"
date_updated: 2026-05-26
source_url: "https://github.com/mahmoodlab/CONCH"
---

## Definition

CONCH is a vision-language foundation model for histopathology trained by contrastive learning on paired H&E image patches and natural-language captions. It produces transferable embeddings for downstream tasks including patch classification, retrieval, and (as used here) fusion with non-image modalities such as spatial transcriptomics.

## Strengths

- Strong zero-shot transfer across diverse histopathology tasks.
- Patch-level embeddings concatenable with other modalities.

## Known limitations

- Patch-level granularity may under-represent fine subcellular morphology.
- Cell-type heterogeneity captured implicitly only via image texture, not gene expression.

## Relevance to active research

Used in [[papers/novae-graph-based-foundation-model-spatial]] as the H&E embedding source for multimodal Novae+CONCH spatial-domain inference, which achieves the highest FIDE score on the human-lung Xenium 5k slide and resolves D2032 (bronchus) and D2027 that Novae alone collapses.
