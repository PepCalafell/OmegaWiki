---
title: "scVelo RNA velocity reveals a reproducible TC→LE differentiation hierarchy with field confidence > 0.85"
slug: scvelo-tc-to-le-differentiation-hierarchy
status: supported
confidence: 0.75
tags: [scVelo, RNA-velocity, differentiation, OSCC, methodological]
domain: methods/single-cell
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "scVelo dynamical model on spatially deconvolved cancer cells across all samples shows a TC→transitory→LE flow with spot velocity vector field confidence >0.85; the same direction is observed at the per-patient level."
conditions: "scVelo dynamical model; spatially deconvolved cancer cells aggregated across 12 samples"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
RNA velocity on OSCC ST cancer cells shows a consistent TC→LE differentiation hierarchy with high vector-field confidence, both in aggregate and at the per-patient level.

## Evidence summary
Fig. 6a UMAP with overlaid velocity streams; Fig. 6b per-patient examples.

## Conditions and scope
Spatially deconvolved cancer cells; scVelo dynamical model.

## Counter-evidence
Velocity assumes consistent splicing kinetics; short-horizon predictions are not lineage-tracing.

## Linked ideas

## Open questions
Whether the directionality reverses in patients on systemic therapy (e.g. neoadjuvant).
