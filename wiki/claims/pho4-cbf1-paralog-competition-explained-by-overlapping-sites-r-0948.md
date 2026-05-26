---
title: "Differential numbers of overlapping Pho4 vs Cbf1 active 8-mers predict BET-seq ΔΔΔG at Pearson r=0.948 (r²=0.898)"
slug: pho4-cbf1-paralog-competition-explained-by-overlapping-sites-r-0948
status: supported
confidence: 0.95
tags: [Pho4,Cbf1,paralog-competition,BET-seq,overlapping-binding-sites,quantitative]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.4e, main text): 'the difference in the number of consecutive active 8-mers for each TF strongly predicted which TF would dominate binding (Pearson r = 0.796; Fig.4c,d). Incorporating the relative binding strengths — that is, the PADIT-seq activities of the k-mer — yielded an even stronger correlation (Pearson r = 0.948; r² = 0.898 ± 0.0004). The overlapping binding sites model explains about 50% of the remaining variance that PWM models fail to capture (r² = 0.795 ± 0.0007).'"
conditions: "All 1,048,576 NNNNN-CACGTG-NNNNN flanking variants; BET-seq differential binding."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The differential summed PADIT-seq activity across all nine 8-mers overlapping a NNNNN-CACGTG-NNNNN sequence predicts BET-seq ΔΔΔG for Pho4 vs Cbf1 at Pearson r=0.948 (adjusted r²=0.898), explaining ~50% of the variance left unexplained by PWM-only models — a quantitative mechanism for paralog binding specificity.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.4e).

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

- Whether the same OBS-based decomposition explains paralog binding in HOX or bZIP families
