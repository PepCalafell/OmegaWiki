---
title: "Mscore — CXCL9+ macrophage marker-gene risk model for ICB efficacy"
aliases:
  - Mscore
tags:
  - biomarker
  - risk-model
  - ICB
  - bladder-cancer
  - macrophage
maturity: emerging
key_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
first_introduced: "2024"
date_updated: 2026-06-05
related_concepts:
  - cxcl9-spp1-tam-ratio-ici-biomarker
  - immune-checkpoint-blockade
  - sting-biomarkers-precision-immunotherapy
---

## Definition

Mscore is a five-gene transcriptomic risk score (CXCL9, C3, CTSC, CAPG, CTSB) built from Macro-CXCL9 marker genes via AIC-selected multivariate Cox regression on the IMvigor210 cohort, designed to predict immune checkpoint blockade efficacy and prognosis in bladder cancer.

## Intuition

Rather than counting a single chemokine, Mscore distils the CXCL9⁺ macrophage program into a weighted signature; CXCL9 enters with a protective (negative) weight while cathepsins (CTSC, CTSB), complement C3, and CAPG enter as risk-increasing, so a high Mscore marks an immune-unfavourable, ICB-resistant tumour.

## Formal notation

Mscore = -0.1463×CXCL9 + 0.1018×C3 + 0.1317×CTSC - 0.1869×CAPG + 0.1556×CTSB (expression-weighted).

## Variants

- Standalone Mscore vs combined Mscore+TMB+TNB (best response-prediction AUC 0.7758).

## When to use

As a candidate stratifier for anti-PD-L1 (atezolizumab) response in metastatic urothelial carcinoma, pending prospective validation.

## Known limitations

- Derived and tested only on retrospective bulk cohorts; modest discrimination; no phase-3 validation; marker-gene biology untested in bladder cancer cells.

## Open problems

- Whether Mscore adds value over simpler predictors (CXCL9, PD-L1, TMB) and generalises across platforms.

## Key papers

- [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]

## My understanding

A conventional signature-and-Cox biomarker; its novelty is the CXCL9⁺ macrophage origin of the genes rather than the modelling, and it needs external validation before clinical weight.
