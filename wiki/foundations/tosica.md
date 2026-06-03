---
title: "TOSICA"
slug: "tosica"
domain: "single-cell genomics / reference-based annotation"
status: mainstream
aliases:
  - TOSICA
  - transformer cell-type annotation
first_introduced: "Chen et al., Nature Communications 2023"
date_updated: 2026-06-03
source_url: "https://github.com/JackieHanLab/TOSICA"
---

## Definition

TOSICA (Transformer for One-Stop Interpretable Cell-type Annotation) is a transformer-based model that annotates single cells against a reference atlas while outputting per-cell prediction probabilities and interpretable gene/pathway attention.

## Intuition

Self-attention over gene/pathway tokens lets the model transfer reference cell-type labels to new datasets and quantify prediction uncertainty, supporting batch-robust label transfer at atlas scale.

## Formal notation

Cells are embedded as pathway/gene token sequences; a transformer encoder produces a class distribution per cell, with the max-probability label assigned and the probability used as a confidence/uncertainty score.

## Key variants

- Pathway-token vs gene-token input representations.
- Reference-model fine-tuning for specific tissues.

## Known limitations

- Confidence reflects reference coverage; genuinely novel states are mislabeled with possibly high probability.
- Requires a well-annotated reference atlas.

## Open problems

- Detecting and flagging out-of-distribution cell states.

## Relevance to active research

Used to transfer a pan-cancer core-atlas annotation onto an independent validation set (39 datasets, 2.17M cells), achieving 0.94 mean prediction probability including for cancer types absent from the core.
