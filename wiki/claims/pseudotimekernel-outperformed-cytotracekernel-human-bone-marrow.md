---
title: "On CD34+ human bone marrow, the PseudotimeKernel outperformed the CytoTRACEKernel in recapitulating known state transitions"
slug: pseudotimekernel-outperformed-cytotracekernel-human-bone-marrow
status: supported
confidence: 0.75
tags:
  - trajectory-inference
  - cellrank
  - hematopoiesis
  - benchmarking
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: moderate
    detail: "On CD34+ human bone marrow, positive CBC log-ratios (Welch's t-test) favored the PseudotimeKernel over the CytoTRACEKernel; CytoTRACEKernel achieved TSI=0.85 vs optimal=1.0."
conditions: "Dataset-specific result on 6,881 CD34+ human bone marrow cells; not a general kernel ranking."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

On a CD34+ human bone marrow hematopoiesis dataset (6,881 cells), the **PseudotimeKernel recapitulated known cell-state transitions more faithfully than the CytoTRACEKernel**, shown by positive CBC log-ratios (Welch's t-test). The CytoTRACEKernel reached a TSI of 0.85 versus an optimal identification of 1.0, illustrating the difficulty of recovering all terminal states.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.7, Fig.2d, p.25–26): Procedure 2 shows "the PseudotimeKernel outperforming the CytoTRACEKernel on this specific dataset"; CTK TSI = 0.85.

## Conditions and scope

Dataset-specific (CD34+ human bone marrow); the authors stress kernel choice is data-dependent, not universal.

## Counter-evidence

This is one dataset; CytoTRACEKernel may outperform on systems lacking a reliable pseudotime/root.

## Linked ideas

(none yet)

## Open questions

- Which data properties predict, a priori, which kernel will perform best?
