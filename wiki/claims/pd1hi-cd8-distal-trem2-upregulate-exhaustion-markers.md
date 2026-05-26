---
title: "PD-1hi CD8 T cells distal from TREM2 macs upregulate exhaustion markers (HAVCR2, TOX, TIGIT) vs contact counterparts"
slug: pd1hi-cd8-distal-trem2-upregulate-exhaustion-markers
status: supported
confidence: 0.8
tags:
  - TREM2
  - PD1hi-CD8
  - exhaustion
  - HAVCR2
  - TOX
  - TIGIT
  - spatial-conditional-DE
  - MERFISH
domain: "spatial transcriptomics / tumor immunology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: medium
    detail: "Proximity-conditional DE of PD-1hi CD8 T cells stratified by distance from TREM2 macs in MERFISH-imaged HCC. Distal cells upregulate HAVCR2, TOX, TIGIT (Fig. S3d)."
conditions: "MERFISH proximity-conditional DE."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

PD-1hi CD8 T cells distal from TREM2 macs upregulate canonical T-cell exhaustion markers (HAVCR2/TIM3, TOX, TIGIT) relative to PD-1hi CD8 T cells in direct spatial contact with TREM2 macs — paired with the converse activation phenotype in contact cells.

## Evidence summary

- Conditional DE in MERFISH-segmented tissue.
- Distal PD-1hi CD8 cells exhibit exhaustion signature.

## Conditions and scope

- Correlational; spatial snapshot.

## Counter-evidence

- Causation ambiguous — exhausted cells may simply fail to engage TREM2 macs.

## Linked ideas

- [[claims/pd1hi-cd8-contact-trem2-upregulate-activation-cytotoxicity]]

## Open questions

- Does temporal dynamics (e.g., scTCR + spatial) reveal the directionality?
