---
title: "oncoPredict — in-silico bulk-RNA drug sensitivity prediction"
slug: oncopredict-drug-sensitivity
domain: "methods / pharmacogenomics"
status: mainstream
aliases:
  - "oncoPredict"
  - "oncoPredict R package"
  - "GDSC-based IC50 prediction"
  - "pRRophetic successor"
  - "bulk RNA IC50 prediction"
  - "calcPhenotype"
first_introduced: "Maeser, Gruener, Huang 2021 Brief Bioinform (oncoPredict R package, descendant of pRRophetic)"
date_updated: 2026-05-25
source_url: "https://cran.r-project.org/web/packages/oncoPredict/"
---

## Definition

An R package that predicts per-sample drug sensitivity (typically log-IC50) from bulk-tumour transcriptomes by training ridge-regression models on cell-line training data (most commonly GDSC) and applying them to TCGA-style tumour expression profiles. Successor to pRRophetic with extended cell-line databases and corrected batch handling.

## Intuition

If gene-expression patterns in cancer cell lines predict measured IC50 of compound X, the same patterns in tumour transcriptomes should rank-order tumour samples by predicted sensitivity. The output is an *in-silico* IC50 estimate, useful for hypothesis generation rather than direct clinical inference.

## Formal notation

- Training: ridge regression of log-IC50 on cell-line bulk RNA expression (GDSC1, GDSC2, CTRP).
- Prediction: `calcPhenotype` applied to tumour expression matrix.
- Output: per-sample predicted log-IC50 per drug.

## Key variants

- GDSC1 vs GDSC2 vs CTRP training compendia.
- pRRophetic (predecessor) is broadly equivalent in spirit.

## Known limitations

- Predicted IC50 is not measured patient response; the absolute scale is heuristic.
- Confounded by stromal contamination of bulk tumour RNA.
- Limited to compounds with sufficient cell-line training data.

## Open problems

- Calibration against clinical response data is rarely performed.
- Spatial / single-cell-resolved drug sensitivity prediction is still nascent.

## Relevance to active research

oncoPredict is the workhorse for "high-hypoxia tumours are predicted to be resistant to drug X" claims in transcriptomics-only studies. Used in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] for gemcitabine, oxaliplatin, cisplatin, 5-FU, and paclitaxel sensitivity prediction in TCGA-PAAD.
