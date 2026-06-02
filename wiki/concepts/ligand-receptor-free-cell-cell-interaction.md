---
title: "Ligand–receptor-free cell–cell interaction inference"
aliases:
  - LR-pair-free CCI inference
  - ligand–receptor-independent CCI inference
tags:
  - cell-cell-interaction
  - spatial-transcriptomics
  - self-supervised
  - methods
maturity: emerging
key_papers:
  - identifying-spatial-single-cell-level-interactions
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts:
  - cci-influence-tensor
---

## Definition

Inference of cell–cell interactions (CCIs) from spatial transcriptomics that does **not** require a predefined catalogue of ligand–receptor (L–R) pairs. Instead of scoring known L–R pairs against expression, the interaction signal is learned directly from how a cell's state depends on its spatial neighbourhood.

## Intuition

Imaging-based spatial transcriptomics (CosMx, MERFISH, Xenium) profiles only a small, pre-selected gene panel, so any conventional L–R-based CCI method captures only the subset of L–R pairs present on the panel. By learning interactions de novo — predicting a central cell's state from the organization, types, states, and ligand expression of neighbouring cells — methods such as [[foundations/gitiii-graph-transformer-cci-method]] sidestep the panel-coverage bottleneck and can surface interactions that no curated L–R database would have flagged.

## Variants

- **L–R-database-scoring methods** (the contrast class): [[foundations/cellchat-cell-cell-communication]], [[foundations/cellphonedb-ligand-receptor]], [[foundations/nichenet-ligand-target-inference]] — require curated L–R priors.
- **Self-supervised / learned-interaction methods**: GITIII predicts central-cell state from neighbours without L–R priors.

## Comparison

L–R-database methods are interpretable in terms of known biology but blind to interactions absent from their catalogue or gene panel; L–R-free methods are panel-agnostic and can find novel axes, but their predictions are correlational and lack a built-in molecular mechanism. The two are complementary: a future direction is to re-inject structured L–R prior knowledge (e.g. CellChatDB) into otherwise de-novo inference to recover biophysical realism.

## When to use

When the spatial gene panel is small relative to the L–R repertoire, when the goal is hypothesis-generating discovery of unexpected interaction axes, or when single-cell-resolution (not cell-type-averaged) interaction estimates are needed.

## Known limitations

De-novo inference identifies correlations between cell state and niche, not causal signalling. It does not, by itself, name the molecular mediator of an inferred interaction.

## Open problems

- Combining L–R-free discovery with curated prior knowledge for biological realism.
- Distinguishing direct signalling from biomechanical/metabolic confounders.

## Key papers

- [[papers/identifying-spatial-single-cell-level-interactions]] — News & Views introducing GITIII as an L–R-pair-free CCI method.

## My understanding

This is the conceptual hook of the GITIII commentary: the limited-gene-panel problem of imaging spatial transcriptomics makes L–R-catalogue methods structurally incomplete, and a learned, neighbourhood-prediction objective is a clean way around it. The trade-off — correlational, mechanism-free output — is the same one that [[concepts/niche-composition-predicts-cell-type-identity]] and niche-covariation approaches face.
</content>
