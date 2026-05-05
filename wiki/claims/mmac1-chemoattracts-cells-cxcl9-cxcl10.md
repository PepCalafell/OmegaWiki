---
title: "mMAC1 attracts and activates T cells via CXCL9/CXCL10 chemokines and HLA-class-I/MIF interactions"
slug: mmac1-chemoattracts-cells-cxcl9-cxcl10
status: weakly_supported
confidence: 0.6
tags:
  - macrophage
  - T-cell
  - chemokine
  - tumor-microenvironment
  - cell-cell-communication
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "CellChat predicted L-R pairs in BLCA scRNA-seq: CXCL9:CXCR3, CXCL10:CXCR2, ICAM1:SPN, HLA-A/B/C/E/F:CD8, MIF:CD74+CD44/CXCR4. mMAC1 % strongly correlates with T-cell % (r=0.74, P=2.2×10⁻⁶⁷)."
conditions: "Inferred from gene expression via CellChat, not validated experimentally with antibody blockade or transwell migration."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

The hypoxic inflammatory MAC subset (mMAC1) preferentially expresses chemoattractant ligands (CXCL9, CXCL10) and antigen-presentation/costimulation molecules (HLA-class-I, MIF, ICAM1) that, by inferred ligand-receptor interactions, recruit and activate CD8⁺ T cells in immune-hot bladder tumors. This crosstalk plausibly explains the strong mMAC1 / T-cell co-correlation and the survival benefit observed in immune-infiltrated cancers.

## Evidence summary

- CellChat L-R analysis on BLCA scRNA-seq identifies significant interactions between mMAC1 and T cells:
  - CXCL9:CXCR3 (T-cell chemotaxis)
  - CXCL10:CXCR2 (T-cell chemotaxis; note canonical receptor is CXCR3)
  - ICAM1:SPN (T-cell trafficking via CD43)
  - HLA-A/B/C/E/F:CD8 (TCR activation)
  - MIF:CD74+CD44/CXCR4 (costimulation)
- BLCA bulk-deconvolution: mMAC1 % vs T-cell % r=0.74, P=2.2×10⁻⁶⁷.
- iMAC21 anticorrelates with T cells (r=−0.27, P=5×10⁻⁸).

## Conditions and scope

- BLCA scRNA-seq; OC not included in CellChat analysis.
- L-R inferences are predictions, not validated by transwell migration, antibody blockade, or in vivo perturbation.

## Counter-evidence

- CellChat predictions have known false-positive rates; high gene expression does not guarantee functional ligand secretion.
- The CXCL10:CXCR2 pair is non-canonical; CXCL10 typically signals via CXCR3.
- Correlation between mMAC1 and T cells could reflect shared upstream drivers (immune-hot tumor context) rather than direct chemoattraction.

## Linked ideas

(none yet)

## Open questions

- Direct validation: transwell migration assay with mMAC1-conditioned medium ± CXCL9/CXCL10 blockade.
- In vivo depletion of mMAC1 in syngeneic murine tumor models — does T-cell infiltration drop?
- Spatial transcriptomics to confirm physical proximity of mMAC1 and T cells in BLCA tumors.
