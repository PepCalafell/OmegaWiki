---
title: "Zero-shot spatial-domain inference across panels, tissues, and platforms"
slug: zero-shot-spatial-domain-inference
domain: "methods / spatial-transcriptomics / transfer-learning"
maturity: emerging
tags: []
aliases:
  - zero-shot spatial transcriptomics
  - zero-shot niche inference
  - transfer learning spatial transcriptomics
  - zero-shot domain assignment
  - cross-tissue zero-shot inference
  - cross-panel zero-shot spatial
  - pretrained spatial domain inference
  - inference-only spatial transcriptomics
  - panel-agnostic zero-shot spatial domains
  - foundation-model inference spatial
key_papers:
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
date_updated: 2026-05-26
---

## Definition

Inference of spatial domains on a new slide using a pretrained foundation model without any retraining on the new data — the model is applied as-is regardless of the slide's tissue, gene panel, or imaging platform, provided the panel and technology fall within the model's training distribution (and ideally even when they do not).

## Why it matters

Conventional spatial-clustering methods require per-study training (or per-slide training when panels mismatch), which is computationally expensive and breaks reproducibility across cohorts. Zero-shot inference dramatically lowers the entry barrier for spatial-omics consumers and enables cross-cohort comparisons that are otherwise impossible.

## Key open questions

- Out-of-distribution performance on unseen tissues and proteomics modalities.
- Sample-efficient few-shot adaptation when zero-shot under-performs.

## Status today

Demonstrated by [[papers/novae-graph-based-foundation-model-spatial]] on the breast and colon multi-panel benchmarks, where zero-shot Novae matches or beats other methods trained on those slides; analogous to zero-shot transfer in vision/language foundation models.
