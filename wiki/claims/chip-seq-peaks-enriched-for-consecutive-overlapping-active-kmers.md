---
title: "ChIP-seq/ChIP-nexus peaks of all six TFs are enriched for multiple consecutive overlapping active k-mers"
slug: chip-seq-peaks-enriched-for-consecutive-overlapping-active-kmers
status: supported
confidence: 0.9
tags: [ChIP-seq,ChIP-nexus,overlapping-binding-sites,TF-occupancy,correlational]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.2b, main text): 'Across all 6 TFs, we found that ChIP-seq and ChIP-nexus peaks were significantly enriched for having a larger number of consecutive, active k-mers ... HOXD13 6 consecutive active 8-mers n=8,122; NKX2.5 5 consecutive n=5,985; TBX5 4 consecutive n=5,209; EGR1 4 consecutive 9-mers n=4,271; Pho4 4 consecutive 8-mers n=224; Cbf1 3 consecutive 8-mers n=280.' P values 1.01e-168 to ~0 across TFs."
conditions: "ChIP-seq for HOXD13 (mouse forelimb), EGR1 (mouse cortex), NKX2.5/TBX5 (human cardiomyocytes); ChIP-nexus for Pho4/Cbf1 (S. cerevisiae). Enrichment robust to background definition and FDR cutoff."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Genomic ChIP-seq and ChIP-nexus peaks for all six benchmarked TFs are significantly enriched for stretches of multiple, consecutive, 1-bp-step overlapping PADIT-seq active k-mers compared with length-matched genomic background.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.2b).

## Conditions and scope

Enrichment significance holds irrespective of background definition (Extended Data Fig.4a) and FDR cutoff (Extended Data Figs.4b, 5).

## Counter-evidence

Discrimination of bound vs unbound regions overall is not improved by including lower-affinity sites (Extended Data Fig.3a); the effect is on quantitative occupancy levels, not binary calls.

## Linked ideas

## Open questions

- Are similar enrichments observed for TFs of other DBD families not tested here?
