---
title: "ChIP-nexus footprint grows 1 bp per additional overlapping binding site (Cbf1: 28→29→30 bp; Pho4: 27→28 bp)"
slug: chip-nexus-footprint-grows-1bp-per-overlapping-site
status: supported
confidence: 0.95
tags: [ChIP-nexus,footprint,overlapping-binding-sites,mechanistic,Pho4,Cbf1]
domain: regulatory-genomics
source_papers:
  - multiple-overlapping-binding-sites-determine-transcription
evidence:
  - source: multiple-overlapping-binding-sites-determine-transcription
    type: supports
    strength: strong
    detail: "Quote (Fig.3, main text): 'With each additional, overlapping binding site, we observed precisely one additional cut on each strand, leading to 1-bp increments in total footprint size... Cbf1: 28→29→30 bp; Pho4: 27→28 bp.' CACGTG positional artefact controlled (Extended Data Fig.7)."
conditions: "ChIP-nexus on Pho4 and Cbf1 in S. cerevisiae; peaks stratified by 3, 4, or 5 overlapping active 8-mers; CACGTG E-box register controlled."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

In ChIP-nexus data, each additional consecutive overlapping active 8-mer at a CACGTG E-box produces exactly one extra significant 5' cut on each strand and a 1-bp increase in total footprint size — the unique molecular signature of independent TF–DNA contacts predicted by the overlapping-binding-sites model and inconsistent with single extended-motif recognition.

## Evidence summary

Reported in [[papers/multiple-overlapping-binding-sites-determine-transcription]] (Fig.3).

## Conditions and scope

Pho4 and Cbf1 only; analysis restricted to peaks with CACGTG at matched register to rule out positional artefacts.

## Counter-evidence

None — the controlled CACGTG-register analysis rules out the main competing artefact.

## Linked ideas

## Open questions

- Whether mammalian TFs show the same incremental footprint pattern in ChIP-exo / ChIP-nexus data
