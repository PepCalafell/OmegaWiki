---
title: "Generative probabilistic integration (scVI/scANVI) outperforms alternatives for annotated atlas integration"
slug: scanvi-generative-integration-outperforms-alternatives-annotated
status: weakly_supported
confidence: 0.75
tags:
  - data-integration
  - scANVI
  - benchmarking
  - atlas
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "Generative probabilistic models (scVI/scANVI) showed superior performance integrating complex datasets vs other approaches, particularly when cell annotations are available; scANVI was selected as the atlas integration method for its top-ranked benchmark performance."
conditions: "Atlas-scale, annotated single-cell data; integration quality measured on benchmark metrics."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

For atlas-level integration of the inflammation cohort, generative probabilistic models (scVI and its semi-supervised extension scANVI) outperformed alternative integration approaches, especially when cell-type annotations were available, motivating the choice of scANVI as the integration backbone.

## Evidence summary

Stated at p.634 and reiterated in the integration-method comparison (p.641). Consistent with external scIB benchmarks the authors cite.

## Conditions and scope

Holds for annotated, atlas-scale data; the paper later shows linear methods (Harmony) can generalize better on unseen studies (see [[claims/harmony-generalizes-best-among-integration-methods]]).

## Counter-evidence

On unseen-study generalization, VAEs (scANVI) lost more predictive power than linear methods, qualifying the superiority claim.

## Linked ideas

- [[concepts/atlas-level-data-integration]] · [[concepts/batch-removal-vs-bioconservation-tradeoff]]

## Open questions

- Does scANVI's advantage hold without query labels for tuning?
