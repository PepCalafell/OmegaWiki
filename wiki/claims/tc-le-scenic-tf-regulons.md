---
title: "SCENIC identifies distinct TC and LE TF regulons (EGR3/DLX5/MXI1/GRHL3/PITX1 in TC; TP63/HOXB2/CREB3L1/TCF4/NFATC4 in LE)"
slug: tc-le-scenic-tf-regulons
status: supported
confidence: 0.75
tags: [SCENIC, transcription-factor, regulon, OSCC, mechanistic]
domain: oncology/regulatory-genomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "SCENIC reports TC-upregulated TFs EGR3, DLX5 (proto-oncogenic), MXI1, GRHL3, PITX1 (tumor suppressors); LE-upregulated TFs TP63, HOXB2 (differentiation), CREB3L1, TCF4, NFATC4 (EMT regulators). IPA upstream regulator analysis corroborates with EHF, BCL3 for TC and SORL1, EGFR for LE."
conditions: "SCENIC default thresholds; per-sample regulon scoring"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The OSCC TC and LE are governed by partially non-overlapping sets of transcription-factor regulons whose biological functions (tumor suppression / differentiation in TC, EMT regulation in LE) align with the broader DEG patterns.

## Evidence summary
SCENIC regulon scoring (Supplementary Fig. 2p, Supplementary Data 3); IPA upstream-regulator analysis (Supplementary Fig. 2q).

## Conditions and scope
HPV-negative OSCC ST, malignant spots only.

## Counter-evidence
SCENIC regulon assignments are model-based and not validated by orthogonal ChIP / CUT&RUN within this paper.

## Linked ideas

## Open questions
Which of these TFs are mechanistic drivers vs passenger correlates of the spatial state.
