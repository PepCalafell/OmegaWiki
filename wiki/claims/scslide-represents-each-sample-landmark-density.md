---
title: "scSLIDE represents each sample as a landmark relative-density profile"
slug: scslide-represents-each-sample-landmark-density
status: supported
confidence: 0.9
tags: [scSLIDE, sample-level, density, methods]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Method section and Figure 1: each sample is summarized by the density of its cells around ~5,000 landmark cells, producing a sample-by-landmark relative-density matrix used for all downstream analysis."
conditions: "Requires a cell-level embedding and a representative landmark set."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

scSLIDE transforms each sample's single-cell data into a compact profile that records where its cells fall in a high-dimensional embedding, by quantifying the density of the sample's cells around a fixed set of landmark cells.

## Evidence summary

Defined in the Method and Figure 1 of [[reconstructing-developmental-disease-progression-sample-level]]. The procedure builds a "landmark abundance" matrix (k-nearest-landmark counts aggregated per sample) and normalizes it into a relative-density matrix.

## Conditions and scope

Methodological definition; holds by construction of the framework.

## Counter-evidence

None within the paper.

## Linked ideas

Implements [[sample-level-embedding]] via [[landmark-based-density-estimation]].

## Open questions

How sensitive is the profile to landmark count and embedding quality across very large atlases?
