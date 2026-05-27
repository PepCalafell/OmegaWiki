---
title: "Niche composition as predictor of central-cell-type identity"
aliases:
  - "niche composition predictor"
  - "logistic regression niche classifier"
  - "niche prediction task"
tags:
  - spatial-transcriptomics
  - cell-cell-interaction
  - tissue-architecture
maturity: emerging
key_papers:
  - nico-identifies-extrinsic-drivers-cell-state
first_introduced: "Agrawal et al. Nat Commun 2024 (NiCo Interactions module)"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

A logistic-regression formulation in which the identity of a central cell type CC is predicted from the cell-type-composition vector of its local neighborhood (frequencies within radius R). Regression coefficients quantify which neighboring cell types are over- or under-represented in CC's niche relative to chance, and their magnitudes and signs construct a directed cell-type interaction graph reflecting tissue architecture without requiring pre-specified tissue domains.

## Intuition

If a cell type has a stereotyped niche (e.g. Paneth cells next to stem cells; central-vein endothelial cells next to central hepatocytes), a classifier can recover that cell type from a permutation-shuffled but neighborhood-preserved tissue. The classifier's coefficient pattern reveals which neighbor identities are most discriminative — i.e., the strongest niche partners — and the confusion matrix surfaces pairs of cell types sharing the same niche.

## When to use

- When tissue-domain detection is overkill but per-cell-type niche partner identification is needed.
- When cell types of interest have stereotyped local niches but variable global localization (e.g. immune cell types).
- As a sanity check before running covariation analysis.

## Known limitations

- Predictive capacity (per-class precision) depends on niche stereotypy; migratory cells (DCs, monocytes, neutrophils) show low predictability.
- Sensitive to the choice of neighborhood radius R.
- Confounded by tissue-domain effects when cell types co-occur within large homogeneous regions.

## Open problems

- Integration with cell-state covariation: should the niche-prediction model condition on cell state to detect *state-dependent* niche preferences?
- Statistical correction for tissue-domain confounding.

## Key papers

- [[papers/nico-identifies-extrinsic-drivers-cell-state]] — introduces the formulation as NiCo's Interactions module and benchmarks against MISTy, CellCharter, Stagate, SpaGCN, Banksy, SpatialPCA on Allen brain MERFISH and STARmap visual cortex.

## My understanding

A lightweight but information-dense readout: a per-cell-type prediction accuracy below ~0.1 is itself biologically meaningful — it labels the cell type as "niche-promiscuous", typically migratory.
