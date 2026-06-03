---
title: "The scSLIDE Alzheimer trajectory correlates with the independent neuropathology CPS score (r=0.67)"
slug: scslide-alzheimer-trajectory-correlates-neuropathology-pseudoprogression
status: supported
confidence: 0.9
tags: [Alzheimer, validation, CPS, neuropathology, scSLIDE]
domain: neuroscience
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "scSLIDE trajectory vs SEA-AD continuous pseudoprogression score (CPS): Pearson r=0.67, p=5.07e-13. CPS is derived from neuropathology (pTau neurons, amyloid-beta plaques, astrogliosis) and was not given to scSLIDE."
conditions: "SEA-AD cohort; CPS is an independent, non-transcriptomic ground truth."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

The molecular disease-progression trajectory scSLIDE infers from Alzheimer snRNA-seq aligns with the SEA-AD continuous pseudoprogression score (CPS) — an independent neuropathology-derived burden measure — at Pearson r = 0.67 (p = 5.07×10⁻¹³).

## Evidence summary

Figure 3f of [[reconstructing-developmental-disease-progression-sample-level]]. CPS reflects pTau-bearing neurons, amyloid-β plaques, and astrogliosis via Bayesian modeling and uses no snRNA-seq data, making it a genuine external validation. The trajectory also tracked CERAD score, cognition, and dementia measures.

## Conditions and scope

SEA-AD cohort, where an independent ground-truth severity measure exists. This is the paper's key validation that the inferred continuum is biologically real.

## Counter-evidence

Independent CPS scores were not available for the Psych-AD replication cohort (validated there indirectly via CERAD/BRAAK).

## Linked ideas

Validates [[scslide-infers-continuous-alzheimer-disease-severity]]; strongest support for [[continuous-disease-progression-modeling]].

## Open questions

How well does the trajectory predict longitudinal clinical decline?
