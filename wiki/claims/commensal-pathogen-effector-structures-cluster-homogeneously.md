---
title: "Commensal and pathogen effector structures form mostly homogeneous clusters; mixed clusters depleted"
slug: commensal-pathogen-effector-structures-cluster-homogeneously
status: supported
confidence: 0.8
tags: [t3ss, effectors, structure, foldseek, alphafold]
domain: microbiology
source_papers:
  - effector-host-interactome-map-links-type
evidence:
  - source: effector-host-interactome-map-links-type
    type: supports
    strength: strong
    detail: "FoldSeek clustering of AlphaFold structures: homogeneous (commensal-only or pathogen-only) clusters overrepresented, mixed clusters II/III depleted (empirical P < 0.0001, n=10,000 label permutation), robust over parameters."
conditions: "AlphaFold-predicted tertiary structures; FoldSeek clustering."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Commensal and pathogen effectors are structurally distinct: structure clusters are
predominantly homogeneous, and mixed commensal–pathogen clusters are depleted.

## Evidence summary

[[effector-host-interactome-map-links-type]] (p.443, Fig.1c): homogeneous clusters
overrepresented, mixed clusters II/III depleted (P << 0.0001, empirical P, two-sided
label permutation test). Robust over varying FoldSeek parameters and when restricting
to vertebrate/human pathogens.

## Conditions and scope

Depends on AlphaFold prediction quality; meta-effectors clustered near random expectation.

## Counter-evidence

Some mixed cluster I exists.

## Linked ideas

Supports [[commensal-pathogen-effector-divergence]]. Uses [[foldseek]], [[alphafold-multimer]].

## Open questions

Selective forces driving separate structural trajectories.
