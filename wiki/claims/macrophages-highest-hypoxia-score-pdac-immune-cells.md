---
title: "Macrophages exhibit the highest hypoxic microenvironment scores among PDAC immune cells (scRNA-seq, GSE155698)"
slug: macrophages-highest-hypoxia-score-pdac-immune-cells
status: supported
confidence: 0.75
tags: [hypoxia,macrophage,PDAC,scRNA-seq,GSE155698,tumor-microenvironment]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.5, Results): 'macrophages exhibited the highest hypoxic microenvironment scores, significantly higher than those of other immune cell types (Fig 2E and 2F)' — scores computed with AddModuleScore and AUCell on GSE155698 (37,018 PDAC + 7,316 normal pancreas cells across 13 annotated cell types)."
conditions: "Hypoxia score = ssGSEA / AddModuleScore / AUCell over the MSigDB 200-gene Hallmark Hypoxia set. Single PDAC cohort (GSE155698, n=16 PDAC + 3 normal); no formal multi-cohort replication of the cross-cell-type ranking."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

Across 13 cell types annotated in PDAC scRNA-seq (GSE155698), macrophages have the highest per-cell hypoxia signature score among immune cells, both by AddModuleScore (Seurat) and AUCell. This motivates the paper's subsequent focus on a hypoxia-responsive macrophage subcluster ("cluster 1").

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 2E–F). The signal is consistent across two independent scoring methods (AddModuleScore and AUCell), which mitigates method-specific artefacts.

## Conditions and scope

- Single PDAC cohort (Steele GSE155698, 16 primary PDAC + 3 normal pancreas).
- Scoring uses the 200-gene MSigDB Hallmark Hypoxia set, not an in-house signature.
- Cross-cell-type ranking; no functional readout that macrophages *respond* to hypoxia more than other immune cells (only that their transcriptional signature is more hypoxia-like).

## Counter-evidence

None within the paper's scope. Distinct from the canonical TAM-hypoxia accumulation model in [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]], which discusses TAM recruitment to hypoxic niches but does not rank hypoxia signature scores across PDAC immune cell types at single-cell resolution.

## Linked ideas

## Open questions

- Does this ranking generalise to other PDAC scRNA-seq cohorts (PanCanAtlas, Peng 2019)?
- Is the macrophage hypoxia signal dominated by infiltration of hypoxic niches or by intrinsic TAM transcriptional state?
