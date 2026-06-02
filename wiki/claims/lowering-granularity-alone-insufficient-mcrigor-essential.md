---
title: "Lowering granularity alone is insufficient; coarse partition + mcRigor filtering beats a naively fine partition"
slug: lowering-granularity-alone-insufficient-mcrigor-essential
status: supported
confidence: 0.75
tags: [single-cell, metacell, mcRigor, granularity, statistical-power]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "SEACells (γ=90) + mcRigor gave greater statistical power and more biologically supported enhancer-gene associations than fine-grained SEACells (γ=5): a validated GATA2 enhancer (LOC117038771) and multiple TAL1 HCPs were detected only with γ=90 + mcRigor, not with γ=5 or single cells."
conditions: "HSPC multiome data; fine γ leaves sparsity unresolved, reducing detection power."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Avoiding dubious metacells by simply using a low granularity level is not a substitute for mcRigor: a coarse partition (more aggregation, less sparsity) filtered by mcRigor delivers more statistical power and more biologically supported associations than a fine partition.

## Evidence summary

SEACells (γ = 90) + mcRigor outperformed SEACells (γ = 5, without mcRigor): a previously reported GATA2-regulating enhancer (LOC117038771) and multiple TAL1 highly-correlated peaks were detected only with the coarse-plus-filter strategy, while sparsity limited detection at γ = 5 and at single-cell resolution.

## Conditions and scope

Demonstrated on the HSPC multiome enhancer-gene inference task.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Whether the advantage holds for tasks other than regulatory inference.
