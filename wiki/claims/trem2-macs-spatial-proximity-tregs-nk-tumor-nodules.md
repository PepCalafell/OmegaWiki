---
title: "In HCC tumor nodules, TREM2 macs are spatially proximal to Tregs and NK cells by MERFISH"
slug: trem2-macs-spatial-proximity-tregs-nk-tumor-nodules
status: supported
confidence: 0.8
tags:
  - MERFISH
  - TREM2
  - Treg
  - NK-cell
  - spatial-transcriptomics
  - HCC
domain: "spatial transcriptomics / tumor immunology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: medium
    detail: "MERFISH (Vizgen MERSCOPE) on HCC tissue, with cell types defined by scRNA-seq-derived gene signatures. In tumor nodules, TREM2 macs spatially most proximal to Tregs and NK cells, as well as monocytes and FOLR2 macs (Fig. 2d left)."
conditions: "MERFISH custom panel; Cellpose segmentation with 20% mask shrinkage; tumor-nodule regions defined by tumor-cell + hepatocyte gene expression."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

MERFISH proximity analysis reveals that TREM2 macs within HCC tumor nodules are spatially closest to Tregs and NK cells (also adjacent to monocytes and FOLR2 macs).

## Evidence summary

- MERFISH on HCC tissue with custom Vizgen panel.
- Cell types annotated by scRNA-seq-derived signatures.
- Pairwise spatial proximity analysis within tumor-nodule regions.

## Conditions and scope

- Segmentation-dependent (Cellpose).
- Mask shrinkage may bias peripheral-marker detection.

## Counter-evidence

- None within this paper.

## Linked ideas

- [[foundations/merfish-imaging-spatial]]

## Open questions

- Functional consequence of TREM2-mac/Treg proximity in HCC?
