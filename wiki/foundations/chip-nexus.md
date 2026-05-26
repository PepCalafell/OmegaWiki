---
title: "ChIP-nexus (ChIP with nucleotide-resolution exonuclease and barcoded ligation)"
slug: chip-nexus
domain: "genomics / methods / TF binding"
status: mainstream
aliases:
  - "ChIP-nexus"
  - "ChIP-Nexus"
  - "ChIP nexus"
  - "chromatin immunoprecipitation with exonuclease"
  - "nucleotide-resolution ChIP"
  - "exonuclease-trimmed ChIP"
  - "ChIP-exo"
  - "single-base ChIP footprinting"
first_introduced: "He et al. *Nat Biotechnol* 2015 (ChIP-nexus)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

ChIP-nexus is a variant of ChIP-exo that combines chromatin immunoprecipitation with 5'→3' lambda-exonuclease trimming, a unique molecular barcode (UMI), and single-ligation library construction. The exonuclease stops at the TF–DNA crosslink, so the 5' ends of reads pinpoint individual TF–DNA contact points at single-bp resolution. Footprint expansion (distance between leftmost and rightmost significant cuts) and per-position "cut" counts are interpretable as discrete TF-binding events.

## Relevance to active research

In [[papers/multiple-overlapping-binding-sites-determine-transcription]], ChIP-nexus on Pho4 and Cbf1 in S. cerevisiae provides the strongest in vivo evidence for the overlapping-binding-sites model: each additional overlapping active 8-mer produces one additional significant 5' cut on each strand, and footprint size grows in 1-bp increments — a molecular signature uniquely consistent with independent TF occupancy at each consecutive overlapping site, distinguishing the model from "extended-motif" alternatives.
