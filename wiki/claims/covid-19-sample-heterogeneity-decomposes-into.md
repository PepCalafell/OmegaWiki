---
title: "COVID-19 sample heterogeneity decomposes into independent infection, time-since-onset, and severity axes"
slug: covid-19-sample-heterogeneity-decomposes-into
status: supported
confidence: 0.85
tags: [COVID-19, diffusion-map, severity, scSLIDE]
domain: immunology
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "COMBAT COVID-19 dataset (78 infected, 10 controls, >700k cells): DC1 separates case from control, DC2 correlates with time since onset (not severity), DC3 stratifies severity along a continuum; severity and TSO axes are uncorrelated."
conditions: "Demonstrated on the Ahern/COMBAT dataset and reproduced on an independent COVID-19 cohort (Stephenson et al)."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Applied to COVID-19 single-cell data, scSLIDE's sample-level diffusion components separate three independent axes: case-vs-control infection (DC1), time since disease onset (DC2), and disease severity along a continuum (DC3).

## Evidence summary

Figure 2 of [[reconstructing-developmental-disease-progression-sample-level]]. DC1 perfectly separates cases from controls; DC2 correlates strongly with TSO but not severity; DC3 arranges infected samples from mild to critical. Severity and TSO axes were uncorrelated.

## Conditions and scope

Shown on the COMBAT dataset; the first two axes reproduced on an independent dataset, while DC3 only partially resolved severity tiers in the smaller cohort.

## Counter-evidence

In the smaller replication dataset, DC3 did not robustly separate moderate/critical/severe, likely due to fewer patients.

## Linked ideas

Example of [[continuous-disease-progression-modeling]] disentangling axes that case-control analysis would blend.

## Open questions

How many samples are needed to resolve a given number of independent axes?
