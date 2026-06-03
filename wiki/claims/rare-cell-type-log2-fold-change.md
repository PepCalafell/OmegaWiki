---
title: "Detecting log2FC=1 in a rare cell type requires several samples per condition (nominal p=0.05)"
slug: rare-cell-type-log2-fold-change
status: supported
confidence: 0.8
tags: [single-cell, power-analysis, rare-cell-types, sample-size, quantitative]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Worked example: rare cell type 1% of 10,000 cells, pseudobulk expr ≈10; log2FC=1 at nominal p=0.05 needs 6 samples/condition (3/14 low/high dispersion)."
conditions: "Single-nucleus design; average expression >0.1 molecules/cell; nominal (uncorrected) p=0.05."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

For a rare cell type comprising 1% of a 10,000-cell sample with average expression >0.1 molecules/cell (pseudobulk expression ≈10), detecting a \(\log_2\mathrm{FC}=1\) at a nominal p-value of 0.05 requires about 6 samples per condition under the typical-dispersion curve — 3 (optimistic) to 14 (pessimistic) across the dispersion band.

## Evidence summary

Direct application of the analytical procedure (worked numerical example in the Analysis section).

## Conditions and scope

Nominal, uncorrected significance; the requirement grows sharply once multiple-testing correction is applied (see [[claims/genome-wide-fdr-correction-sharply-increases]]).

## Counter-evidence

Estimates rest on the heuristic dispersion band; real designs may need more.

## Linked ideas

- [[concepts/rare-cell-type-single-cell-enrichment]]
- [[concepts/analytical-power-analysis-deseq2-model]]

## Open questions

- How sensitive is the requirement to the assumed per-cell expression and cell fraction?
