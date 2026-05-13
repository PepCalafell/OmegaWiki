---
title: "Propeller — cell-type composition test for scRNAseq"
slug: propeller-cell-composition-analysis
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "Propeller"
  - "speckle::propeller"
  - "cell-type composition analysis"
  - "cluster proportion test"
  - "arcsin-transformed compositional test"
  - "moderated ANOVA cell composition"
  - "Phipson propeller"
  - "cell-proportion differential test"
  - "compositional analysis scRNA-seq"
first_introduced: "Phipson et al. 2022 *Bioinformatics* (speckle package)"
date_updated: 2026-05-13
source_url: "https://github.com/phipsonlab/speckle"
---

## Definition

Propeller is a statistical method (in the R package `speckle`) for testing differences in cell-type proportions between samples in scRNAseq data. It applies a variance-stabilizing transformation (arcsin square-root or logit) to the cell-type proportions and then uses moderated t-tests / moderated ANOVA via empirical Bayes (from limma) for hypothesis testing.

## Workflow

1. Compute per-sample cell-type proportions from cluster labels.
2. Apply arcsin-square-root transformation (variance-stabilizing for proportions).
3. Fit a linear model per cluster against the condition of interest.
4. Apply empirical Bayes moderation to t-statistics.
5. Correct for multiple testing (FDR / BH).

## Strengths

- Variance-stabilizing transformation handles low-count clusters better than raw chi-square / Fisher.
- Empirical Bayes shrinkage stabilizes per-cluster variance.
- Supports paired and unpaired designs, multi-level factors.

## Limitations

- Assumes independence between cells within a sample (no within-sample correlation).
- Compositional bias: increases in one cluster mathematically force decreases in others.
- Sensitive to cluster boundaries — re-clustering can change the test.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses Propeller v0.99.1 with arcsin transformation for testing TAM cluster proportions across (i) CRC primary vs CRC liver met vs primary LIHC, (ii) primary cutaneous melanoma vs melanoma brain met vs primary GBM, and (iii) MANA-score upper vs lower quartile lung tumours.

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
