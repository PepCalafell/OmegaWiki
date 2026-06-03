---
title: "scSLIDE infers a continuous Alzheimer disease-severity trajectory via principal curve"
slug: scslide-infers-continuous-alzheimer-disease-severity
status: supported
confidence: 0.85
tags: [Alzheimer, trajectory, principal-curve, scSLIDE]
domain: neuroscience
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Diffusion components 1-2 of the SEA-AD sample-level density matrix were continuous (not discrete case-control); a joint principal curve fit through them inferred a pseudo-trajectory of disease progression across donors, reproduced in Psych-AD."
conditions: "SEA-AD and Psych-AD snRNA-seq cohorts."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

In Alzheimer's snRNA-seq data, scSLIDE's sample-level diffusion components vary continuously rather than splitting into discrete case/control groups, and fitting a joint principal curve through them yields a continuous disease-progression trajectory across donors.

## Evidence summary

Figure 3c of [[reconstructing-developmental-disease-progression-sample-level]]; the trajectory revealed intra-group heterogeneity (e.g. Donor_82 strongly shifted vs Donor_12 control-like) and was reproduced in the Psych-AD cohort (Figure 4b).

## Conditions and scope

Demonstrated on SEA-AD and reproduced on Psych-AD.

## Counter-evidence

The trajectory is a computational prediction requiring independent validation (provided by CPS, see linked claim).

## Linked ideas

Instance of [[continuous-disease-progression-modeling]] using [[principal-curve-fitting]]; validated by [[scslide-alzheimer-trajectory-correlates-neuropathology-pseudoprogression]].

## Open questions

Does the same continuous structure hold in earlier preclinical AD cohorts?
