---
title: "STAT1 and SP1 are the primary transcriptional regulators of the IFN-induced signature"
slug: stat1-sp1-primary-transcriptional-regulators-ifn
status: supported
confidence: 0.75
tags:
  - transcription-factor
  - interferon
  - GRN
  - STAT1
  - SP1
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "GRN analysis (CollecTRI regulons + decoupleR ULM) identified STAT1 and SP1 as the sole TF regulators of the IFN-induced signature; STAT1 regulates canonical IFN genes across lineages while SP1 activates a heterogeneous, cell-type-specific target set."
conditions: "Regulons with ≥10 targets; activity inferred per cell type (Level 1/2)."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

A gene-regulatory-network analysis identified STAT1 and SP1 as the primary (and, after filtering, sole) transcription-factor regulators of the IFN-induced signature in circulating immune cells. STAT1 regulated canonical IFN-signaling genes across multiple lineages, whereas SP1 drove a more heterogeneous, cell-type-specific target set.

## Evidence summary

CollecTRI regulons + decoupleR ULM on pseudobulk matrices, filtered to regulons with ≥10 targets (Methods p.652; Fig. 2e; p.637). The non-canonical role of SP1 in the IFN-induced program is a novel emphasis.

## Conditions and scope

TF-activity inference from prior-knowledge regulons; correlative, not perturbational.

## Counter-evidence

Regulon-based inference cannot fully separate SP1 from GC-box-binding paralogs; causality not tested.

## Linked ideas

- [[claims/sle-shows-opposing-stat1-sp1-activity]] · [[claims/stat1-activity-rises-during-sle-flares]]
- Foundations: [[foundations/stat1-tf]] · [[foundations/sp1-transcription-factor]] · [[foundations/collectri-tf-regulon-network]] · [[foundations/decoupler-activity-inference]]

## Open questions

- Is SP1's contribution to the IFN-induced program causal?
