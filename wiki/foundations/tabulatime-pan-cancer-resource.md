---
title: "TabulaTIME — pan-cancer single-cell TME reference (4.5M cells, 36 cancer types)"
slug: tabulatime-pan-cancer-resource
domain: "computational genomics / oncology resources"
status: mainstream
aliases:
  - TabulaTIME
  - Tabula of the tumor immune microenvironment
  - TabulaTIME framework
  - TabulaTIME pretrained model
  - pan-cancer TabulaTIME reference
  - Han 2025 TabulaTIME
  - Wang TabulaTIME atlas
  - TabulaTIME pan-cancer scRNA-seq resource
first_introduced: "2025"
date_updated: 2026-05-26
source_url: "https://doi.org/10.1038/s43018-025-01039-5"
---

## Definition

TabulaTIME is a pan-cancer single-cell reference integrating 4,483,367 tumor cells from 103 published scRNA-seq studies, 36 cancer types, and 746 donors. It defines 6 major TME lineages × 56 cell subtypes and ships with a pretrained transfer-learning model for automated cell-type annotation of independent scRNA-seq datasets.

## Key variants

- All-lineage integration (140,072 MetaCells, CCA-corrected).
- Lineage-specific integrations: cytotoxic lymphocytes, conventional/regulatory T cells, B lymphocytes, myeloid, fibroblasts, endothelial.
- Pretrained transfer-learning model for query-dataset annotation (accuracy ~0.72-0.76 on BRCA/NSCLC).

## Known limitations

- Cross-study technical heterogeneity (10x vs other platforms) cannot be fully removed.
- Transfer-learning accuracy is below 0.8; not a replacement for manual curation in rare lineages.
- TCGA-derived ecotype subtyping is bulk-decomposition; single-cell validation incomplete.

## Relevance to active research

Useful as a query backbone for any new pan-cancer scRNA-seq ingest; provides canonical cell-subtype labels (Macro_SLPI, eFibro_CTHRC1, capEndo_RGCC, etc.) that the wiki can adopt as standard.
