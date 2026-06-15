---
title: "Simple models tend to outperform complex models for perturbation prediction"
slug: simple-models-outperform-complex-models-perturbation
status: supported
confidence: 0.75
tags:
  - perturbation-prediction
  - simple-baselines
  - benchmarking
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Best-practice finding from the perturbation-prediction task (Supplementary Note 1.8)."
conditions: "Open Problems perturbation-prediction task."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

For perturbation prediction, simple models tend to outperform more complex ones in the Open Problems benchmark.

## Evidence summary

"simple models tend to outperform more complex ones for perturbation prediction" (p.1038; Supplementary Note 1.8). Together with the label-projection and denoising results, this is part of a recurring pattern across multiple Open Problems tasks.

## Conditions and scope

The perturbation-prediction task as currently scoped; complex foundation-model approaches may close the gap with larger, more diverse perturbation datasets.

## Counter-evidence

Perturbation prediction is an active frontier; later foundation-model entrants may overturn this on richer data.

## Linked ideas

Part of the cross-task evidence for [[concepts/simple-baselines-outperform-complex-single-cell]].

## Open questions

Whether large perturbation foundation models eventually surpass simple baselines on this task.
