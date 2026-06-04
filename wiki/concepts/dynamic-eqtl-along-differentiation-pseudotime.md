---
title: "Dynamic eQTL along differentiation pseudotime"
aliases:
  - dynamic eQTL
  - dynamic genetic effect
tags: []
maturity: active
key_papers:
  - chinese-immune-multi-omics-atlas
first_introduced: ""
date_updated: 2026-06-04
related_concepts:
  - cell-type-specific-genetic-regulation-immune
---

## Definition

A dynamic eQTL is a genetic regulatory effect whose magnitude (and sometimes direction) changes along a continuous cell-state trajectory, such as the differentiation pseudotime of monocytes or B cells, rather than being constant within a discrete cell type.

## Intuition

Static, cell-type-binned QTL mapping can miss effects that switch on or strengthen during differentiation. Modeling the variant effect as a function of pseudotime reveals context-dependent regulation tied to developmental state.

## Formal notation

A single-cell Poisson mixed-effects (scPME) model tests the variant × pseudotime interaction on expression; an absolute effect size `|β|` that changes along pseudotime indicates a dynamic eQTL (e.g. BLK β shifting −0.54 → −0.78 in B cells).

## Variants

- Increasing-effect dynamic eQTL (e.g. BLK in B cells)
- Decreasing-effect dynamic eQTL (e.g. STIM1 in monocytes)

## Comparison

Refines [[concepts/cell-type-specific-genetic-regulation-immune]] by adding a within-lineage temporal axis to cell-type specificity.

## When to use

When a candidate causal gene shows differentiation-stage-dependent expression and the regulatory effect may not be captured by pseudobulk mapping.

## Known limitations

Pseudotime is inferred, not measured; genome-wide mapping still relied on pseudobulk for efficiency.

## Open problems

Efficient genome-wide single-cell dynamic-QTL models.

## Key papers

- [[papers/chinese-immune-multi-omics-atlas]] — 32% of B-cell and 46.9% of monocyte lead cis-eQTLs are dynamic along pseudotime (scPME model).

## My understanding

A useful reminder that "cell type" is a coarse bin; genetic regulation is a function of continuous state, which matters for developmentally regulated disease genes.
