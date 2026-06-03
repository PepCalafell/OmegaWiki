---
title: "Spatially-constrained ligand-receptor interaction inference"
aliases: ["spatial constraint LR inference", "neighbourhood-constrained cell-cell interaction"]
tags: [spatial-omics, cell-cell-interaction, ligand-receptor, methods]
maturity: active
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2023"
date_updated: 2026-06-03
related_concepts: [spatial-multiomics-orthogonal-validation, cross-platform-spatial-meta-community]
---

## Definition

Inference of ligand-receptor (L-R) cell-cell interactions that requires the interacting cells/spots to be spatial neighbours, rather than inferring interactions purely from co-expression in dissociated data. Implemented for example by stLearn's spatially-constrained two-level permutation (SCTP) and integrated across replicates/platforms by MMCCI.

## Intuition

Tissue dissociation in scRNA-seq removes spatial context, so two cell types can be predicted to interact even if they reside in distant tissue regions (false positives). Adding a spatial-neighbour constraint removes biologically implausible interactions and, conversely, recovers interactions that scRNA-seq missed but that are visible as co-expression between neighbouring cells in spatial data.

## Formal notation

For L-R pair (l,r) and neighbouring spots/cells (i,j): score from co-expression of l in i and r in neighbour j; significance via permutation over expression and spatial labels (see [[stlearn-sctp-spatial-lr]]).

## Variants

- Spot-level (Visium) vs single-cell (CosMx, Xenium)
- Single-sample SCTP vs multi-sample MMCCI integration

## Comparison

Improves specificity over dissociated-data tools (e.g. CellChat / CellPhoneDB applied to scRNA-seq) by adding spatial constraints; complements them rather than replacing the L-R database itself.

## When to use

Whenever spatial data are available and the goal is high-confidence, cell-type-resolved interactions for downstream validation or therapeutic-target nomination.

## Known limitations

- Sensitive to neighbourhood radius definition
- Restricted to panel genes on imaging platforms
- Proximity co-expression is inference, not direct binding proof

## Open problems

- Optimal neighbourhood scales across platforms
- Distinguishing autocrine/juxtacrine/paracrine modes

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — applies SCTP/stLearn across CosMx, Visium, Xenium, showing removal of scRNA-seq false positives (XCL1-XCR1) and recovery of missed interactions (WNT5A-ROR1).

## My understanding

A correction to the dominant dissociated-data interaction paradigm: space is a hard prior that filters and rescues predicted interactions, and is essential before nominating drug targets.
