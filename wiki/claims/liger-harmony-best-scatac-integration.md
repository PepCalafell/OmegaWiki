---
title: "LIGER and Harmony are the only methods that consistently integrate scATAC-seq batches in peak/window feature spaces"
slug: liger-harmony-best-scatac-integration
status: supported
confidence: 0.85
tags:
  - data-integration
  - scATAC-seq
  - benchmarking
  - chromatin-accessibility
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "On 6 mouse-brain scATAC-seq integration tasks (3 feature spaces × small/large), LIGER and Harmony are the only methods that consistently merge batches within cell-type clusters across peaks and windows. Most other methods fail to integrate or actively degrade the data (see [[claims/most-scatac-methods-worsen-data]]). LIGER performs stronger batch removal; Harmony preserves more bio-conservation."
conditions: "Holds for peaks and windows feature spaces; gene-activity feature space is uniformly poor (see [[claims/scatac-peaks-windows-beat-gene-activity]]). Both methods focus on batch removal at the cost of nuanced biology, consistent with the broader tradeoff."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

For scATAC-seq integration on peak and window feature spaces, only LIGER and Harmony consistently integrate batches across mouse-brain datasets. Both methods prioritize batch removal over bio-conservation, which is the necessary regime for scATAC-seq where unintegrated batch structure dominates cell-type structure. LIGER performs stronger batch removal; Harmony preserves more biological variation; both outperform every method that wins on scRNA-seq.

## Evidence summary

Quote (p.46-47): "LIGER and Harmony, which focus on batch removal over bio-conservation, fully merged batches within cell-type clusters. This trend could also be seen on the large ATAC peak and window tasks, which proved prohibitively large for most methods due to poor scaling with the number of features… LIGER performs stronger batch removal than Harmony, although it leaves some batch structure within cerebellar granule cells on large ATAC tasks. In contrast, Harmony comparatively focuses more on the conservation of biological variation."

## Conditions and scope

- Tested only on mouse brain scATAC-seq (3 datasets × 11 batches in the large task).
- Peak / window feature spaces required; gene-activity feature space fails for all methods including these two.
- ComBat ranks well on aggregate but fails on small ATAC tasks and partially fails on nested batches.

## Counter-evidence

- LIGER creates artificial biological substructure from single batches on small peak/window tasks — an over-correction artifact.
- ComBat is reported as ranking among top methods overall but underperforms in small ATAC tasks.

## Linked ideas

(none yet)

## Open questions

- Does the LIGER/Harmony advantage extend to scATAC-seq atlases beyond mouse brain (e.g. immune cells, tumor)?
- Can dedicated scATAC-seq dimensionality reduction (SCALE, LSI) + MNN-anchor matching beat LIGER/Harmony?
