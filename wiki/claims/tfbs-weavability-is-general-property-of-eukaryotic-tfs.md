---
title: "199/200 surveyed eukaryotic TFs have densely-connected (k-1)-overlap binding-site graphs (weavability is general)"
slug: tfbs-weavability-is-general-property-of-eukaryotic-tfs
status: supported
confidence: 0.9
tags: [TFBS-weavability,UniPROBE,uPBM,binding-site-architecture,general-principle]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Extended Data Fig.10i, main text): 'we analysed uPBM data spanning 200 human and mouse TFs across 9 major DBD classes from the UniPROBE database. ... For 199 out of 200 TFs, the largest connected component contained more than 80% of nodes (P < 0.001, permutation test).'"
conditions: "200 human/mouse TFs from UniPROBE; top 500 8-mers per TF by uPBM E-score; 1,000 random size-matched networks for null."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Across 200 human and mouse TFs spanning 9 major DBD classes (UniPROBE), 199/200 form (k-1)-overlap k-mer graphs in which >80% of nodes lie in the largest connected component (permutation P<0.001) — establishing weavability and, by implication, the overlapping-binding-sites model as a general feature of eukaryotic TF–DNA recognition.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Extended Data Fig.10i).

## Counter-evidence

One of 200 TFs does not meet the threshold.

## Linked ideas

## Open questions

- Prokaryotic TFs untested
- Does weavability correlate with TF dosage robustness, cofactor dependence, or paralog divergence?
