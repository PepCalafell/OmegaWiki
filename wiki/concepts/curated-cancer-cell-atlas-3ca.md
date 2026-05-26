---
title: "Curated Cancer Cell Atlas (3CA)"
aliases:
  - 3CA
  - Curated Cancer Cell Atlas
  - Weizmann 3CA
  - Tirosh 3CA atlas
  - pan-cancer scRNA-seq compendium
  - cancer single-cell atlas
  - 124-dataset cancer scRNA-seq atlas
  - tumour scRNA-seq compendium
  - 3CA resource
  - Curated cancer cell atlas v2
tags: [scrna-seq, pan-cancer, atlas, resource, oncology, tirosh]
maturity: active
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2023 (v1, Gavish et al.); 2025 (v2)"
date_updated: 2026-05-26
related_concepts: [recurrent-malignant-metaprograms-nmf, atlas-level-data-integration, tumor-hypoxia-intratumoral-heterogeneity]
---

## Definition

The Curated Cancer Cell Atlas (3CA) is a community resource that aggregates and standardises published cancer scRNA-seq and snRNA-seq datasets into a single uniform compendium emphasising malignant cells. Version 2 (Tyler et al. 2025) contains **124 datasets, 2,836 samples, 5,658,705 cells across >40 cancer types**.

## Intuition

Most individual scRNA-seq cancer studies profile only 5–20 tumours, leaving them statistically underpowered to detect robust pan-cancer or cancer-type-specific patterns. 3CA pools these studies *without* integration so that each dataset's biological variability is preserved while standardised cell-type annotations and formats make combined analyses tractable.

## Key features

- Format standardised to UMI counts or log2(TPM/10+1).
- Cell-type annotations validated by inferred CNAs and canonical markers; redefined de novo in 12 studies; imported from TISCH2 in 9 studies.
- No batch correction or integration — design choice motivated by the concern that integration removes biological signal in cancer.
- Website (https://www.weizmann.ac.il/sites/3CA/) exposes per-dataset UMAPs, MP-composition pies, gene-query tool, MP gene-set overlap tool, and marker-gene explorer.

## When to use

- As a reference compendium when asking pan-cancer questions about expression, cell-cycle, or marker genes.
- As a source of cancer-type-resolved scores for [[concepts/recurrent-malignant-metaprograms-nmf|malignant MPs]] in downstream analyses.
- As an external comparator for integrated atlases (e.g. Sikkema HLCA, MoMac-VERSE).

## Known limitations

- Cell-to-cell expression cannot be directly compared across samples (no integration).
- Sparse clinical annotations.
- Cell-type annotations are partly inherited from heterogeneous source studies.
- snRNA-seq vs scRNA-seq compositional differences confound MP comparisons.

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — Tyler et al. 2025, Nature Cancer (v2 release).

## My understanding

3CA is now the natural pan-cancer scRNA-seq baseline for any thesis-level question that needs cancer-type-resolved expression patterns or cell-cycle phase bias estimates. The deliberate avoidance of integration is the defining design decision and the main thing to compare against integrated atlases like HLCA or HCA.
