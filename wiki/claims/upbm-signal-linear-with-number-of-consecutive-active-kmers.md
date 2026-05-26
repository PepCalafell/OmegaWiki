---
title: "uPBM signal intensity is linear in the number of consecutive overlapping active k-mers (all six TFs)"
slug: upbm-signal-linear-with-number-of-consecutive-active-kmers
status: supported
confidence: 0.85
tags: [uPBM,overlapping-binding-sites,additive,quantitative,benchmark]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: moderate
    detail: "Quote (Extended Data Fig.8b, main text): 'uPBM signal intensities correlated linearly with the number of consecutive, overlapping active k-mers across around 40,000 60-bp probes for all 6 TFs.'"
conditions: "All-6-TFs; ~40,000 60-bp uPBM probes."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

uPBM probe signal intensity scales linearly with the number of consecutive overlapping PADIT-seq active k-mers per probe across ~40,000 60-bp probes for all six TFs, supporting the additive contribution of overlapping sites.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Extended Data Fig.8b).

## Counter-evidence

None.

## Linked ideas

## Open questions

- Departure from linearity at very high counts of overlapping sites
