---
title: "Angiogenic vs. MHC-II TAM mutual exclusivity"
aliases:
  - "angiogenic-MHC-II TAM exclusivity"
  - "mutually exclusive angiogenic and MHC-II TAM programs"
tags:
  - TAM
  - macrophage-heterogeneity
  - MHC-II
  - angiogenesis
  - chromatin-accessibility
  - pan-cancer
maturity: emerging
key_papers:
  - functional-genetic-screens-reveal-key-pathways
first_introduced: "2025"
date_updated: 2026-07-23
related_concepts:
  - lgp-factor-tam-polarization-axis
  - metabolic-niche-partitioning-tam-phenotype
  - siglec15-pd-l1-mutually-exclusive-tam-dichotomization
  - pan-cancer-tam-atlas-23-clusters
---

## Definition

Across human and mouse cancers, the angiogenic (proangiogenic, VEGFA/ARG1/SPP1-marked) TAM program and the MHC-II-high (antigen-presenting, CD74/CIITA-marked) TAM program are anticorrelated and rarely co-expressed in the same cell — a conserved mutual exclusivity that unifies disparate marker-based TAM taxonomies (e.g. SPP1+/C1Q+ vs PTGS2+/C1Q+).

## Intuition

TAM diversity across the literature looks like a zoo of markers, but two opposing poles recur: a vessel-building, immunosuppressive angiogenic state and an antigen-presenting MHC-II state. A macrophage tends to commit to one, so the two signatures partition cells rather than mixing.

## Formal notation

Operationalised as a negative pairwise Pearson correlation between angiogenic and MHC-II signature scores (AUCell) across single cells, and as reciprocal chromatin accessibility at angiogenic vs. MHC-II loci.

## Variants

- Human validation: VEGFA and MHC-II protein are mutually exclusive by FACS in patient TAMs.
- Chromatin version: MHC-II loci fully closed in angiogenic TAMs; MHC-II+ TAMs carry ~27,578 more accessible sites, a more "permissive" (plastic) state.

## Comparison

Distinct from the SigLec15–PD-L1 axis ([[siglec15-pd-l1-mutually-exclusive-tam-dichotomization]]), which dichotomises TAMs on immunosuppressive-ligand identity rather than angiogenic-vs-presentation function. This axis is driven mechanistically by the [[lgp-factor-tam-polarization-axis]].

## When to use

Use to collapse cancer-specific TAM marker sets onto a common two-pole framework, or to predict that an intervention increasing MHC-II TAMs will decrease angiogenic TAMs.

## Known limitations

- ISG+ and lipid-associated states sit partly outside the two poles (ISG+ TAMs share signatures of both).
- Exclusivity is strong but not absolute; "undetermined" cells exist.

## Open problems

- Whether commitment is reversible at the single-cell level in vivo.
- The transcription-factor logic (ETS/bZIP) that enforces the switch.

## Key papers

- [[functional-genetic-screens-reveal-key-pathways]] — establishes the pan-cancer conservation, chromatin basis, and mechanistic driver of the exclusivity.

## My understanding

The most convincing evidence is the reciprocal chromatin state: mutual exclusivity is written into accessibility, not just expression, which is why it is stable and conserved across 15 cancer types.
