---
title: "CellChat nominates KLRB1-CLEC2B, SIGLEC1-SPN, LILRB1-HLA-F, HAVCR2-LGALS9 as candidate cell-extrinsic triggers of baseline JAK-STAT in spleen"
slug: cellchat-receptor-ligand-candidates-baseline-jak-stat-spleen
status: weakly_supported
confidence: 0.45
tags: [cellchat, receptor-ligand, klrb1, siglec1, lilrb1, havcr2, tim3, lgals9, spleen, tissue-context]
domain: immunology
source_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
evidence:
  - source: jak-stat-signaling-maintains-homeostasis-cells
    type: supports
    strength: weak
    detail: "Fig. 6e,f + Extended Data Fig. 9c,d: CellChat on Tabula Muris / Tabula Sapiens spleen single-cell atlases (with ProjecTILs T-cell subtyping) identifies receptor-ligand interactions highly weighted at splenic CD8 T cells and macrophages — KLRB1-CLEC2B (T cell - lectin-expressing immune cells), SIGLEC1-SPN (Mac - T cells), LILRB1-HLA-F (Mac - many cell types), HAVCR2/TIM3-LGALS9 (Mac - myeloid cells)."
conditions: "Computational inference on public spleen scRNA-seq atlases (mouse Tabula Muris, human Tabula Sapiens)."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Computational receptor-ligand inference (CellChat) on Tabula Muris / Tabula Sapiens spleen single-cell atlases nominates KLRB1-CLEC2B (T cells with lectin-expressing immune partners), SIGLEC1-SPN (macrophages with T cells), LILRB1-HLA-F (macrophages with HLA-F-expressing partners) and HAVCR2/TIM3-LGALS9 (macrophages with myeloid partners) as candidate receptor-ligand pairs that may mediate the tissue-context-derived signals triggering baseline JAK-STAT in splenic CD8+ T cells and macrophages.

## Counter-evidence

- CellChat predictions are computational hypotheses; no genetic or pharmacological perturbation of any single pair has been tested.
- The atlases used do not necessarily reflect spleen architecture at the spatial resolution required for cell-cell interaction inference.
