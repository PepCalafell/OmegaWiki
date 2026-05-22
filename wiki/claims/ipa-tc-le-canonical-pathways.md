---
title: "IPA predicts LE-specific activation of GP6/EIF2/HOTAIR and TC-specific MSP-RON, IL-33, p38 MAPK canonical pathways"
slug: ipa-tc-le-canonical-pathways
status: supported
confidence: 0.7
tags: [IPA, canonical-pathways, OSCC, mechanistic]
domain: oncology/pathway-analysis
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "IPA across 10+ patients predicts LE-exclusive activation of GP6, EIF2 and HOTAIR canonical signalling; TC-specific activation of MSP-RON-in-macrophages, IL-33 and p38 MAPK signalling, with downregulation of LXR/RXR and SPINK1 in TC."
conditions: "IPA z-score thresholds; pathways activated/deactivated across ≥10 of 12 samples"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
IPA recovers distinct canonical-pathway activation profiles for TC and LE that align with their broader functional differences (LE invasive/translational, TC immune-modulating/differentiation).

## Evidence summary
Fig. 2f IPA heatmap.

## Conditions and scope
HPV-negative OSCC ST DEG lists.

## Counter-evidence
IPA relies on a closed knowledge base; z-score thresholds are sensitive to DEG list size.

## Linked ideas

## Open questions
Whether GP6 signalling at the LE is a drug-targetable axis.
