---
title: "GLUE — graph-linked unified embedding for unpaired multi-omics integration"
slug: glue-multiomics-integration
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - GLUE
  - scGLUE
  - graph-linked unified embedding
  - graph-linked VAE multi-omics
  - Cao Gao GLUE
  - GLUE variational autoencoder
  - regulatory-graph guided integration
  - unpaired single-cell integration
first_introduced: "Cao & Gao 2022 *Nat Biotechnol* — Multi-omics single-cell data integration and regulatory inference with graph-linked embedding"
date_updated: 2026-05-26
source_url: "https://github.com/gao-lab/GLUE"
---

## Definition

GLUE is a variational-autoencoder-based framework for unpaired multi-omics single-cell data integration. It uses a feature-space graph (e.g., gene↔chromatin region, gene↔protein) to constrain how encoders for different modalities map into a shared latent space. The result is a joint embedding where cells from different modalities are nearby when they share underlying biology, without requiring per-cell pairing.

## Intuition

Two single-cell modalities measuring different physical cells can still be aligned if you tell the model how features in one modality relate to features in the other (e.g., this gene encodes that protein). The graph propagates the alignment signal through the feature space.

## Formal notation

Each modality A, B has an encoder f_A, f_B producing latent posteriors q_A(z|x), q_B(z|x); a discriminator forces latent distributions to match. A feature graph G with nodes spanning both modalities adds a regularization term that aligns the feature-level representations.

In [[papers/mapping-early-human-blood-cell-differentiation]], GLUE integrated 2500-cell scp-MS data with 9086-cell CITE-seq data; joint-space silhouette was 0.03 and downstream cellRank trajectory inference benefited measurably.

## Key variants

- Original GLUE for scRNA-seq + scATAC-seq.
- Extended to scRNA-seq + scp-MS in Furtwängler 2025.
- MultiVI, scMoMaT, Cobolt — alternative unpaired-integration frameworks.

## Known limitations

- Quality depends on feature graph completeness.
- Silhouette scores in absolute terms are typically low; alignment is "good enough" rather than tight.
- Computationally heavier than anchor-based label transfer.

## Open problems

- Cross-modality integration for >2 modalities simultaneously.
- Benchmark metrics beyond silhouette and label-transfer accuracy.

## Relevance to active research

- [[papers/mapping-early-human-blood-cell-differentiation]] uses GLUE for the scp-MS + CITE-seq joint latent space.
