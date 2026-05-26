---
title: "uPBM E-scores predict PADIT-seq active k-mers with AUROC > 0.97 across all six TFs"
slug: upbm-escore-aurocs-above-097-for-padit-seq-active-kmers
status: supported
confidence: 0.95
tags: [uPBM,PADIT-seq,AUROC,benchmark,methodological]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.1d, main text): 'uPBM E-scores showed strong predictive power across all TFs (AUROC > 0.97), HT-SELEX enrichment scores demonstrated substantially lower performance, irrespective of the HT-SELEX cycle analysed.'"
conditions: "Six TFs (HOXD13, EGR1, NKX2.5, TBX5, Pho4, Cbf1). k=8 for most, k=9 for EGR1."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

uPBM E-scores discriminate PADIT-seq active k-mers from inactive k-mers with AUROC > 0.97 across all six benchmarked TFs, while HT-SELEX enrichment AUROC is substantially lower at every cycle.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.1d).

## Conditions and scope

Comparison run for k=8 for HOXD13, NKX2.5, TBX5, Pho4, Cbf1; k=9 for EGR1.

## Counter-evidence

None.

## Linked ideas

## Open questions

- Whether the AUROC gap shrinks for TFs with lower-affinity preferences not captured here
