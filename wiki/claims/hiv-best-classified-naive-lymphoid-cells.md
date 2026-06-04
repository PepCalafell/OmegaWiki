---
title: "HIV is best classified by naive lymphoid cells, consistent with CD4 T-cell tropism"
slug: hiv-best-classified-naive-lymphoid-cells
status: weakly_supported
confidence: 0.7
tags:
  - HIV
  - classification
  - lymphoid
  - tropism
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "Per-cell-type patient classifiers showed HIV was best classified by naive lymphoid cells (naive CD4/CD8 T cells and B cells, F1 0.83), in line with the virus's tropism for CD4 T cells."
conditions: "Scenario 1; per-cell-type F1 across diseases."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Training one classifier per cell type revealed disease-specific cell-type informativeness: HIV was best classified by naive lymphoid cells (naive CD4/CD8 T cells and B cells, F1 0.83), consistent with HIV's known tropism for CD4 T cells — biologically interpretable cell-type contributions to diagnosis.

## Evidence summary

Per-cell-type/disease F1 analysis (Fig. 4d; Extended Data Fig. 8c; p.639).

## Conditions and scope

Scenario 1 cross-validation; correlative interpretation.

## Counter-evidence

Cell-type informativeness can reflect dataset composition, not only biology.

## Linked ideas

- [[concepts/patient-classification-reference-embedding-projection]]
- Foundations: [[foundations/hiv-virus]]

## Open questions

- Do cell-type informativeness patterns transfer across cohorts?
