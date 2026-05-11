---
title: "mMAC1 chemoattracts T cells via CXCL9:CXCR3 and CXCL10:CXCR2 and supports T-cell activation via HLA class I and MIF:CD74"
slug: mmac1-chemoattracts-cells-cxcl9-cxcl10
status: supported
confidence: 0.75
tags:
  - mMAC1
  - CXCL9
  - CXCL10
  - CXCR3
  - CXCR2
  - T-cell
  - CellChat
  - ligand-receptor
  - bladder-carcinoma
domain: "immunology / oncology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "CellChat ligand-receptor analysis on BLCA scRNA-seq cells annotated with mMAC1 signature (Calafell 2024 Fig. 5H). Significant pairs mMAC1 → T cell: CXCL9:CXCR3, CXCL10:CXCR2 (chemoattraction), ICAM1:SPN (trafficking), HLA-A/B/C/E/F:CD8 (TCR/antigen presentation), MIF:CD74+CD44/CXCR4 (costimulation). mMAC1 % correlates with T cell % in BLCA bulk data (r = 0.74, P = 2.2×10⁻⁶⁷)."
conditions: "BLCA scRNA-seq + CellChat inference; CIBERSORTx for cell-proportion correlation."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

In bladder urothelial carcinoma, mMAC1-like cells engage T cells through a defined ligand-receptor program: CXCL9:CXCR3 and CXCL10:CXCR2 for chemoattraction, ICAM1:SPN for trafficking, HLA class I:CD8 for TCR/antigen presentation, and MIF:CD74 (with CD44/CXCR4) for costimulation. The mMAC1 percentage in BLCA tumors correlates strongly with T-cell percentage (r = 0.74, P = 2.2×10⁻⁶⁷).

## Evidence summary

- CellChat ligand-receptor inference on annotated BLCA scRNA-seq (Calafell 2024 Fig. 5H).
- CIBERSORTx-derived cell percentage correlation (Fig. 5F-G).

## Conditions and scope

- CellChat predictions are computational; ligand-receptor expression on the same cell does not prove functional interaction.
- BLCA-specific; OC and other tumors not separately tested for ligand-receptor pairs.

## Counter-evidence

- CXCL10 canonically binds CXCR3 (not CXCR2); the CXCL10:CXCR2 pair in the figure may reflect non-canonical binding or noise. CXCL9:CXCR3 is the canonical pair.

## Linked ideas

- Mechanistic anchor for the BLCA immune-hot phenotype and OS benefit.
- Suggests mMAC1 induction could enhance ICI response via T-cell recruitment.

## Open questions

- Functional validation (blocking antibody / receptor KO) of CXCL9-CXCR3 axis in mMAC1 ↔ T-cell coculture.
- Whether MIF:CD74 is a uniquely costimulatory axis or a general inflammatory marker.
- Whether mMAC1-T cell colocalization in situ corroborates the CellChat prediction.
