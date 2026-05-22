---
title: "Atlas-level data integration in single-cell genomics"
aliases:
  - atlas integration
  - atlas-scale integration
  - reference atlas integration
  - Human Cell Atlas integration
  - HCA integration
  - large-scale scRNA-seq integration
  - multi-donor integration
  - multi-laboratory integration
  - nested batch effects integration
  - million-cell integration
  - cross-protocol integration
  - cross-tissue integration
  - single-cell atlas construction
tags:
  - data-integration
  - atlas
  - scRNA-seq
  - HCA
  - benchmarking
maturity: stable
key_papers:
  - "[[papers/benchmarking-atlas-level-data-integration-single]]"
first_introduced: "Human Cell Atlas white paper (Regev et al. 2017); operationalised by Luecken et al. 2022 scIB benchmark"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/batch-removal-vs-bioconservation-tradeoff]]"
  - "[[concepts/scrna-atlas-as-reference-projection]]"
---

## Definition

Atlas-level data integration is the problem of merging single-cell omics datasets that span many donors, laboratories, conditions, tissues, protocols and species into a single self-consistent representation suitable for downstream analysis. It is distinguished from simple batch correction by (a) the diversity and depth of batch-effect sources (nested, confounded with biology), (b) the scale (hundreds of thousands to millions of cells), and (c) the requirement that the integrated representation support cell-type discovery, rare cell-state preservation, and continuous trajectory inference simultaneously.

## Intuition

A reference atlas like the Human Cell Atlas combines samples from many labs over many years, using different protocols and sample-handling pipelines. Each combination introduces a new batch-effect axis. Linear batch correction methods (ComBat) implicitly assume a single global batch geometry; they fail when batch and biology overlap nonlinearly. Atlas-level integration requires methods that can model nonlinear, hierarchical batch structure without erasing the rare cell-states an atlas exists to discover.

## Workflow

1. Per-batch preprocessing (QC, normalization, optional HVG selection, optional scaling).
2. Integration: produce a corrected gene matrix, joint embedding, or integrated kNN graph.
3. Evaluation: scIB metrics (batch removal + bio-conservation), 14 metrics aggregated 40/60.
4. Downstream: cell-type annotation, trajectory inference, reference projection of new query data via scArches / Azimuth.

## When to use

This concept frames any HCA-scale, multi-donor, multi-laboratory single-cell project. It is the primary use-case for scVI, scANVI, Scanorama, and the scIB pipeline.

## Known limitations

- Integration is fundamentally lossy when batch and biology are confounded.
- Hyperparameter choices for deep-learning integration methods are not standardized.
- The scIB benchmark covers RNA + ATAC; multimodal atlas integration (CITE-seq, RNA+ATAC, spatial) is not yet benchmarked.

## Open problems

- Reference-mapping (scArches) as an alternative to from-scratch integration.
- Joint multimodal atlas integration.
- Cross-species atlas construction without species batch erasure of biology.

## Relevance to active research

Atlas-level data integration is the foundational methodology underlying every multi-donor scRNA-seq study, including the MoMac-VERSE / TAM atlases relevant to thesis work — see [[papers/benchmarking-atlas-level-data-integration-single]] for the canonical method-selection benchmark.
