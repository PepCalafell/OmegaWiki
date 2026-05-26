---
title: "In vivo Pho4 ChIP-seq dominance over Cbf1 increases with Pho4-specific overlapping active 8-mers (and vice versa)"
slug: in-vivo-pho4-cbf1-binding-resilience-tracks-overlapping-site-counts
status: supported
confidence: 0.85
tags: [Pho4,Cbf1,ChIP-seq,paralog-competition,in-vivo,correlational]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: moderate
    detail: "Quote (Fig.4f, main text): 'DNA sequences with a larger number of Pho4-specific consecutive active 8-mers showed reduced Cbf1 binding when Pho4 was present and vice versa. We also observed this effect in vivo, where ChIP-seq peaks containing more Pho4-specific consecutive active 8-mers showed higher Pho4 occupancy in the presence of Cbf1.'"
conditions: "Genomic context PBMs + in vivo ChIP-seq in Δpho80 and Δpho80Δcbf1 yeast strains."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The differential count of paralog-specific consecutive overlapping active 8-mers at a locus predicts which paralog wins in vitro and in vivo: more Pho4-specific overlapping sites → Pho4 displaces Cbf1 in vitro and shows higher Pho4 ChIP-seq pileup when Cbf1 is present in vivo, and the symmetric pattern holds for Cbf1.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.4f).

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

- Whether the same logic predicts paralog occupancy outcomes in mammalian co-expressed paralog pairs
