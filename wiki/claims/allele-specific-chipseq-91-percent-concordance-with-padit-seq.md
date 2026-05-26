---
title: "PADIT-seq identifies the preferred allele in allele-specific ChIP-seq at 91% concordance"
slug: allele-specific-chipseq-91-percent-concordance-with-padit-seq
status: supported
confidence: 0.9
tags: [allele-specific-ChIP-seq,PADIT-seq,variant-effect,in-vivo,quantitative]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Extended Data Fig.9c, main text): 'we validated PADIT-seq predictions using allele-specific ChIP-seq data. PADIT-seq identified the preferred allele with 91% concordance, substantially outperforming MotifBreakR.'"
conditions: "Allele-specific ChIP-seq dataset reference 69."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

PADIT-seq-based allelic scoring predicts which allele a TF preferentially binds in vivo with 91% concordance against allele-specific ChIP-seq, substantially better than MotifBreakR.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Extended Data Fig.9c).

## Counter-evidence

None.

## Linked ideas

## Open questions

- TF coverage of the allele-specific ChIP-seq dataset and whether PADIT-seq atlas extension is required for genome-wide application
