---
title: "HT-SELEX cycle progression preferentially enriches sequences with more consecutive overlapping active k-mers"
slug: htselex-cycle-progression-enriches-overlapping-active-kmers
status: supported
confidence: 0.85
tags: [HT-SELEX,overlapping-binding-sites,additive,affinity,methodological]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: moderate
    detail: "Quote (Extended Data Fig.8a, main text): 'we tiled HT-SELEX sequencing reads with PADIT-seq k-mers because each cycle enriches for sequences with higher TF affinity. Consistent with our model, sequences containing more overlapping active k-mers became progressively more abundant across successive rounds of selection.'"
conditions: "HT-SELEX cycles 1-4; all six benchmarked TFs."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

When HT-SELEX reads are re-analysed with PADIT-seq active k-mers, sequences carrying more consecutive overlapping active k-mers become progressively more abundant across selection rounds — consistent with overlapping sites contributing additively to total TF affinity.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Extended Data Fig.8a).

## Conditions and scope

Re-analysis of existing HT-SELEX datasets for the six PADIT-seq TFs.

## Counter-evidence

None.

## Linked ideas

## Open questions

- Quantitative recapitulation of HT-SELEX cycle enrichment from PADIT-seq affinity tables alone
