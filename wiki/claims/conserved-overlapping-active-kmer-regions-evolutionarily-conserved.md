---
title: "Genomic regions with multiple consecutive overlapping active k-mers are significantly more evolutionarily conserved than flanking sequence"
slug: conserved-overlapping-active-kmer-regions-evolutionarily-conserved
status: supported
confidence: 0.85
tags: [evolution,conservation,phastCons,overlapping-binding-sites,functional]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.2d, main text): 'We found that genomic regions containing consecutive active k-mers were significantly more conserved than flanking sequences (Fig.2d) across varying numbers of consecutive, active k-mers (Supplementary Fig.1).' phastCons mm10 60-way / hg38 30-way; * adjusted P < 0.05 paired Wilcoxon."
conditions: "HOXD13, EGR1, NKX2.5, TBX5 ChIP-seq peaks. Pho4/Cbf1 omitted due to insufficient peak number."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Regions of ChIP-seq peaks containing multiple consecutive overlapping PADIT-seq active k-mers have higher phastCons evolutionary conservation scores than their immediate flanking sequences (paired Wilcoxon adjusted P<0.05), suggesting the overlapping sites are under purifying selection and therefore functional.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.2d, Supplementary Fig.1).

## Counter-evidence

Not performed for Pho4/Cbf1 due to small peak numbers; remains demonstrated for 4 TFs.

## Linked ideas

## Open questions

- Whether conservation depth tracks the *number* of overlapping sites monotonically
