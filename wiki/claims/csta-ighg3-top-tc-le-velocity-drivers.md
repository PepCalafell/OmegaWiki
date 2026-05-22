---
title: "CSTA and IGHG3 are top differentially spliced driver genes for TC and LE states respectively"
slug: csta-ighg3-top-tc-le-velocity-drivers
status: supported
confidence: 0.7
tags: [scVelo, driver-genes, CSTA, IGHG3, mechanistic]
domain: oncology/RNA-velocity
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "Among genes with dynamic splicing behaviour, CSTA scores highest in TC (consistent with its tumor-suppressor / MET-regulator role) and IGHG3 in LE (consistent with epithelial-cancer Ig involvement in proliferation, invasion and EMT). Other drivers include proto-oncogenes and tumor suppressors (Supplementary Data 6)."
conditions: "scVelo top-likelihood gene calls; phase portrait inspection"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The TC and LE states are driven (in the RNA-velocity sense) by characteristic genes — CSTA for TC and IGHG3 for LE — whose known biology aligns with the observed state assignment.

## Evidence summary
Fig. 6c–d, Supplementary Fig. 6a, Supplementary Data 6.

## Conditions and scope
scVelo dynamical model on spatially deconvolved cancer cells.

## Counter-evidence
"Driver" assignment is purely model-based; functional validation is absent.

## Linked ideas

## Open questions
Whether CSTA induction can re-route LE cells back toward TC experimentally.
