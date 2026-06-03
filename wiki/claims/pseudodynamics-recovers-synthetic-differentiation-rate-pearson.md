---
title: "pseudodynamics+ recovers synthetic differentiation rate at average Pearson 0.81"
slug: pseudodynamics-recovers-synthetic-differentiation-rate-pearson
status: weakly_supported
confidence: 0.7
tags:
  - methods
  - synthetic-benchmark
  - parameter-recovery
  - quantitative
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "On synthetic 5D time-series data with known ground-truth parameters, pseudodynamics+ recovered the increasing growth-rate trend and estimated the differentiation rate per dimension at an average Pearson correlation of 0.81 (Fig. S2d)."
conditions: "Synthetic data generated from cubic-spline velocity/growth/diffusion functions; PDE-integrated densities."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

On controlled synthetic five-dimensional data, pseudodynamics+ accurately recovers ground-truth dynamic parameters, achieving an average Pearson correlation of 0.81 for the differentiation rate.

## Evidence summary

Single synthetic experiment with known generative parameters; growth-rate trend also recovered.

## Conditions and scope

Synthetic, low-dimensional; real-data parameter recovery lacks ground truth.

## Counter-evidence

None reported; 0.81 indicates good but imperfect recovery.

## Linked ideas

## Open questions

- Recovery accuracy at higher dimensions and with noisier densities.
