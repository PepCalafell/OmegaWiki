---
title: "GITIII — self-supervised graph transformer for single-cell-level cell–cell interactions"
slug: gitiii-graph-transformer-cci-method
domain: "spatial transcriptomics / methods / cell–cell interaction"
status: mainstream
aliases:
  - GITIII
first_introduced: "2026"
date_updated: 2026-06-02
source_url: ""
---

## Definition

GITIII (introduced by Xiao, Zhang, Zhao & Wang, *Nature Machine Intelligence* **8**, 42–58, 2026) is a self-supervised graph-transformer method that infers spatially resolved cell–cell interactions (CCIs) at single-cell resolution from imaging-based spatial transcriptomics data, **without relying on prior knowledge of ligand–receptor pairs**. It is the method discussed by the *Nature Machine Intelligence* News & Views [[papers/identifying-spatial-single-cell-level-interactions]].

## Intuition

GITIII operates on the principle that the cellular microenvironment is a key determinant of a cell's state: it learns to predict the gene-expression state of a central ("receiver") cell from the spatial organization, ligand expression, cell types, and cell states of its neighbouring ("sender") cells. The discrepancy and learned weighting between neighbours expose how each neighbour influences the central cell — a CCI signal — without needing a predefined ligand–receptor catalogue.

## Key variants

GITIII first decomposes gene expression into a cell-type component and a cell-state deviation (capturing intrinsic heterogeneity). It then builds cell-neighbourhood subgraphs from the spatial data and processes them with two modules:

1. **Embedding module** producing three embeddings — a **node embedding** (integrates neighbour cell state and type while masking the cell-state expression of same-type neighbours to prevent perfect prediction), a **distance embedding** (models signalling decay with distance), and an **edge embedding** (captures the influence of neighbouring ligands and spatial proximity).
2. **Single-layer graph transformer encoder** that integrates the embeddings to predict the receiver cell's state. The single layer is deliberate: it keeps the output directly traceable to neighbourhood input features, preserving interpretability that is lost in deeper networks.

The final output is a **CCI influence tensor** ([[concepts/cci-influence-tensor]]) quantifying the impact of every neighbouring cell on the state of the central receiver.

## Known limitations

- Identified CCIs represent **correlations** between cell state and its niche, not causal mechanisms.
- Restricted gene panels of imaging-based spatial transcriptomics preclude downstream signalling-response analysis.
- De novo inference does not incorporate curated biophysical prior knowledge of signalling molecules (e.g. CellChatDB).
- Transcriptomics-only; does not integrate proteomics, metabolomics, or epigenomics.

## Open problems

- Integrating causal machine-learning methods for mechanistic, not correlative, CCI understanding.
- Incorporating structured prior knowledge (diffusion ranges of secreted vs surface ligands) to improve biological realism.
- Moving toward predictive, in-silico simulation of CCI perturbations for therapeutic-target discovery.

## Relevance to active research

Downstream applications enabled by GITIII's influence tensor include CCI-informed cell clustering, CCI-network construction, differential analysis of cell subgroups (DEGs and their interacting cell types), and comparison of CCI strength across biological conditions. It is a peer/alternative to ligand–receptor-based CCI tools such as [[foundations/cellchat-cell-cell-communication]], [[foundations/cellphonedb-ligand-receptor]], [[foundations/nichenet-ligand-target-inference]], and to graph-based spatial frameworks such as [[concepts/graph-based-foundation-model-spatial-transcriptomics]]. It applies to imaging platforms such as [[foundations/cosmx-spatial-transcriptomics]], [[foundations/merfish-imaging-spatial]], and [[foundations/xenium-in-situ-spatial-transcriptomics]].
</content>
</invoke>
