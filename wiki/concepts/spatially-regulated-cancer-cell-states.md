---
title: "Spatially regulated cancer cell states — TC and LE as plastic cell-state attractors"
aliases:
  - spatially regulated cancer cell states
  - cancer cell states TC LE
  - plastic cancer cell states
  - spatial cancer cell state continuum
  - epithelial-like vs mesenchymal-like cancer cell state
  - dynamic CSC states
  - eCSC mCSC niche
  - CD24 epithelial CSC
  - CD44 mesenchymal CSC
  - cancer cell plasticity spatial
  - cancer cell state attractor niche
tags: [cancer-stem-cells, EMT, plasticity, spatial-transcriptomics, OSCC]
maturity: active
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Arora & Cao et al. 2023 Nat Commun"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
The view that transcriptional differences between TC and LE are not explained by molecular-subtype mixing or genetic clonal diversity but rather by spatially regulated, plastic cancer cell states. Each state mixes epithelial-like cancer stem cells (CD24+, TC) and mesenchymal-like cancer stem cells (CD44+, LE) with non-stem-like malignant cells in characteristic proportions.

## Intuition
Cells with the same genome can occupy different attractors in transcriptional state space depending on their local niche. The TC vs LE position chooses which attractor they settle into; this also reconciles the prior literature on dynamic CSC states with the observed spatial structure.

## Variants
- Epithelial-like cancer stem cell (eCSC) state — TC, CD24+
- Mesenchymal-like cancer stem cell (mCSC) state — LE, CD44+
- Transitory state — intermediate, mixes TC and LE DEGs

## Comparison
HNSCC TCGA molecular subtypes (Basal, Atypical, Mesenchymal, Classical) describe whole-tumour averages; this concept argues that multiple subtypes coexist within one tumour and that the spatially defined state is a more informative axis than bulk subtype.

## When to use
- Interpreting CSC marker IHC stains spatially
- Designing therapies that target a cell *state* rather than a *subtype*
- Reasoning about EMT plasticity at the invasive front

## Known limitations
- The CSC vs non-CSC distinction inside each state remains contested
- Single-cell resolution within Visium spots is missing — markers averaged over neighbours
- Validation rests on immunofluorescence of serial sections, not lineage tracing

## Open problems
- Lineage tracing of TC ↔ LE transitions in vivo
- Whether state transitions are reversible under therapy (the in-silico Dynamo work suggests yes)

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
The paper's strongest mechanistic claim. Spatial regulation of cancer cell *states* (not just composition) sets up the rest of the story: the differentiation trajectory, the prognostic asymmetry, and the in-silico drug screen all hang on this framing.
