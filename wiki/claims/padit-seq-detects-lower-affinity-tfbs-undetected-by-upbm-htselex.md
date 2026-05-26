---
title: "PADIT-seq detects hundreds of lower-affinity TFBSs that uPBM and HT-SELEX miss"
slug: padit-seq-detects-lower-affinity-tfbs-undetected-by-upbm-htselex
status: supported
confidence: 0.9
tags: [PADIT-seq,low-affinity,TFBS,uPBM,HT-SELEX,methodological]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (p.1-2 abstract / Fig.1): 'we developed protein affinity to DNA by in vitro transcription and RNA sequencing (PADIT-seq), with which we comprehensively assayed the binding preferences of six TFs to all possible ten-base-pair DNA sequences, detecting hundreds of novel, lower-affinity binding sites.' uPBM AUROC > 0.97 for high-affinity, HT-SELEX 'substantially lower performance, irrespective of the HT-SELEX cycle' (Fig.1d-e)."
conditions: "Six TFs: HOXD13, EGR1, NKX2.5, TBX5, Pho4, Cbf1. All-10-mer library (n=1,048,576)."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

PADIT-seq, by coupling TF binding to transcriptional output of a barcoded T7-driven reporter, identifies hundreds of lower-affinity TFBSs per TF (e.g. 554 active 10-mers for EGR1, 1,780 active 8-mers for HOXD13) that conventional uPBM E-scores and HT-SELEX cycle enrichment systematically fail to detect with reliable ordering.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Khetan et al., Nature 2025, Fig.1).

## Conditions and scope

Demonstrated across six TFs spanning C2H2 zinc-finger, homeodomain, T-box, and bHLH families. Sensitivity depends on TF / nbALFA-T7 RNAP concentrations and sequencing depth.

## Counter-evidence

None within the paper. MITOMI Kd (Fig.1b; Pearson r=0.94) and custom PBMs (Pearson r > 0.86) provide orthogonal validation.

## Linked ideas

## Open questions

- Generalisation to all DBD families
- Sensitivity floor for very weak, transient TFs (e.g. cofactor-dependent ones)
