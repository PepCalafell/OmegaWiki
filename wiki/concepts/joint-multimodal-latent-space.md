---
title: "Joint multimodal latent space for unpaired single-cell integration"
aliases:
  - joint latent space
  - unpaired multimodal integration
  - joint embedding multi-omics
  - GLUE joint latent space
  - unpaired cell integration
  - cross-modality latent representation
  - VAE-based multi-omics integration
  - shared latent embedding
  - manifold alignment single-cell
  - latent-space label transfer
  - mosaic single-cell integration
tags:
  - multi-omics
  - integration
  - representation-learning
  - single-cell
  - methods
maturity: active
key_papers:
  - mapping-early-human-blood-cell-differentiation
first_introduced: "Cao & Gao 2022 (GLUE); generalized notion of unpaired multimodal latent embedding"
date_updated: 2026-05-26
related_concepts:
  - single-cell-proteomics-mass-spec
  - mrna-protein-discordance
---

## Definition

A latent representation that places single-cell observations from two (or more) different modalities — measured on *different* physical cells — into a shared low-dimensional space such that cells with similar underlying biology are nearby regardless of modality. Enables label transfer, trajectory inference across modalities, and downstream tasks (cellRank, scProtVelo) on the joint embedding.

## Intuition

If two modalities both reflect the same underlying cell-state manifold (e.g., scRNA-seq and scp-MS of bone marrow HSPCs), a model can learn a single latent space where mRNA cells and protein cells are interchangeable for the purpose of trajectory analysis — even without per-cell pairing. The price is that the per-cell mRNA-protein correlation must be inferred rather than measured.

## Formal notation

Given two datasets {x_i^A} and {x_j^B} with no pairing, learn encoders f_A and f_B such that the latent posteriors q_A(z|x^A) and q_B(z|x^B) match the same prior, and a graph-guided constraint links biologically related features across modalities. GLUE achieves this with a VAE + a feature-space graph linking genes to proteins / regulatory regions.

In [[papers/mapping-early-human-blood-cell-differentiation]], GLUE integrated scp-MS (2500 cells) with CITE-seq (9086 cells) into a joint space with silhouette = 0.03, and cellRank on this joint space improved lineage assignment from 86%→91% (RNA) and 65%→95% (protein) for CLP/pre-pDC/MDP/pre-mDC.

## Variants

- **GLUE** (Cao & Gao 2022): graph-linked VAEs for unpaired multi-omics.
- **MOJITOO / scGLUE / Cobolt / MultiVI**: alternative unpaired-integration models with similar goals.
- **totalVI** (Gayoso et al. 2021): paired integration of mRNA + ADT in CITE-seq.

## Comparison

- vs paired integration (totalVI): paired methods directly measure mRNA-protein pairs per cell; unpaired methods (GLUE) infer the correspondence via latent space matching. Paired is statistically tighter; unpaired allows combining datasets that could not otherwise be analyzed together.
- vs anchor-based label transfer (Seurat reference mapping): label transfer is one-directional and lossy; joint latent space is symmetric and reusable for downstream methods (trajectory, velocity).

## When to use

- When combining datasets from incompatible modalities (scp-MS + scRNA-seq).
- When per-cell pairing is technically impossible (scp-MS destroys the cell; cannot also do scRNA-seq on the same cell).
- When downstream methods (cellRank, scProtVelo) need a single embedding.

## Known limitations

- Per-cell mRNA-protein relationships are inferred, not observed; per-gene discordance estimates inherit this uncertainty.
- Quality of integration depends on the feature graph (gene↔protein mapping); poor graphs degrade alignment.
- Silhouette scores at this scale (0.03 in the paper) are low in absolute terms — joint spaces are "good enough" rather than tight.

## Open problems

- Paired single-cell mRNA + untargeted protein measurements to ground-truth unpaired integrations.
- Better metrics for joint-space quality beyond silhouette.
- Handling more than two modalities (mRNA + protein + chromatin + spatial) jointly.

## Key papers

- [[papers/mapping-early-human-blood-cell-differentiation]] — uses GLUE for scp-MS + CITE-seq integration.

## My understanding

The unpaired-integration trick is the only path forward given current single-cell proteomics technology — scp-MS is destructive and incompatible with simultaneous scRNA-seq. The Furtwängler paper uses GLUE pragmatically and shows the downstream tasks (cellRank, scProtVelo) benefit, but the silhouette of 0.03 should keep us honest about how aligned the modalities really are.
