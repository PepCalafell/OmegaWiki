---
title: "scSLIDE outperforms existing sample-level embedding methods on subtle phenotypes"
slug: scslide-outperforms-existing-sample-level-embedding
status: supported
confidence: 0.8
tags: [scSLIDE, benchmark, MrVI, scPoli, PILOT, McFadden-r2]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "On SEA-AD, none of MRVI, scPoli, PILOT, unsupervised-scSLIDE, or a cell-proportion baseline reproduced the severity trajectory; scSLIDE had McFadden pseudo-r2=0.701 (case-control) and 0.526 (CPS) vs 0.189-0.330 and 0.321-0.453 for others."
conditions: "SEA-AD benchmark with CPS ground truth."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Across five alternative sample-level methods (MrVI, scPoli, PILOT, an unsupervised scSLIDE variant, and a cell-type-proportion baseline), scSLIDE alone reproduced the SEA-AD severity trajectory, achieving the best McFadden pseudo-r² for both case-control prediction (0.701 vs 0.189–0.330) and CPS prediction (0.526 vs 0.321–0.453).

## Evidence summary

Supplementary Figure 12 of [[reconstructing-developmental-disease-progression-sample-level]]; SEA-AD chosen because its subtle phenotypes have an independent CPS ground truth.

## Conditions and scope

Single benchmark dataset (SEA-AD) with subtle severity signal; "to our knowledge the only semi-supervised sample-level embedding method".

## Counter-evidence

A single benchmark; broader head-to-head comparison across diverse datasets is future work.

## Linked ideas

Benchmarks [[mrvi-multi-resolution-variational-inference]], [[scpoli-prototype-reference-mapping]], [[pilot-optimal-transport-patient-trajectory]]; supports [[supervised-dimensional-reduction-essential-resolving-subtle]].

## Open questions

How do the methods compare on datasets where the dominant axis is not disease severity?
