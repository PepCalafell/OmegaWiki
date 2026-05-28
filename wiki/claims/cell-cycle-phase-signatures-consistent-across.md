---
title: "Cell-cycle phase signatures are consistent across cell types"
slug: cell-cycle-phase-signatures-consistent-across
status: weakly_supported
confidence: 0.6
tags: [cell-cycle, cell-state, proteomics]
domain: cell biology
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Differentially expressed proteins across cell-cycle phases but within the same phase show cell state yields highly consistent protein expression regardless of cell type (Fig. 4b); melanoma-trained model tested on monocytes."
conditions: "Observed for cell-cycle proteins in monocytes vs melanoma; supports cross-type transfer of state deconvolution."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Cell-state (cell-cycle phase) protein-expression signatures are highly consistent across different cell types, so a model trained on one cell type's states can deconvolve another's.

## Evidence summary

Differentially expressed proteins across G1/S/G2 within a phase were consistent between monocytes and melanoma cells (Fig. 4b); melanoma cells were used for training and monocytes for testing, and DECODE still performed best (Fig. 4d).

## Conditions and scope

Demonstrated for cell-cycle-phase proteins in two cell types; underpins cross-type state-deconvolution feasibility.

## Counter-evidence

Generalization beyond cell-cycle phase and these two cell types is untested.

## Linked ideas

## Open questions

Whether other state axes (activation, differentiation) share signatures across types as strongly.
