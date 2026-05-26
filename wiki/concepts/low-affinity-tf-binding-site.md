---
title: "Low-affinity TF binding site"
aliases:
  - "low-affinity TFBS"
  - "lower-affinity binding site"
  - "weak TF binding site"
  - "sub-optimal binding site"
  - "low-affinity DNA binding site"
  - "lower-affinity motif"
  - "sub-threshold motif match"
  - "below-PWM-threshold TFBS"
  - "non-consensus TFBS"
  - "degenerate TFBS"
tags:
  - transcription-factor
  - DNA-binding
  - low-affinity
  - cis-regulation
  - developmental-enhancer
maturity: stable
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Driver, Thoma & Nüsslein-Volhard 1989; Crocker 2015; Farley 2015"
date_updated: 2026-05-26
related_concepts:
  - overlapping-binding-sites-model
  - padit-seq
---

## Definition

A low-affinity TF binding site is a DNA sequence whose dissociation constant for a given TF is substantially weaker than the consensus high-affinity match, yet is still bound at biologically meaningful rates in vivo. These sites contribute to precise spatiotemporal gene expression (developmental enhancers — Bicoid, Pax6, Hox), confer phenotypic robustness (homotypic clusters), and underlie the cumulative binding additivity described by the overlapping-binding-sites model.

## Intuition

PWM-based motif callers throw away weak matches by design (low log-odds → no call). Two decades of developmental-biology work has shown that those discarded weak matches frequently encode genuine, function-critical TF binding. The Khetan 2025 PADIT-seq work makes this concrete at scale and recasts the lower-affinity sites as a coherent population whose collective contribution drives in vivo occupancy.

## Formal notation

- High vs low affinity is operationally a threshold on the affinity assay (e.g. uPBM E-score 0.45 vs 0.25, or PADIT-seq activity FDR cutoff)
- In PADIT-seq: hundreds of additional active k-mers per TF below the conventional uPBM E-score threshold
- Function tests: developmental enhancer reporter assays (Bicoid, Pax6), homotypic cluster MITOMI experiments, ChIP-nexus footprinting

## Variants

- Homotypic clusters of low-affinity sites (non-overlapping, tens-to-hundreds of bp apart — Crocker 2015, Segal 2008)
- Overlapping low-affinity sites (1-bp offsets — Khetan 2025, this model)
- STR-flanking low-affinity sites (Horton 2023)

## Comparison

vs high-affinity TFBS: low-affinity sites are individually weakly bound but collectively dominant when many co-occur; high-affinity sites are individually sufficient but sparser.
vs PWM consensus calls: PWM thresholds throw away most low-affinity sites; PADIT-seq detects them; SELEX biases against them through repeated selection cycles.

## When to use

- Designing developmental-enhancer reporters where graded TF dosage matters
- Interpreting why a single noncoding variant has large expression effects despite not destroying the consensus
- Understanding paralog-TF specificity at shared core motifs

## Known limitations

- Sensitivity threshold depends on the affinity assay (uPBM, BET-seq, PADIT-seq, MITOMI all draw a different cutoff)
- Functional categorisation (functional vs nonfunctional low-affinity sites) is still partially context-dependent
- Chromatin-context modulation of low-affinity sites is poorly quantified

## Open problems

- Universal definition of "low-affinity but functional" across TF families
- In vivo cofactor / chromatin contributions to low-affinity binding
- Evolutionary turnover of low-affinity sites

## Relevance to active research

[[papers/multiple-overlapping-binding-sites-determine-transcription]] uses PADIT-seq to systematically catalogue low-affinity sites and shows they together explain in vivo occupancy via the [[overlapping-binding-sites-model]].
