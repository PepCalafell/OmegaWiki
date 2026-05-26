---
title: "Avoiding data-integration methods (Harmony/scANVI/Seurat) preserves biological signal in cancer scRNA-seq compendia"
slug: cca3-no-data-integration-preserves-biological-signal
status: weakly_supported
confidence: 0.55
tags: [batch-correction, integration, scrna-seq, atlas, methods, opinion]
domain: methods
source_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
evidence:
  - source: curated-cancer-cell-atlas-provides-comprehensive
    type: supports
    strength: moderate
    detail: "Authors argue scANVI/Harmony/Seurat integration removes biological signal in cancer because most variation comes from unique genetic/epigenetic states, not batch."
conditions: "Position is a design choice rather than a head-to-head benchmark; effect depends on the analysis."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

For pan-cancer malignant-cell scRNA-seq analyses focused on intratumour heterogeneity, avoiding batch correction and integration methods preserves biologically meaningful inter-tumour variation that integration tools tend to remove.

## Evidence summary

Stated as a design choice in 3CA v2 Discussion (p.1096) with the rationale that cancer transcriptional variation is dominated by tumour-specific genetic/epigenetic profiles rather than technical batch effects.

## Conditions and scope

Applies to MP discovery and ITH characterization; cell-to-cell expression comparison across studies is sacrificed.

## Counter-evidence

For TME cell-type-level analyses, integration can be useful and may not destroy signal at the same magnitude. Some benchmarks ([[benchmarking-atlas-level-data-integration-single]]) show scANVI/scVI/Harmony preserve biology reasonably well in many contexts.

## Linked ideas

—

## Open questions

- Can a "cancer-aware" integration method preserve malignant ITH while reducing technical batch effects?
- Would integrated 3CA yield additional MPs or destroy some of the existing 67?
