---
title: "DECODE has reasonable memory and runtime efficiency among deconvolution methods"
slug: decode-reasonable-memory-runtime-efficiency-among
status: supported
confidence: 0.7
tags: [efficiency, benchmark, deconvolution]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "On the scenario-1 dataset DECODE ranked fifth in peak RAM and fourth in runtime among the compared methods (Fig. 2j,k)."
conditions: "Measured on a single dataset (scenario 1)."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE is computationally practical: on the scenario-1 dataset it ranked fifth in peak memory usage and fourth in runtime among the compared methods.

## Evidence summary

Peak RAM and runtime comparison (Fig. 2j,k) on scenario 1 placed DECODE mid-pack (5th RAM, 4th time), indicating reasonable efficiency despite being a multi-stage deep model.

## Conditions and scope

Measured on one dataset; the one-time artificial-noise-cell generation adds a fixed cost dependent on single-cell feature dimensionality.

## Counter-evidence

Not the fastest or most memory-light method; deep training has overhead.

## Linked ideas

## Open questions

Scaling behavior on very large cohorts or high-dimensional references.
