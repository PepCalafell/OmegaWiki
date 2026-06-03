---
title: "Alzheimer case-control differential expression replicates poorly across cohorts"
slug: alzheimer-case-control-differential-expression-replicates
status: supported
confidence: 0.85
tags: [Alzheimer, case-control, reproducibility, pseudobulk-DE]
domain: neuroscience
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Using Psych-AD (299 individuals) as discovery and SEA-AD (89) as replication, only a median of 17 genes (median 17.8%) of significant case-control DE genes nominally replicated."
conditions: "Binary pseudobulk case-control DE; snRNA-seq; cross-cohort replication."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Standard binary case-control pseudobulk differential-expression analysis of Alzheimer's snRNA-seq replicates poorly between cohorts: only a median of 17 genes (17.8%) significant in the Psych-AD discovery cohort nominally replicated in SEA-AD.

## Evidence summary

Figure 3a and Supplementary Figure 6 of [[reconstructing-developmental-disease-progression-sample-level]], consistent with prior reports of low reproducibility in AD single-cell studies.

## Conditions and scope

Pseudobulk-by-donor-and-cell-type case-control DE across two snRNA-seq cohorts.

## Counter-evidence

The paper attributes the failure to the binary-label assumption rather than to DE testing per se.

## Linked ideas

Motivates [[continuous-disease-progression-modeling]]; contrasted with [[trajectory-based-differential-expression-far-more]].

## Open questions

How much of the irreproducibility is threshold-choice vs genuine cohort difference?
