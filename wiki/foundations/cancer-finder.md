---
title: "Cancer-Finder"
slug: "cancer-finder"
domain: "single-cell genomics / malignant cell identification"
status: mainstream
aliases:
  - Cancer-Finder
first_introduced: "Single-cell malignant-cell classifier (pre-trained deep model)"
date_updated: 2026-06-03
source_url: ""
---

## Definition

Cancer-Finder is a pre-trained machine-learning tool that classifies individual cells as malignant or non-malignant from single-cell transcriptomes, used to seed candidate malignant-cell pools prior to CNV-based confirmation.

## Intuition

Malignant cells share transferable transcriptional hallmarks distinguishing them from normal epithelium; a pre-trained classifier flags candidates quickly, which are then cross-checked with copy-number inference.

## Formal notation

Per-cell binary malignancy prediction from a pre-trained model; candidates retained only if they also show discernible CNV patterns (e.g. via inferCNV) relative to patient-matched normal references.

## Key variants

- Used in tandem with inferCNV/infercnvpy for confirmation.

## Known limitations

- Pre-trained model may misclassify rare or low-purity malignant states.
- Requires CNV cross-validation to control false positives.

## Open problems

- Generalization to cancer types under-represented in training data.

## Relevance to active research

Used in pan-cancer TME atlas construction to refine malignant-cell identification (paired with infercnvpy), ensuring TME-cell analyses are not contaminated by tumor cells.
