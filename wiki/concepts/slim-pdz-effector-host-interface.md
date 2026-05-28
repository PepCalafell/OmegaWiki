---
title: "SLiM- and PDZ-mediated effector–host interfaces"
aliases:
  - SLiM-domain effector interface
  - PDZ-PBM effector interface
tags:
  - microbiome
  - host-pathogen
  - slim
  - pdz-domain
maturity: emerging
key_papers:
  - effector-host-interactome-map-links-type
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts:
  - effector-interaction-sequence-independence
  - microbiome-host-meta-interactome-hummi
---

## Definition

The finding that a substantial fraction of commensal effector–host interactions are
mediated by short linear motifs (SLiMs) in the bacterial protein binding human globular
domains — most prominently bacterial C-terminal PDZ-binding motifs (PBMs) engaging human
PDZ domains — rather than by large globular interfaces.

## Intuition

Bacteria can "mimic" host motifs: a short C-terminal tail acts like a host ligand and
docks into a host domain pocket, a mode AlphaFold often misses but motif-template
inference (mimicINT) and the holdup assay can capture and quantify.

## Formal notation

mimicINT identified 54 SLiM–domain interfaces in HuMMIMAIN (51 pass ≥1 stringency,
P = 0.0137; 22 pass two criteria, P = 0.0005). The largest group: 23 PDZ–PBM
interactions; 16/23 (70%) validated by holdup assay.

## Variants

Globular interface (AlphaFold-Multimer) vs SLiM–domain (mimicINT); single vs tandem PDZ
domains.

## Comparison

Connects bacterial effector mimicry to the broader SLiM-mediated interaction literature
(ELM).

## When to use

When predicting or validating effector–host binding modes, especially via host
[[pdz-domain]] scaffolds.

## Known limitations

Predictions require experimental validation; tandem-domain requirements can cause
assay misses.

## Open problems

How widespread is functional mimicry without sequence similarity among commensal
effectors?

## Key papers

- [[effector-host-interactome-map-links-type]]

## My understanding

The structural-mechanistic layer explaining how divergent effectors achieve specific
host targeting.
