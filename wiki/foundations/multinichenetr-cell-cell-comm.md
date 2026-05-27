---
title: "MultiNicheNetR — multi-sample ligand-receptor cell-cell communication inference"
slug: multinichenetr-cell-cell-comm
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "MultiNicheNetR"
  - "MultiNicheNet"
first_introduced: "Browaeys et al. 2023 (preprint, biorxiv); extension of NicheNet (Browaeys, Saelens & Saeys 2020 Nat Methods)"
date_updated: 2026-05-27
source_url: "https://github.com/saeyslab/multinichenetr"
---

## Definition

MultiNicheNetR extends NicheNet to perform multi-sample differential cell-cell communication analysis on scRNA-seq atlases. It infers ligand-receptor activity per sample / group, performs differential-expression-aware prioritisation, and tests for condition-specific interaction enrichment.

## Intuition

If NicheNet asks "what ligand drives the downstream target genes in this cell type?", MultiNicheNetR adds the comparative axis: "which interactions are enriched in tumor vs adjacent-healthy, or in MiTE-treated vs control?".

## Key variants

- Multi-sample design with condition labels (e.g., tumor vs adjacent-healthy, or treatment arms)
- Single-sample fallback delegating to NicheNet inference

## Known limitations

- Sensitive to cell-type annotation granularity
- Ligand-receptor database completeness limits coverage
- Computational cost grows quickly with sample number

## Relevance to active research

Used in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]] on a 332,723-cell human cancer atlas to reveal predominant TAM-T cell interactions in the TME (CXCL9-CXCR3, CD80/CD86-CTLA-4, ICOSLG-ICOS, TGFBR1-TGFB1, etc.).
