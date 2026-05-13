---
title: "Cytokine-driven polarization-state atlas across 17 immune cell types"
aliases:
  - cytokine-driven polarization states
  - immune cell polarization atlas
  - 66 polarization states Immune Dictionary
  - per-cell-type cytokine polarization
  - lymphocyte polarization beyond TCR/BCR
  - Mac-a Mac-b Mac-e polarization
  - NK-a NK-c NK-e NK-f polarization
  - cytokine-induced cell state plasticity
  - immune cell plasticity reference
  - polarization subcluster scRNA-seq
maturity: stable
tags:
  - cytokines
  - polarization
  - immune-plasticity
  - single-cell
key_papers:
  - dictionary-immune-responses-cytokines-single-cell
first_introduced: "2024"
date_updated: 2026-05-13
related_concepts:
  - cytokine-cell-type-specific-response-pleiotropy
  - m1-m2-polarization-paradigm
---

## Definition

Cui & Hacohen 2024 defined 66 major cytokine-driven polarization states across 17 immune cell types by subclustering each cell type and identifying subclusters significantly enriched for cytokine-treated relative to PBS-treated cells. Each state is induced by one or a handful of dominant cytokine drivers and expresses a distinguishable gene programme.

## Intuition

Extends the M1/M2 macrophage paradigm to *every* immune cell type. Demonstrates that resting lymph-node lymphocytes can be polarized by cytokines alone (no TCR/BCR signal required) — overturning the older view that lymphocyte differentiation is gated by antigen receptor signaling.

## Variants

- ISG-I states (IFNα/β/ε/κ → e.g., B-a, T4-a, Mac-a, NK-a) — universal across cell types
- ISG-II states (IFNγ, IL-2/12/15/18 → e.g., B-b, Mac-b) — STAT1-driven
- IL-1 family states (IL-1α/β → e.g., T4-c, NK-c, Treg-c, MigDC-c) — pro-inflammatory
- IL-4/13 states (Mac-e, B-f) — alternative activation
- IL-18 polyfunctional state (NK-f) — unique
- Migration states (TNF or IL-1 → MigDC-c, Mac with Ccr7)

## When to use

Reference for polarization-state assignment in any immune scRNA-seq dataset; pair with IREA for automated inference.

## Known limitations

Mouse lymph node, single 4-h timepoint, single cytokine per experiment, supraphysiological doses.

## Open problems

- Mapping mouse states to human counterparts
- Multi-cytokine combinatorial polarization (most in vivo contexts mix signals)
- Persistence/reversibility of polarization states

## Key papers

- [[papers/dictionary-immune-responses-cytokines-single-cell]]

## My understanding

A foundational reference. For HypoxiaVERSE-relevant macrophage subtyping work, Mac-a (ISG-I) / Mac-b (ISG-II / IFNγ-M1) / Mac-e (IL-4/13-M2) are the canonical anchors against which to compare tumour-derived TAM phenotypes.
