---
title: "Human Cytokine Dictionary dataset"
slug: human-cytokine-dictionary-dataset
domain: "immunology"
status: mainstream
aliases:
  - "Human Cytokine Dictionary"
  - "huCytoDict"
  - "human cytokine dictionary PBMC dataset"
first_introduced: "Oesinghaus et al. 2025 (bioRxiv)"
date_updated: 2026-05-28
source_url: "https://doi.org/10.64898/2025.12.12.693897"
---

## Definition

A single-cell transcriptomic perturbation atlas of human peripheral blood: 9,697,974 PBMCs from 12 healthy donors, each stimulated in vitro for 24 h with one of 90 individual cytokines (or PBS), sequenced by Parse Biosciences split-pool barcoding. Cells are annotated into 16 major cell types (12 retained for response analysis after low-abundance filtering). The deliverable is donor-consensus differential-expression profiles (log2FC vs PBS) for each cytokine × cell-type combination, plus derived response-magnitude scores, tissue-specificity indices, and a curated cytokine-production/communication network.

## Intuition

It is the human counterpart to the mouse [[immune-dictionary-dataset]] (Cui et al. 2024): where the mouse Dictionary used in vivo lymph-node injection of 86 cytokines, the human Dictionary uses in vitro PBMC stimulation with 90 cytokines at far greater cell scale. It is the largest single-cell cytokine perturbation dataset in primary human immune cells to date and is intended as an open community reference for decoding cytokine activity in any human transcriptomic dataset.

## Key variants

- Raw screen: 90 cytokines × 12 donors × 16 cell types, ~9.7M cells
- Donor-consensus DE compendium: log2FC + padj per cytokine × cell type (gene sets consumed by huCIRA)
- CIP compendium: 82 cytokine-induced immune programs from DRVI decomposition
- Reference cytokine–cell interaction database integrating ImmunoGlobe + immuneXpresso

## Known limitations

- Single 24 h timepoint — misses early and late signaling dynamics
- In vitro PBMC (no tissue context, no stromal/structural niche)
- Supraphysiological cytokine doses (upper range of in vitro use)
- 12 donors — limited power to link response variability to genetics/demographics
- Resting PBMCs (no concurrent TCR/BCR engagement)

## Open problems

- Multi-timepoint and dose-response extensions
- Cross-tissue human perturbation atlasing
- Linking donor response variability to genotype / age / sex at scale
- Use as training data for virtual-cell / AI cytokine-perturbation models

## Relevance to active research

Directly comparable to the mouse [[immune-dictionary-dataset]] and the [[cytokine-perturbation-scrna-seq-vivo-lymph]] resources already in the vault. Provides a human PBMC reference panel against which tumor / disease cytokine activity can be inferred (relevant to HypoxiaVERSE TAM/NK cytokine inference). Consumed by [[hucira-cytokine-immune-response-analysis]].
