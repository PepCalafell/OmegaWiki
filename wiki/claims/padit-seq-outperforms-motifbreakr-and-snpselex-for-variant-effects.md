---
title: "PADIT-seq outperforms MotifBreakR and SNP-SELEX at predicting variant effects on TF binding (AUROC 0.943/0.962 vs 0.790/0.872)"
slug: padit-seq-outperforms-motifbreakr-and-snpselex-for-variant-effects
status: supported
confidence: 0.95
tags: [PADIT-seq,MotifBreakR,SNP-SELEX,variant-effect-prediction,benchmark]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.5c, main text): 'PADIT-seq outperformed existing approaches in identifying differential TF binding, achieving AUROC values of 0.943 for HOXD13 and 0.962 for EGR1. MotifBreakR ... showed notably lower performance (AUROC = 0.790 for HOXD13, AUROC = 0.872 for EGR1).' Custom PBM validation on ~280 variants per TF."
conditions: "Custom PBMs on ~280 variants each for HOXD13 and EGR1; ref/alt differential binding ground truth."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

PADIT-seq scoring of noncoding variants outperforms MotifBreakR (PWM-based) and SNP-SELEX preferential binding scores at predicting custom-PBM-validated allelic TF binding, with AUROC 0.943 (HOXD13) and 0.962 (EGR1) vs 0.790 / 0.872 for MotifBreakR.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.5c).

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

- Generalisation across TFs without an existing PADIT-seq table
