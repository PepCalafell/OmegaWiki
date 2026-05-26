---
title: "PD-1hi CD8 T cells in direct spatial contact with TREM2 macs upregulate activation/cytotoxicity markers (KLRK1, CD69, CD27, CXCR6, EOMES, GZMA/H/K) vs distal counterparts"
slug: pd1hi-cd8-contact-trem2-upregulate-activation-cytotoxicity
status: supported
confidence: 0.8
tags:
  - TREM2
  - PD1hi-CD8
  - cytotoxicity
  - EOMES
  - GZMK
  - KLRK1
  - spatial-conditional-DE
  - MERFISH
domain: "spatial transcriptomics / tumor immunology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: medium
    detail: "Proximity-conditional differential expression of PD-1hi CD8 T cells stratified by contact vs distance from TREM2 macs (MERFISH). Contact PD-1hi CD8 upregulate KLRK1, CD69, CD27, CXCR6, CXCR4, CD2, EOMES, CXCL16, GZMA, GZMK, GZMH (Fig. S3d)."
conditions: "MERFISH proximity-conditional DE; PD-1hi CD8 in contact vs distal from TREM2 mac."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

In MERFISH-imaged HCC tissue, PD-1hi CD8 T cells in direct spatial contact with TREM2 macs upregulate canonical activation and cytotoxicity markers (KLRK1, CD69, CD27, CXCR6, CXCR4, CD2, EOMES, CXCL16, GZMA, GZMK, GZMH) relative to PD-1hi CD8 T cells distal from TREM2 macs.

## Evidence summary

- Proximity-conditional DE on MERFISH-segmented cells.
- Stratification: PD-1hi CD8 contact-with-TREM2 vs distal.
- Effect size and significance reported in Fig. S3d.

## Conditions and scope

- Conditional DE on segmentation-derived contacts; subject to segmentation artefacts.
- Correlational, not causal.

## Counter-evidence

- Could reflect pre-existing T-cell state attracting TREM2 macs rather than TREM2-mac-mediated activation.

## Linked ideas

- [[claims/pd1hi-cd8-distal-trem2-upregulate-exhaustion-markers]]

## Open questions

- Identity of direct ligand-receptor pairs mediating the activation phenotype.
