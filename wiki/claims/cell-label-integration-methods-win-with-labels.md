---
title: "Cell-label-using integration methods (scGen, scANVI) preserve single-batch cell-state differences others remove"
slug: cell-label-integration-methods-win-with-labels
status: supported
confidence: 0.85
tags:
  - data-integration
  - scRNA-seq
  - cell-labels
  - semi-supervised
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "scGen and scANVI are the only methods that preserve cell-state differences present only in a single batch. On the lung atlas task, scGen and scANVI retain neutrophil-state differences across batches that Scanorama and Harmony remove. Across human+mouse immune integration, scGen is the top-performing method by retaining nuanced biological variation across species."
conditions: "Requires consistent, high-quality cell-type annotations across batches. Quality of bio-conservation depends on annotation granularity — coarse labels (e.g. T cell vs B cell) miss fine state variation that scGen / scANVI would otherwise preserve. When labels are unavailable, Scanorama and scVI are preferred."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

scGen and scANVI — the only integration methods in the scIB benchmark that consume cell-type labels — are the only methods that preserve biological cell-state differences present in only a single batch. Their advantage over label-agnostic methods (Scanorama, scVI, Harmony) is largest on integration tasks with strong batch effects confounded with biology (e.g. across species, across tissue locations).

## Evidence summary

Quote (p.44): "Methods that use cell identity information (scGen and scANVI) must be considered separately in this tradeoff. These methods preserved biological variation most strongly. Yet, performance depended on the resolution of the cell identity labels: if specific biological variation is not encoded in cell identity labels (for example, spatial location in lung endothelial cells), scGen in particular will remove biological variation confounded with batch effects. However, if this variation is encoded (for example, neutrophil states in the lung), scGen and scANVI are the only methods that are able to preserve cell state differences that are each present only in a single batch."

## Conditions and scope

- The advantage requires accurate, biologically meaningful labels. Coarse labels collapse the advantage.
- scGen requires labels at training time; scANVI is semi-supervised and can use partial labels.
- For atlas-construction workflows where labels are derived per-batch then harmonised, this claim is a strong recommendation to use scANVI as the integration method.

## Counter-evidence

- When labels do not encode the biological variation of interest (e.g. spatial location of endothelial cells in lung), scGen actively removes that variation along with batch effect.
- Label noise propagates into the integrated embedding — bad labels produce bad integration.

## Linked ideas

(none yet)

## Open questions

- How robust is scANVI to noisy labels (e.g. 10% mislabelled cells)?
- For atlases built without per-batch annotation, can self-supervised pretraining replace cell labels in scANVI-style methods?
