---
title: "Novae produces nested hierarchical spatial domains that switch resolution without re-clustering"
slug: novae-nested-hierarchical-spatial-domains-no-reclustering
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - hierarchical-clustering
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Prototypes (elementary spatial domains) are regrouped to form higher-level domains at user-chosen resolution; assignment is a fast mapping rather than re-clustering. Fig. 2 and 'Assignment to spatial domains' methods."
conditions: "Hierarchical assignment is a mapping from prototypes — quality depends on a sufficiently broad prototype catalogue."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Novae returns spatial-domain labels at any desired resolution via a near-zero-cost mapping over a fixed set of learned prototypes, avoiding the per-resolution re-clustering required by Leiden/mclust pipelines.

## Evidence summary

Fig. 2 (heatmaps of prototype weights and dendrograms); methods section "Assignment to spatial domains" describes the prototype-to-resolution mapping as a vectorial operation.

## Conditions and scope

Quality of the hierarchy depends on training-time prototype diversity. Resolution levels are bounded by the number of learned prototypes.

## Counter-evidence

— none reported.

## Linked ideas

— none yet.

## Open questions

- Optimal prototype count as a function of training-corpus diversity.
