---
title: "Holdup assay"
slug: holdup-assay
domain: methods
status: mainstream
aliases:
  - holdup assay
  - hold-up assay
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

The holdup assay is a quantitative, in vitro, chromatographic method for measuring
the affinity of domain–motif interactions. Purified domains (e.g. PDZ domains) are
incubated with peptide ligands; the fraction of ligand "held up" by the immobilized
domain yields an equilibrium dissociation constant (Kd).

## Intuition

Stronger binding = more peptide retained. Running many domain×peptide pairs in
parallel gives a quantitative interaction matrix with affinity values.

## Formal notation

Output is a Kd (µM) per domain–peptide pair, often visualized as a heatmap; positives
can be cross-referenced against orthogonal assays (e.g. Y2H).

## Key variants

PDZ-domain holdup against C-terminal PDZ-binding motif (PBM) peptides; tandem-domain
configurations.

## Known limitations

Tests defined domain/peptide fragments, so interactions needing full-length context
or tandem-domain arrangements may be missed.

## Relevance to active research

Used to validate predicted PDZ–PBM interfaces between human PDZ proteins and the
C-termini of commensal T3SS effectors (16/23 Y2H pairs confirmed).
