---
title: "Combining multiple kernels improves terminal-state recovery and numerical stability"
slug: combining-multiple-kernels-improves-terminal-state
status: supported
confidence: 0.75
tags:
  - trajectory-inference
  - cellrank
  - multiview
  - kernel-combination
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: moderate
    detail: "Previous analyses benefited from combining kernels (weighted average of transition matrices) in correctly identifying all terminal states and in numerical stability — one view regularizes another."
conditions: "Kernel weighting is global (not cell-specific); benefit depends on the complementarity of the combined views."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Combining several kernels via a **weighted average of their transition matrices** can improve trajectory inference: prior CellRank analyses benefited in terms of correctly identifying all terminal states and numerical stability, because one data view regularizes another.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.3): "Previous analyses benefited from this step in terms of correctly identifying all terminal states and numerical stability, as one view may regularize another."

## Conditions and scope

Combining kernels is optional (≥1 transition matrix suffices). The weighting is global; the authors note cell-specific weighting could better exploit each view's strengths.

## Counter-evidence

Benefit is qualitative/anecdotal in the protocol; global weighting may underuse strong local views.

## Linked ideas

(none yet)

## Open questions

- Can cell-specific (adaptive) kernel weighting outperform a single global weight?
