---
title: "Neo2 — de novo designed IL-2/IL-15 mimic"
slug: neo2-designed-il-mimic
domain: "protein design / immunology"
status: mainstream
aliases:
  - "Neo-2/15"
  - "Neoleukin-2/15"
  - "Neo2"
first_introduced: "Silva et al. 2019, Nature (De novo design of potent and selective mimics of IL-2 and IL-15)"
date_updated: 2026-06-10
source_url: "https://doi.org/10.1038/s41586-018-0830-7"
---

## Definition

Neo2 (Neo-2/15) is a hyperstable de novo designed protein that mimics interleukin-2 (IL-2) and interleukin-15 by binding the IL-2Rβ and common gamma chain (γc, IL2RG) subunits of the receptor, but is engineered to have no binding to IL-2Rα (CD25) and no structural homology to natural IL-2. It reconstitutes IL-2Rβγc signalling — JAK1/3 → STAT5 — to drive lymphocyte proliferation and effector function while avoiding IL-2Rα-mediated Treg bias and toxicity.

## Intuition

Natural IL-2 has poor stability, short half-life, and α-chain-driven toxicity. Neo2 reproduces only the βγc-engaging "business end" of IL-2 on a small, hyperstable de novo scaffold, decoupling activation of effector CD8/NK cells from IL-2Rα biology. It is the binding module repurposed in this paper's switchable cytokine ASNeo2.

## Formal notation

Engages IL-2Rβ + γc → heterodimerization → JAK1/JAK3 trans-phosphorylation → pSTAT5. No CD25 (IL-2Rα) contact.

## Key variants

- Neo-2/15 (original βγc agonist)
- ASNeo2 (this paper) — Neo2 rigidly fused to a designed hinge switch so that effector binding sterically clashes with γc and triggers facilitated dissociation of the active complex.

## Known limitations

- As a foreign designed protein, potential immunogenicity in vivo.
- Native Neo2 has no intrinsic off-switch — once bound it signals until the complex internalizes/degrades (the limitation this paper addresses).

## Open problems

- Tuning agonist strength and receptor selectivity for therapeutic windows.
- Controlling temporal dynamics of signalling — addressed here by fusing Neo2 to a facilitated-dissociation switch.

## Relevance to active research

Neo2 is the receptor-engaging module of ASNeo2, the rapidly switchable IL-2 mimic used in [[design-facilitated-dissociation-enables-timing-cytokine]] to terminate IL-2Rβγc signalling within seconds. Connected to [[il-2-cytokine]] and [[stat5-tf]] biology.
