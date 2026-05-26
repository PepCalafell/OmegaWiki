---
title: "uPBM (universal protein-binding microarray)"
slug: upbm-protein-binding-microarray
domain: "biochemistry / TF binding / in vitro"
status: mainstream
aliases:
  - "uPBM"
  - "universal PBM"
  - "protein-binding microarray"
  - "PBM"
  - "Bulyk PBM"
  - "universal protein-binding microarrays"
  - "DNA-binding specificity microarray"
  - "all-8-mer microarray"
first_introduced: "Mukherjee et al. 2004 / Berger et al. *Nat Biotechnol* 2006 / Berger & Bulyk *Nat Protoc* 2009"
date_updated: 2026-05-26
source_url: ""
---

## Definition

A universal protein-binding microarray (uPBM) is a double-stranded DNA microarray designed so that every possible 8-mer (and many 10-mers) is represented multiple times across the array. A purified, epitope-tagged DBD is hybridised, and bound TF is detected by fluorescent anti-tag antibody. Two summary scores per 8-mer are reported: a median signal intensity (continuous affinity proxy) and an E-score (∈ [-0.5, 0.5], rank-based; E > 0.45 marks high-confidence binding).

## Relevance to active research

In [[papers/multiple-overlapping-binding-sites-determine-transcription]], uPBM E-scores serve as the gold-standard reference for PADIT-seq calibration — uPBM E-scores correlate strongly with PADIT-seq active k-mers (AUROC > 0.97 across all six TFs), establishing that PADIT-seq recapitulates known high-affinity binding while extending detection into the lower-affinity regime that uPBM probes cannot reliably quantify.
