---
title: "HVG selection improves scRNA-seq integration performance across most metrics"
slug: hvg-selection-improves-integration
status: supported
confidence: 0.9
tags:
  - data-integration
  - scRNA-seq
  - preprocessing
  - HVG
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Paired comparisons (same method, same task, HVG vs full features) across all RNA + simulation tasks: 74% of pairs had a higher overall integration score with HVG; 81% better batch removal; 66% better bio-conservation. Exceptions: trajectory and cell-cycle conservation tend to favor full feature integration."
conditions: "Holds for paired comparisons restricted to methods that accept HVG input. Cell-cycle and trajectory metrics favor full-feature input because relevant gene programs are not necessarily in the HVG set."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

HVG (highly-variable gene) selection before integration improves scRNA-seq integration outcomes in 74% of paired comparisons (same method × same task), with 81% better batch removal and 66% better bio-conservation. Cell-cycle conservation and trajectory conservation are the only metrics that favor full-feature integration, because the gene programs underlying these phenomena are not always in the HVG set.

## Evidence summary

Quote (p.45): "for HVGs, 74% of comparisons had a higher overall score; 81% had better batch removal and 66% had better bio-conservation scores. Notable exceptions were trajectory and cell-cycle conservation scores, which tended to favor full feature integration runs."

## Conditions and scope

- Compared against full feature input under the same method and task.
- Restricted to methods that accept HVG input (excludes methods that internalize HVG selection like Conos).
- When the analysis target is cell-cycle or trajectory inference, use full features; otherwise prefer HVG.

## Counter-evidence

- 26% of paired comparisons did not improve with HVG — method/task interaction is real.

## Linked ideas

(none yet)

## Open questions

- What HVG selection method (Scanpy default vs Seurat vst vs deviance-based) is optimal across methods?
- Does the HVG advantage hold for very-large atlases (>10M cells) where HVG selection itself becomes noisy?
