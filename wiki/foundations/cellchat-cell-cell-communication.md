---
title: "CellChat — ligand-receptor cell-cell communication"
slug: cellchat-cell-cell-communication
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "CellChat"
  - "ligand-receptor inference"
  - "cell-cell communication scRNA-seq"
  - "L-R interaction analysis"
  - "intercellular signaling inference"
  - "cell-cell crosstalk inference"
first_introduced: "Jin et al. 2021 *Nature Communications*"
date_updated: 2026-05-05
source_url: "https://github.com/jinworks/CellChat"
---

## Definition

CellChat is a computational framework for inferring intercellular communication networks from single-cell RNA-seq data. It uses a curated database of ligand-receptor (L-R) pairs (CellChatDB) plus a probability model that combines L and R expression with cofactors and signaling network structure (mass-action-style) to score interaction probability between pairs of cell populations.

## Intuition

Given an scRNA-seq dataset with cell-type annotations, CellChat tells you "cell type A signals to cell type B via L-R pair X with probability P". It outputs interaction networks (heatmaps, chord plots), pathway-level aggregations, and significance tests via permutation.

## Formal notation

- Input: annotated scRNA-seq expression matrix (cell × gene + cell-type label)
- Database: CellChatDB (~2000 human/mouse L-R pairs, multimeric receptors, cofactors)
- Output: interaction probability + p-value (permutation) + signaling pathway aggregation

## Key variants

- CellPhoneDB — earlier and widely-used alternative with similar logic
- NicheNet — adds downstream regulatory potential
- LIANA — meta-tool that consolidates multiple L-R inference methods

## Known limitations

- Inference is from RNA expression, not protein abundance or actual interaction.
- High false-positive rate when cell types are spatially separated in vivo.
- Ligand "secretion" vs "membrane-bound" is treated similarly without spatial context.

## Open problems

- Spatially-aware extensions (using Visium / Xenium data) are still emerging.
- Validation rate of inferred L-R pairs against in vivo perturbation is unknown.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses CellChat on BLCA scRNA-seq to identify mMAC1 → T-cell ligand-receptor pairs: CXCL9:CXCR3, CXCL10:CXCR2 (chemotaxis), ICAM1:SPN (trafficking), HLA-A/B/C/E/F:CD8 (TCR activation), MIF:CD74+CD44/CXCR4 (costimulation). These predicted interactions form the mechanistic basis for the proposed mMAC1 → T-cell-recruitment-and-activation explanation of the survival benefit.
