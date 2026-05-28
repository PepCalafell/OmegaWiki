---
title: "Secondary cytokine response cascade (indirect signaling)"
aliases:
  - secondary cytokine response
  - indirect cytokine cascade
  - higher-order cytokine signaling
maturity: emerging
tags:
  - cytokines
  - signaling-cascade
  - indirect-response
  - cell-cell-communication
key_papers:
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2025"
date_updated: 2026-05-28
related_concepts:
  - cytokine-receptor-expression-insufficient-cytokine-response
  - cytokine-mediated-immune-cell-cell-interactome
  - il-32-beta-myeloid-neutrophil-inflammatory
---

## Definition

The phenomenon whereby a measured cytokine response in a cell type is not direct but mediated by a secondary cytokine that the primary stimulus induced in another cell. Over a 24 h stimulation, PBMCs both respond to the primary cytokine and secrete higher-order cytokines, so the endpoint transcriptome reflects the cumulative cascade. The Dictionary identifies secondary mediators by requiring (1) the secondary cytokine is upregulated in cells expressing the primary receptor and (2) the indirect responder's profile resembles its direct response to the secondary cytokine (Pearson r > 0.5).

## Intuition

If monocytes "respond" to IL-12/IL-2/IL-15 despite lacking the primary receptors, something is relaying the signal. The Dictionary shows that IFN-γ released by NK CD56hi cells is the relay: the monocyte response to IL-12/IL-2/IL-15 matches its response to direct IFN-γ. This is why response without receptor expression is common and why naive ligand–receptor inference misattributes signals.

## Variants

- IL-2/IL-12/IL-15 → NK-derived IFN-γ → monocytes (canonical example)
- Inflammatory cytokines → broad TNF-α / IFN-γ secondary induction

## Comparison

Mechanistic complement to [[cytokine-receptor-expression-insufficient-cytokine-response]] (receptor expression neither necessary nor sufficient): secondary cascades explain a major class of receptor-independent "responses."

## When to use

When attributing a cytokine response as direct vs indirect; when cell-cell communication or perturbation-response inference must avoid crediting the primary cytokine for a relayed effect.

## Known limitations

- Inference relies on correlation thresholds and timepoint choice
- Cannot fully exclude unknown receptors or rapid undetected intermediates
- 24 h endpoint conflates direct and cascade contributions

## Open problems

- Temporal resolution of primary vs secondary waves
- Quantifying cascade depth (tertiary and higher orders)
- Disentangling cascades in dense tissue / tumor niches

## Key papers

- [[papers/single-cell-cytokine-dictionary-human-peripheral]]

## My understanding

A crucial interpretive caveat for any cytokine-perturbation or communication analysis: a 24 h readout is a cascade, not a clean direct response. The NK→IFN-γ→monocyte example is the clearest case and a template for cascade detection.
