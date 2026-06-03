---
title: "Core regulatory hubs of macrophage activation"
aliases:
  - macrophage activation hub genes
  - common denominators of macrophage activation
  - activation-independent macrophage regulators
tags:
  - macrophage
  - transcription-factors
  - network-biology
maturity: emerging
key_papers:
  - transcriptome-based-network-analysis-reveals-spectrum
  - transcriptional-regulator-network-human-inflammatory-macrophages
first_introduced: "Xue et al. 2014 Immunity (ARACNe/TINGe RNE)"
date_updated: 2026-06-03
related_concepts:
  - spectrum-model-macrophage-activation
---

## Definition
The set of highly interconnected hub genes — especially transcription factors — that participate in macrophage activation across all stimulation conditions, identified by reverse network engineering of a 299-transcriptome resource. These are the "common denominators" of activation, complementary to the stimulus-specific programs of the spectrum model.

## Intuition
While the spectrum model captures stimulus-specific differences, an all-versus-all mutual-information network reveals genes that sit at the center of activation regardless of stimulus. The most highly expressed hub TFs are candidate master regulators of macrophage activation in general.

## Formal notation
- 9,498 genes → ARACNe → 66,744 interactions, average degree 14.7
- Top 10% hubs = 869 genes participating in 30,431 interactions; 27 are TFs
- Top 5 most highly expressed hub TFs: JUNB, NFKB1, HIVEP1, CREB1, HBP1
- Gene-prioritization (ToppGene/Endeavour) adds STAT3, HMGA1, NFE2, ZNF148, etc.

## Variants
- ARACNe-derived vs TINGe-derived hub rankings (highly concordant)
- Most-interconnected genes (FABP5, TNFAIP6) vs most-highly-expressed TF hubs

## Comparison
vs stimulus-specific TF hubs (STAT1 for IFN-γ, STAT6 for IL-4, STAT4 for TPP): the core regulatory hubs are activation-independent and shared across conditions.

## When to use
- Identifying candidate pan-activation master regulators of human macrophages
- Prioritising TFs for functional follow-up beyond the canonical STATs

## Known limitations
- MI edges are associative, not causal.
- "Most highly expressed = most relevant" is a heuristic ranking.
- HIVEP1 and several hubs have no established macrophage role.

## Open problems
- Functional validation of HIVEP1 and other under-studied hubs in macrophage activation.
- Causal direction within the inferred network.

## Key papers
- [[papers/transcriptome-based-network-analysis-reveals-spectrum]] — Xue et al. 2014: ARACNe/TINGe reverse engineering identifying JUNB, NFKB1, CREB1 and others as core hubs.

## My understanding
The complement to the spectrum model: alongside stimulus-specific diversity there is a shared activation backbone (AP-1 / NF-κB / CREB1 family). Useful when arguing that macrophage activation has both a universal core and a combinatorial periphery.
