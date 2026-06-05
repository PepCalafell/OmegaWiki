---
title: "Macro-CXCL9 as the early/progenitor node of tumor macrophage differentiation"
aliases:
  - Macro-CXCL9
  - CXCL9+ macrophage progenitor node
tags:
  - macrophage
  - trajectory
  - CXCL9
  - tumor-immunology
maturity: emerging
key_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
first_introduced: "2024"
date_updated: 2026-06-05
related_concepts:
  - ifng-mac-cxcl9-tam-ici-responder
  - cxcl9-spp1-tam-ratio-ici-biomarker
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

The proposal — in bladder cancer scRNA-seq — that the CXCL9⁺ macrophage subpopulation (Macro-CXCL9) sits at the initial node of the tumour macrophage differentiation trajectory, branching toward Macro-SPP1 and Macro-FOLR2 states, and carries a distinct transcription-factor program (LYL1, NRF1, SMARCC2, CCNT2, TCF3).

## Intuition

Where the CXCL9:SPP1 framework treats CXCL9⁺ and SPP1⁺ TAMs as opposite polarity endpoints, this view casts the CXCL9⁺ state as developmentally upstream — an IFN-γ-experienced starting point from which protumour SPP1/FOLR2 programs emerge.

## Variants

- Trajectory-origin interpretation (developmental hierarchy) vs IFN-γ-exposure-state interpretation (reversible activation continuum).

## When to use

When reasoning about whether CXCL9⁺ TAMs are a fixed lineage or a plastic state, and when interpreting pseudotime/RNA-velocity results over tumour myeloid cells.

## Known limitations

- Based on computational trajectory inference (PAGA/scVelo) without lineage tracing; snapshot population sizes can confound inferred flux direction.

## Open problems

- Distinguishing a true differentiation hierarchy from an activation-state continuum driven by local IFN-γ.

## Key papers

- [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]

## My understanding

A useful but tentative reframing; the developmental claim is weaker than the well-supported observation that CXCL9⁺ TAMs mark ICI-favourable tumours.
