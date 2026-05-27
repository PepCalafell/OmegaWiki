---
title: "CZI CELLxGENE — harmonized human/mouse single-cell atlas"
slug: czi-cellxgene-atlas
domain: "single-cell genomics / atlases"
status: mainstream
aliases:
  - CELLxGENE
  - CZI CELLxGENE
  - CellxGene
  - CZ CELLxGENE Discover
first_introduced: "2021"
date_updated: 2026-05-27
source_url: "https://cellxgene.cziscience.com/"
---

## Definition

**CZI CELLxGENE** is the Chan Zuckerberg Initiative's single-cell data discovery platform: a continuously growing collection of published single-cell and single-nucleus RNA-seq datasets with harmonized cell-type ontologies (CL terms), donor metadata, and disease annotations. As of the April 2024 snapshot, it indexes hundreds of studies and tens of millions of cells across human organs.

## Intuition

CELLxGENE is the de facto "one query, all cells" atlas for human and mouse single-cell transcriptomics. Harmonization across CL ontology terms enables cross-organ and cross-study comparisons that the original studies do not support. Used as a substrate for atlas-scale downstream inference such as the [[sccellfie-metabolic-task-inference]] metabolic atlas in [[atlas-scale-metabolic-activities-inferred-single]].

## Formal notation

Each dataset is an AnnData object with standardized obs columns (`cell_type_ontology_term_id`, `tissue_ontology_term_id`, `disease_ontology_term_id`, `assay_ontology_term_id`, etc.) accessible via the `cellxgene-census` API.

## Key variants

- **April 2024 snapshot** — anchor used by scCellFie atlas (~30M cells, 668 datasets).
- **Census API** — programmatic, lazy-loadable, queryable backend.
- **CZ CELLxGENE Explorer** — interactive Web viewer per dataset.

## Known limitations

Heterogeneity in sequencing technologies (10x Chromium, smartseq, snRNA-seq), variable annotation depth, and batch effects across labs make raw concatenation risky — most downstream uses rely on per-dataset normalization plus integration ([[scanpy]], Harmony, scVI). Mis-annotated cell types persist and require thresholds (e.g. ≥50 cells per organ).

## Open problems

Continuous re-integration as new datasets are added; standardizing perturbation/condition metadata; coupling to spatial-transcriptomics atlases.

## Relevance to active research

Foundational for cell-type-resolved atlases of expression, regulation, and now metabolism ([[atlas-scale-metabolic-activities-inferred-single]]). Reference for query-to-reference mapping (Azimuth) and for cross-organ landscape papers.
