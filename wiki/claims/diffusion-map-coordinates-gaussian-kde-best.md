---
title: "Diffusion-map coordinates with Gaussian KDE best recapitulate the pseudotime density ground truth"
slug: diffusion-map-coordinates-gaussian-kde-best
status: weakly_supported
confidence: 0.65
tags:
  - methods
  - density-estimation
  - diffusion-map
  - benchmark
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "Benchmark on a megakaryocyte differentiation dataset: diffusion-map + traditional Gaussian KDE best captured developmental stages and density progression vs TIGON GMM, Mellon, Denmarf, hashing-KDE; TIGON had high correlation but missed Day-3 stem accumulation and Day-7 transition."
conditions: "Evaluated on one single-lineage HSC→megakaryocyte dataset with a pseudotime-based ground truth."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

For density estimation feeding the PINN, diffusion-map coordinates coupled with traditional Gaussian KDE most faithfully reproduce the pseudotime-based density ground truth, outperforming GMM, Gaussian-process, and deep-learning density estimators.

## Evidence summary

Single-dataset benchmark; choice justified by best recovery of stage-specific dense regions.

## Conditions and scope

One single-lineage benchmark; generality to other systems untested.

## Counter-evidence

TIGON's estimator achieved high correlation overall (but failed on specific transitions).

## Linked ideas

## Open questions

- Whether the same combination wins on multi-lineage / higher-dimensional data.
