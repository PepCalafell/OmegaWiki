---
title: "Sum of overlapping PADIT-seq activities correlates with ChIP-seq/ChIP-nexus read counts (Pearson 0.29-0.50)"
slug: sum-of-overlapping-padit-activity-correlates-with-chipseq-signal
status: supported
confidence: 0.85
tags: [PADIT-seq,ChIP-seq,quantitative,occupancy,correlational]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: moderate
    detail: "Quote (Extended Data Fig.3b-c, main text): 'the sum of PADIT-seq activity levels of all active k-mers within individual peaks was significantly correlated, albeit modestly, with normalized ChIP-seq and ChIP-nexus read counts (Pearson r = 0.29-0.50). Notably, considering only the highest affinity k-mers resulted in lower correlation ... than when lower-affinity sites were included.'"
conditions: "Per-peak summary; six TFs; r range across TFs."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Per-peak sum of PADIT-seq activities for all active overlapping k-mers correlates with normalised ChIP-seq/ChIP-nexus read counts at Pearson r=0.29-0.50; restricting to only the highest-affinity k-mers reduces the correlation, demonstrating that lower-affinity overlapping sites contribute quantitatively to in vivo occupancy.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Extended Data Fig.3b-c).

## Conditions and scope

Modest absolute correlations; the comparative result (sum > high-affinity-only) is the load-bearing observation.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

- What fraction of the residual variance is explained by chromatin / cofactors?
