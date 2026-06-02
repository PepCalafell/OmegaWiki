---
title: "mcRigor-optimized metacell partition improves DGE concordance with paired bulk RNA-seq"
slug: mcrigor-optimized-partition-improves-dge-concordance
status: supported
confidence: 0.75
tags: [single-cell, metacell, mcRigor, differential-expression, bulk-RNA-seq]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "On paired bulk + scRNA-seq (ESC/DEC), mcRigor selected SEACells γ=13, which gave the highest bulk concordance (Pearson ρ=0.800) and the highest DE F-score (0.400) vs bulk DESeq2 genes — nearly double the single-cell F-score (0.204)."
conditions: "Human ESC and definitive endoderm; DESeq2 at FDR 0.05; bulk DE genes treated as the standard."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

The metacell configuration chosen by mcRigor produces differential-expression results most concordant with paired bulk RNA-seq, improving on single-cell DGE.

## Evidence summary

On a dataset with both bulk and scRNA-seq (human ESC and definitive endoderm cells), mcRigor optimized γ to 6 (MetaCell), 4 (SuperCell), 13 (SEACells); SEACells γ = 13 had the highest Score. That partition achieved the strongest concordance with bulk on the top 200 DE genes (Pearson ρ = 0.800) and the highest DE F-score (0.400) against bulk DESeq2 genes — roughly twice the single-cell F-score (0.204).

## Conditions and scope

Indirect validation using bulk DE genes (DESeq2, FDR 0.05) as the standard, given the absence of ground-truth DE genes in scRNA-seq.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Generalization across tissues and DE methods.
