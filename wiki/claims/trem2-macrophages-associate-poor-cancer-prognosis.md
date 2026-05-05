---
title: "TREM2⁺ tumor-associated macrophages associate with poor cancer prognosis"
slug: trem2-macrophages-associate-poor-cancer-prognosis
status: supported
confidence: 0.7
tags:
  - cancer
  - prognosis
  - macrophage
  - TREM2
  - tumor-microenvironment
domain: "oncology / immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "TCGA pan-cancer: TREM2 MAC signature → worse OS in 7/12 cancer types, the highest-association poor-prognosis MAC signature in the panel. Consistent with prior literature (43)."
conditions: "TCGA bulk-deconvolution-based scoring with MoMac-VERSE-derived signature."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

The TREM2⁺ MAC signature (defined from MoMac-VERSE) is associated with significantly worse overall survival across multiple TCGA cancer types (7 of 12 cancers), making it the most strongly poor-prognosis macrophage subset in the panel.

## Evidence summary

- TCGA pan-cancer survival analysis: TREM2 MAC signature → worse OS in 7/12 cancers (Fig. S5D).
- Cited prior literature (43) characterizing TREM2⁺ MACs as immunosuppressive in TME.
- Consistent with the concept that TREM2⁺ MACs are lipid-handling, tissue-resident-like, and dampening of T-cell responses.

## Conditions and scope

- TCGA bulk RNA-seq, MoMac-VERSE-derived TREM2 signature, CIBERSORTx deconvolution.
- Correlational; some cancers show no association.

## Counter-evidence

- Some recent reports describe context-dependent or beneficial roles for TREM2⁺ MACs in lipid clearance and tissue repair (e.g., in atherosclerosis).
- Bulk deconvolution may conflate TREM2⁺ MACs with related lipid-associated populations.

## Linked ideas

(none yet)

## Open questions

- Direct functional validation across cancer types.
- Therapeutic targeting via anti-TREM2 antibodies (clinical trials ongoing).
- Cancer-specific contributions of TREM2⁺ MACs vs general TAM background.
