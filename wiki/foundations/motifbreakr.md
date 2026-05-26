---
title: "MotifBreakR (PWM-based variant-effect predictor for TF binding)"
slug: motifbreakr
domain: "genomics / TF binding / variant effect prediction"
status: mainstream
aliases:
  - "MotifBreakR"
  - "motifbreakR"
  - "motif breakR"
  - "PWM variant effect predictor"
  - "Coetzee MotifBreakR"
  - "variant TF binding PWM tool"
first_introduced: "Coetzee, Coetzee, Hazelett *Bioinformatics* 2015"
date_updated: 2026-05-26
source_url: ""
---

## Definition

MotifBreakR is an R/Bioconductor tool that scores how a SNP changes a TF binding site by computing the log-odds difference of ref vs alt allele under one or more PWM (position weight matrix) models. It returns an effect size and a strong/weak/neutral call per (variant, TF, motif) triple. Because it relies on single-motif PWM scoring, it only models effects on the immediate motif match.

## Relevance to active research

[[papers/multiple-overlapping-binding-sites-determine-transcription]] uses MotifBreakR as the PWM-based baseline and shows PADIT-seq substantially outperforms it (AUROC 0.943 vs 0.790 for HOXD13; 0.962 vs 0.872 for EGR1) on custom-PBM-validated variant effects. The gap arises because MotifBreakR cannot see overlapping lower-affinity sites flanking the core motif, which the overlapping-binding-sites model treats as additive contributors to ref-vs-alt binding differences.
