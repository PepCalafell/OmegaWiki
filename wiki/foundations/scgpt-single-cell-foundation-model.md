---
title: "scGPT — single-cell multi-omics foundation model"
slug: scgpt-single-cell-foundation-model
domain: methods / single-cell
status: mainstream
aliases:
  - scGPT
first_introduced: "Cui et al. 2024 Nat. Methods (scGPT)"
date_updated: 2026-05-28
source_url: "https://www.nature.com/articles/s41592-024-02201-0"
---

## Definition

scGPT is a transformer-based foundation model for single-cell multi-omics, pretrained on tens of millions of cells using a generative masked-modeling objective over gene/expression tokens. It produces cell and gene embeddings transferable to downstream tasks including cell-type annotation, batch integration, gene-network inference, and perturbation response prediction.

## Intuition

Treat a cell as a "sentence" of gene tokens and pretrain a GPT-like model to fill in masked genes; the learned representation then transfers to many single-cell tasks with light fine-tuning.

## Formal notation

Masked generative pretraining over tokenized (gene, expression-bin) inputs with attention; fine-tuned heads for downstream tasks.

## Key variants

- Whole-human vs organ/tissue-specific pretrained checkpoints.

## Known limitations

- Restricts inputs to gene tokens/HVGs; reported to degrade when forced to genome-wide inputs without rectification; perturbation generalization to unseen contexts is limited.

## Open problems

- Genuine zero-shot perturbation generalization; genome-wide representation without noise blow-up.

## Relevance to active research

A primary foundation-model baseline that AlphaCell benchmarks against on both compositional and zero-shot perturbation tasks, used to argue that masked-token transformers on truncated genes underperform a continuous genome-wide flow model.
