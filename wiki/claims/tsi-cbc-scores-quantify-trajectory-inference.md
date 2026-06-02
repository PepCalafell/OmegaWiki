---
title: "TSI and CBC scores quantify terminal-state recovery and transition fidelity for model selection"
slug: tsi-cbc-scores-quantify-trajectory-inference
status: supported
confidence: 0.8
tags:
  - trajectory-inference
  - cellrank
  - benchmarking
  - model-selection
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: strong
    detail: "TSI quantifies recovery of known terminal states vs number of macrostates; CBC quantifies how accurately a kernel recapitulates known state transitions — both used for kernel/estimator comparison."
conditions: "Both metrics require some prior knowledge (known terminal states for TSI; known state transitions for CBC) as a reference."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank provides two performance metrics for model selection in the absence of ground truth: the **terminal-state identification (TSI) score**, which quantifies how faithfully an estimator recovers known terminal states relative to the number of macrostates used, and the **cross-boundary correctness (CBC) score**, which quantifies how accurately a kernel-derived transition matrix recapitulates known cell-state transitions.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.4, p.25–26): the TSI score "quantifies how faithfully a kernel-derived transition matrix recovers known terminal states"; CBC "quantifies how accurately the kernel aligns with known state transitions." Log-ratios of CBC between two kernels, tested with Welch's t-test, give a relative reference baseline.

## Conditions and scope

Both are relative/semi-supervised metrics requiring prior biological knowledge as reference; they aid kernel choice and macrostate-count selection.

## Counter-evidence

Absolute measurement is difficult without a reference baseline; the authors recommend log-ratio comparisons instead.

## Linked ideas

(none yet)

## Open questions

- Fully unsupervised performance metrics that need no prior terminal-state knowledge.
