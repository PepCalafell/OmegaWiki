---
title: "Denoising methods perform best with non-standard variance-stabilizing preprocessing"
slug: denoising-methods-perform-best-variance-stabilizing
status: supported
confidence: 0.75
tags:
  - denoising
  - preprocessing
  - benchmarking
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Best-practice finding from the denoising task (Supplementary Note 1.6)."
conditions: "Open Problems denoising task."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

Single-cell denoising methods perform best when paired with non-standard preprocessing approaches that better stabilize variance.

## Evidence summary

"denoising methods perform best with non-standard preprocessing approaches that better stabilize variance" (p.1038; Supplementary Note 1.6). The result implies that default log-normalisation pipelines may be suboptimal upstream of denoising.

## Conditions and scope

Denoising task only; "non-standard" preprocessing is defined relative to common log-normalisation defaults.

## Counter-evidence

Non-standard preprocessing complicates pipeline interoperability and may not transfer across denoising methods.

## Linked ideas

Another instance of [[concepts/simple-baselines-outperform-complex-single-cell]] in the sense that preprocessing choices outweigh model sophistication.

## Open questions

Which specific variance-stabilizing transform generalises best across denoising methods.
