---
title: "TREM2 macs are spatially proximal to CXCL13+ PD-1hi CD4 and TCF1+/LAG3+ PD-1hi CD8 T cells in HCC immune aggregates"
slug: trem2-macs-proximal-pd1hi-cd8-tcf1-cxcl13-aggregates
status: supported
confidence: 0.85
tags:
  - MERFISH
  - TREM2
  - PD1hi
  - TCF1
  - CXCL13
  - LAG3
  - immune-aggregate
  - HCC
domain: "spatial transcriptomics / tumor immunology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: strong
    detail: "MERFISH spatial analysis within immune aggregates (B-cell-marker defined). TREM2 macs proximal to CXCL13+ PD-1hi CD4 T cells, TCF1+ PD-1hi CD8 T cells, and LAG3+ PD-1hi CD8 T cells (Fig. 2d middle, Fig. S3c). Consistent in stromal regions too (Fig. 2d right)."
conditions: "Immune aggregates defined by B-cell gene expression (e.g., MS4A1); MERFISH custom panel."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Within HCC immune aggregates, TREM2 macs are spatially proximal to three PD-1hi T-cell subsets: CXCL13+ PD-1hi CD4 helper T cells, TCF1+ PD-1hi CD8 T cells, and LAG3+ PD-1hi CD8 T cells. In stromal regions, TREM2 macs continue to associate with TCF1+ and LAG3+ PD-1hi CD8 T cells.

## Evidence summary

- MERFISH spatial neighbours analysis.
- Immune aggregates defined by B-cell gene signature.
- Consistent association in stromal regions.

## Conditions and scope

- Pairwise proximity; not causal contact.
- Aggregate definition depends on segmentation and B-cell signature thresholding.

## Counter-evidence

- FOLR2 macs in aggregates instead associate with PD-1hi effector CD8 (not TCF1+) — supports specificity of TREM2/TCF1 niche.

## Linked ideas

- [[concepts/trem2-mac-pd1-immune-niche-quartet]]
- [[concepts/cxcl13-cxcr5-tls-recruitment]]

## Open questions

- Are these contacts the *cause* of the TCF1+ progenitor reactivation niche, or merely co-located?
