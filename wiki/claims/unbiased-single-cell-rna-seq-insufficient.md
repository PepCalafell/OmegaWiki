---
title: "Unbiased single-cell RNA-seq is statistically insufficient for rare cell types; enrichment is mandatory"
slug: unbiased-single-cell-rna-seq-insufficient
status: weakly_supported
confidence: 0.7
tags: [single-cell, experimental-design, rare-cell-types, enrichment, power-analysis]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Dozens of samples needed even under most optimistic assumptions; 'standard unbiased single-cell RNA sequencing is insufficient... and cell type enrichment is mandatory.'"
conditions: "Rare populations at stringent (FDR-corrected) significance; conclusion from order-of-magnitude calculation."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Because reaching FDR-corrected significance for a rare cell population requires dozens of biological replicates — often cost-prohibitive — standard "unbiased" single-cell RNA-seq is statistically insufficient to interrogate such populations at the desired significance, making cell-type enrichment effectively mandatory.

## Evidence summary

Design conclusion drawn from the worked rare-cell sample-size example (see [[claims/rare-cell-type-log2-fold-change]], [[claims/genome-wide-fdr-correction-sharply-increases]]).

## Conditions and scope

Applies to rare-population DE goals at stringent significance; not a claim about all single-cell experiments.

## Counter-evidence

Exact thresholds depend on dispersion and effect size; some questions tolerate weaker significance or larger effects.

## Linked ideas

- [[concepts/rare-cell-type-single-cell-enrichment]]

## Open questions

- Quantitative power/cost trade-off of specific enrichment strategies.
