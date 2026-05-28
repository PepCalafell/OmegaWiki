---
title: "scPoli (single-cell population-level integration)"
slug: scpoli-prototype-reference-mapping
domain: methods
status: mainstream
aliases:
  - scPoli
  - prototype reference mapping
first_introduced: "De Donno et al., Nature Methods 2023"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1038/s41592-023-02035-2"
---

## Definition

scPoli is a semi-supervised deep-learning model for single-cell reference mapping and integration. It learns sample-level and cell-level embeddings jointly, builds class "prototypes" from a labeled reference dataset, and maps query (e.g. diseased) cells onto that reference, transferring cell-type labels while flagging cells with no close prototype as "uncertain".

## Intuition

Rather than forcing every query cell into an existing reference label, scPoli's prototype/uncertainty mechanism lets novel cell states surface as unlabeled clusters. This is what makes it suitable for discovering disease-specific populations that have no healthy counterpart.

## Formal notation

Conditional variational autoencoder with learned per-sample condition embeddings; prototypes are centroids of labeled reference cells in latent space; query cells beyond a distance threshold from all prototypes are labeled uncertain.

## Key variants

Part of the scArches ecosystem of architecture-surgery reference mapping methods.

## Known limitations

Uncertainty thresholds are heuristic; semi-supervised cross-tissue integration can underestimate tissue-specific differences. Discovery of novel states depends on the reference being a faithful baseline.

## Open problems

Calibrating uncertainty across very heterogeneous query datasets; distinguishing true novel states from batch artifacts.

## Relevance to active research

Used to map 190,756 diseased skin fibroblasts onto a healthy F1–F5 reference, where ~69,589 cells flagged as uncertain were re-clustered into the disease-adapted and disease-specific fibroblast subtypes.
