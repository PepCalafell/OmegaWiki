---
title: "Kinobeads target assignment improves CKI selectivity profiling over clinical annotations, but cellular effects reflect on+off-target combinations"
slug: kinobeads-target-assignment-improves-cki-selectivity
status: supported
confidence: 0.8
tags:
  - correlational
  - kinobeads
  - kinase-inhibitors
  - selectivity
domain: pharmacology / chemoproteomics
source_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
evidence:
  - source: integrative-epigenome-based-strategy-unbiased-functional
    type: supports
    strength: moderate
    detail: "Intra-family CKI distances using kinobeads target assignment were significantly smaller than both designated-target and random label-shuffled distances; yet some unrelated-family CKIs were equally close or closer, indicating combined on-/off-target effects."
conditions: "LPS and IL-4 networks; Kruskal–Wallis test."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Assigning CKI targets from kinobeads binding data yields functionally tighter intra-family groupings than clinical (designated) annotations, demonstrating kinobeads improves selectivity profiling — yet the residual proximity of unrelated-family CKIs shows cellular effects arise from compound-specific combinations of on- and off-target activity.

## Evidence summary

Intra-family pairwise distances were smallest under kinobeads assignment (vs designated and random) in both LPS and IL-4 networks, but inter-family pairs were sometimes equally close. See [[foundations/kinobeads-chemoproteomic-selectivity-profiling]] and [[concepts/polypharmacology-clinical-kinase-inhibitors]].

## Conditions and scope

Mouse BMDM; networks built from H3K27ac perturbation likelihoods.

## Counter-evidence

Kinobeads coverage is partial (~253/518 kinases), so the binding-based assignment is itself incomplete.

## Linked ideas

## Open questions

- Can a functional readout be used to re-annotate CKI targets beyond binding assays?
