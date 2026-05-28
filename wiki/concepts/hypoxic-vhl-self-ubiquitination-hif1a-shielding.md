---
title: "Hypoxic VHL self-ubiquitination and the HIF1A shielding model"
aliases:
  - "VHL self-ubiquitination"
  - "HIF1A shielding of VHL"
  - "hypoxic VHL degradation"
tags:
  - hypoxia
  - VHL
  - ubiquitination
  - HIF1A
  - protein-stability
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism"
date_updated: 2026-05-28
related_concepts:
  - mitochondrial-vhl-noncanonical-hypoxia-function
---

## Definition

Under chronic hypoxia, the bulk cytosolic VHL pool is degraded via self-ubiquitination by its own VBC complex. The model: normally a hydroxylated HIF1A substrate occupies and "shields" the VHL complex from self-targeting; when hypoxia abolishes HIF1A hydroxylation (and HIF1A no longer engages VHL), the substrate-empty VHL complex self-ubiquitinates VHL at K171/K196, driving its degradation. This explains why VHL protein (but not other VBC components) selectively drops in hypoxia.

## Intuition

An idle E3 ligase eats itself. HIF1A is normally the "meal" that keeps the VHL complex busy and protected; remove the meal (hypoxia ⇒ no hydroxyl-HIF1A) and the ligase turns on itself. This degradation is the flip side of the mitochondrial-import story: VHL is either destroyed or rerouted.

## Formal notation

- Hypoxic VHL degradation: cycloheximide/MG132 sensitive; abolished by K171R/K196R.
- Shielding evidence: normoxic depletion of HIF1A (or adaptors ELOB/ELOC) markedly promotes VHL ubiquitination/degradation; EPAS1 (HIF2A) depletion has limited effect → HIF1A specifically shields VHL.
- Fusion-protein test: tethered VHL–HIF1A preferentially ubiquitinates the HIF1A part (blunted by HIF1A K/R or by swapping HIF1A→GFP).
- WSB1 (a reported VHL E3) acts mainly in normoxia → an alternative (self-ubiquitination) pathway dominates in hypoxia.
- K171/K196 overlap with TOM22-binding motifs → ubiquitination vs import are competing fates.

## Variants

- K171R/K196R VHL: degradation-resistant, increased mitochondrial VHL under hypoxia.
- RBX1 depletion enhances mitochondrial VHL only when combined with HIF1A loss.

## Comparison

- Versus canonical model: canonical VHL is stable and degrades HIF-α; here VHL itself is the degradation target when its substrate is gone.
- Versus WSB1-mediated VHL turnover: WSB1 dominates normoxic VHL turnover; self-ubiquitination dominates hypoxic turnover.

## When to use

Invoke when explaining selective loss of VHL protein under hypoxia, or the competition between VHL degradation and mitochondrial import.

## Known limitations

- Shielding is inferred from depletion/fusion experiments rather than direct structural occupancy measurement.
- K171/K196 are predicted ubiquitination sites.

## Open problems

- Quantitative partition between degraded vs imported VHL across O₂ levels and cell types.
- Whether other substrate-empty E3 ligases use analogous shielding.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

A neat mechanistic prerequisite for the main story: hypoxia first depletes cytosolic VHL (self-ubiquitination) and the surviving pool is the one captured by mitochondria — and because the ubiquitination sites overlap TOM22-binding motifs, the two fates are directly competitive. Links [[foundations/vhl-von-hippel-lindau]], [[foundations/hif1a]].
