---
title: "Tamborero immune-cell signatures"
slug: tamborero-immune-signatures
domain: methods
status: mainstream
aliases:
  - Tamborero signatures
  - Tamborero immune signatures
  - Tamborero gene sets
  - immune cell subset signatures Tamborero
  - immune-subset marker sets Tamborero
first_introduced: "Tamborero et al. 2018 Clin Cancer Res"
date_updated: 2026-05-25
source_url: ""
---

## Definition
A curated set of immune cell-subset gene signatures (B cells, CD4/CD8 T subsets, NK CD56bright / CD56dim, Tregs, Tfh, Tcm/Tem, NKT, Tgd, macrophages, dendritic-cell subsets, eosinophils, mast cells, neutrophils, MDSCs) derived from transcriptional profiles of purified immune populations, intended for marker-based inference of immune infiltration in bulk tumours via ssGSEA.

## Intuition
Tamborero signatures provide a more granular immune-subset readout than ESTIMATE's single immune score, suitable for ssGSEA scoring of bulk RNA or protein expression where dedicated deconvolution methods underperform.

## Formal notation
- 28 immune subsets covered
- Gene set coverage on TPCPA proteome: 33%–81% per subset

## Key variants
- Original Tamborero gene sets
- ssGSEA scoring on protein expression (TPCPA application)

## Known limitations
- Derived from RNA expression of sorted populations — protein-level application is an extrapolation.
- Gene set sizes vary; coverage on proteome platforms is partial.

## Open problems
- Protein-trained immune-subset signatures for direct MS-based inference.

## Relevance to active research
Used pan-cancer to characterise immune-subset infiltration in bulk samples; in TPCPA it underpins the CRC immune consensus cluster (CC1/CC2) prognostic axis.
