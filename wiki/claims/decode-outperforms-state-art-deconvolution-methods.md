---
title: "DECODE outperforms state-of-the-art deconvolution methods in transcriptomic and proteomic data"
slug: decode-outperforms-state-art-deconvolution-methods
status: supported
confidence: 0.75
tags: [deconvolution, benchmark, methods]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: strong
    detail: "Top CCC across cross-donor, cross-disease, cross-health-state, cross-dataset, spatial and multi-cell-type scenarios vs 11 baselines (TAPE, CIBERSORTx, MuSiC, scpDeconv, Scaden, RCTD, Seurat, SPOTlight, Tangram, ucdselect, cell2location)."
conditions: "Self-reported benchmark by the method authors; a few methods slightly exceed DECODE in Pearson's r in scenarios 1,2,4,5."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE achieves the best overall deconvolution accuracy (CCC) on transcriptomic and proteomic data across diverse generalization scenarios, surpassing 11 state-of-the-art baselines.

## Evidence summary

Top CCC in cross-donor, cross-disease, cross-health-state, cross-dataset, spatial and multi-cell-type tasks (Fig. 2a–h). Evaluated via CCC, r.m.s.e. and Pearson's r over 15 datasets / 7 scenarios.

## Conditions and scope

Benchmark conducted by the authors of the method; advantage is clearest on CCC. On real tissue (scenario 7) DECODE shows slightly higher r.m.s.e. than TAPE/Scaden on the Monaco dataset.

## Counter-evidence

A few baselines slightly exceed DECODE in Pearson's r in scenarios 1, 2, 4 and 5 (Supplementary Figs. 1–2).

## Linked ideas

## Open questions

Independent third-party benchmarking would strengthen the generality of the claim.
