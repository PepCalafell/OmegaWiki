---
title: "scRNA-derived LASSO-Cox prognostic signature (single-cell to bulk-survival pipeline)"
aliases:
  - "single-cell-derived prognostic gene signature"
  - "scRNA-seq + bulk RNA-seq prognostic model"
  - "macrophage-DEG LASSO Cox signature"
  - "single-cell anchored survival signature"
  - "scRNA-DEG to TCGA-LASSO-Cox model"
  - "Seurat-DEG + glmnet survival pipeline"
  - "cell-type-specific prognostic gene signature"
  - "single-cell-grounded hypoxia model"
  - "TCGA prognostic model from scRNA-DEG"
  - "cell-type-resolved bulk prognostic signature"
tags:
  - prognostic-model
  - LASSO-Cox
  - scRNA-seq
  - bulk-RNA-seq
  - gene-signature
  - survival-analysis
  - TCGA
  - methodology
maturity: stable
key_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
first_introduced: "Pattern widely deployed since ~2020; Ge et al. 2025 is one instance among many (refs 7, 27–29)"
date_updated: 2026-05-25
related_concepts:
  - cell-type-abundance-from-bulk-tissue-rnaseq
---

## Definition

A standard bioinformatic pipeline that builds a prognostic gene signature with explicit single-cell provenance: (1) identify a biologically meaningful cell subpopulation in scRNA-seq (here, hypoxia-responsive TAM); (2) compute differentially expressed genes for that subpopulation between disease and control; (3) shortlist by univariate Cox regression against bulk-tissue survival (TCGA); (4) shrink to a minimal predictor set by LASSO-Cox with k-fold cross-validation (glmnet); (5) score bulk samples by the linear combination of selected genes weighted by LASSO coefficients (or by ssGSEA on the signature); (6) validate on independent bulk cohorts (ICGC, GEO).

## Intuition

Bulk transcriptomic models conflate signal across cell types. Anchoring the DEG step in a single cell type — and a single cell *state* — encodes biology that a bulk-only approach would miss, and gives each signature gene a candidate cellular producer. The downstream LASSO step preserves predictive power while collapsing the gene list to a deployable size.

## Formal notation

- DEG step: Seurat `FindMarkers`, |log2FC|>0.25, adj. p<0.05.
- Univariate Cox: `survival::coxph` per gene; keep genes with HR significantly ≠ 1.
- LASSO-Cox: `glmnet::cv.glmnet(family="cox")`; choose λ at minimum partial-likelihood deviance.
- Final score: per-patient linear predictor or per-sample ssGSEA on the selected gene set; usually dichotomised at median for KM plots.

## Variants

- LASSO vs elastic-net vs ridge in the shrinkage step.
- ssGSEA scoring vs raw LP scoring for downstream stratification.
- Univariate-Cox-only (no LASSO) vs univariate + LASSO + multivariate.
- Direct LP scoring of an external cohort vs re-fitting weights on each cohort.

## Comparison

- vs bulk-DEG prognostic signatures (most pre-2020 work): provides cell-type provenance but inherits all the limitations of bulk LASSO-Cox.
- vs deep-learning bulk survival models: simpler, more interpretable, smaller effective sample size requirements.

## When to use

- When a candidate prognostic mechanism is hypothesised to act through a specific cell type or state (TAM hypoxic response, T-cell exhaustion, fibroblast subset).
- When integrating a hypothesis-rich scRNA-seq atlas with the larger but cell-type-blind TCGA bulk cohort.

## Known limitations

- The signature inherits the noise and identifiability problems of small-sample univariate Cox; LASSO partially mitigates but does not eliminate.
- Training and reporting on the same TCGA cohort is the norm; held-out evaluation is rare.
- The "cell-type provenance" is descriptive at training time; nothing prevents bulk samples with very different cell-type composition from scoring high.
- Many such signatures are published per disease and converge on a handful of recurring genes (e.g. PLAU in hypoxia signatures), so novelty per signature is often marginal.

## Open problems

- Calibration benchmarks across multiple cell-type-anchored signatures for the same disease.
- Whether deconvolution (CIBERSORTx, Tamborero) + per-cell-type expression infers the same signatures as direct scRNA-DEG, at a fraction of the data cost.

## Key papers

- [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] — TAM-anchored hypoxia signature in PDAC (this paper).

## My understanding

For my thesis, this is the dominant idiom for "translating single-cell biology into a clinical-grade biomarker." Useful to be familiar with the pattern even though novelty per individual instance is low. The hard problem in this space is not the pipeline but the question — *which cell state* anchors the most informative signature.
