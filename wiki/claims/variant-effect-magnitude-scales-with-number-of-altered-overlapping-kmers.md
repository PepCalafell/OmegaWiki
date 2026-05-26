---
title: "Magnitude of allelic TF binding effect scales with the number of overlapping active k-mers altered by the variant"
slug: variant-effect-magnitude-scales-with-number-of-altered-overlapping-kmers
status: supported
confidence: 0.9
tags: [noncoding-variant,overlapping-binding-sites,SNP-SELEX,EGR1,HOXD13,quantitative]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.5e-g, main text): 'A sliding window analysis of PADIT-seq active k-mers across the reference and alternate alleles revealed that the magnitude of differential binding scaled with the number of overlapping binding sites altered ... rs606231230 and rs79228650, exhibited large effects ... rs1104802 and rs73414426 ... showed modest but statistically significant effects ... systematic comparison between SNP-SELEX preferential binding scores and the number of consecutive active k-mers altered between alleles, which showed high correlation.'"
conditions: "HOXD13 and EGR1; SNP-SELEX-tested variants n=5,748 (HOXD13) and 4,136 (EGR1); custom PBM validation."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The effect of a noncoding variant on TF binding scales with the number of overlapping PADIT-seq active k-mers altered between ref and alt alleles. Variants altering many overlapping sites (rs606231230, rs79228650) have large measured effects; variants altering a single site (rs1104802, rs73414426) have modest but statistically significant effects.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.5e-g).

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

- Whether linear additivity persists for >5 simultaneously altered overlapping sites
