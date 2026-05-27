---
title: "NiCo's per-cell-type interaction coefficients correlate with ground-truth tissue-domain cell-type enrichments more consistently than CellCharter, SpaGCN, Stagate, Banksy, SpatialPCA, and Seurat BuildNicheAssay on the Allen brain MERFISH atlas"
slug: nico-interaction-coefficients-recover-allen-brain-merfish-domains
status: supported
confidence: 0.75
tags: [spatial-transcriptomics,tissue-domain,benchmark,Allen-brain-atlas,MERFISH]
domain: methods / spatial-transcriptomics
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: moderate
    detail: "Pearson correlation between Z-scored predicted cell-type enrichment and ground-truth domain enrichment across six annotated domains (D1–D6) shows NiCo highest on average; STARmap visual cortex comparable across methods (Fig. 2g–h)."
conditions: "Allen brain MERFISH (mouse); benchmark uses author-annotated tissue domains."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

NiCo's per-cell-type interaction coefficients correlate with ground-truth tissue-domain cell-type enrichments more consistently than CellCharter, SpaGCN, Stagate, Banksy, SpatialPCA, and Seurat BuildNicheAssay on the Allen brain MERFISH atlas.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — Pearson correlation between Z-scored predicted cell-type enrichment and ground-truth domain enrichment across six annotated domains (D1–D6) shows NiCo highest on average; STARmap visual cortex comparable across methods (Fig. 2g–h).

## Conditions and scope

Allen brain MERFISH (mouse); benchmark uses author-annotated tissue domains.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
