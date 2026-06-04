---
title: "CIMA-CLM — cell language model for chromatin accessibility"
aliases:
  - CIMA-CLM
tags: []
maturity: emerging
key_papers:
  - chinese-immune-multi-omics-atlas
first_introduced: "chinese-immune-multi-omics-atlas"
date_updated: 2026-06-04
related_concepts:
  - cell-type-specific-genetic-regulation-immune
---

## Definition

CIMA-CLM is a cell type–specific deep-learning model that predicts chromatin accessibility by fusing a DNA-sequence embedding (501-bp chromatin sequence) with a single-cell gene-expression embedding, and that scores noncoding-variant effects via in silico mutagenesis.

## Intuition

Whether a sequence is accessible depends both on its intrinsic motif content and on the cell's transcriptional state. By cross-attending a DNA encoder (HyenaDNA) with a transcriptome encoder (scGPT), the model learns context-dependent accessibility, capturing cell type–specific peaks rather than a single consensus.

## Formal notation

Two parallel pretrained encoders (DNA: HyenaDNA; cell: scGPT) feed transformer encoders and a cross-attention fusion decoder. Output is per-region accessibility; in silico mutagenesis compares predicted accessibility of altered vs reference sequence at single-nucleotide resolution.

## Variants

- Sequence + cell-state fusion (CIMA-CLM)
- Contrasted with sequence-free (scOpen) and sequence-only (scBasset, Epiformer, DeepSEA) models

## Comparison

Outperforms scOpen, scBasset, Epiformer, and DeepSEA on accessibility prediction; uniquely conditions on single-cell expression. Builds on the [[foundations/scgpt-single-cell-foundation-model]] and [[foundations/hyenadna-genomic-sequence-model]].

## When to use

To predict cell type–specific accessibility from sequence + expression, or to prioritize noncoding variant effects when experimental ATAC is unavailable.

## Known limitations

Accuracy declines with low per-cell-type capture depth; evaluated on 32 cell types with adequate signal.

## Open problems

Generalization to unseen cell states and ancestries; calibration of variant-effect magnitudes against functional assays.

## Key papers

- [[papers/chinese-immune-multi-omics-atlas]] — median PCC 0.7661–0.9612 (mean 0.8951), AUROC 0.9058–0.9927 (mean 0.9560) across 32 cell types.

## My understanding

A concrete instance of multimodal foundation-model fusion for regulatory genomics; the cell-state conditioning is the key novelty over sequence-only predictors.
