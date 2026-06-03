---
title: "Dichotomous epigenetic versus transcriptional regulation of TR networks"
aliases:
  - two regimes of TR network regulation
  - epigenetic vs transcriptional TR regulation
tags:
  - epigenetics
  - transcription-factors
  - network-biology
  - macrophage
maturity: emerging
key_papers:
  - transcriptional-regulator-network-human-inflammatory-macrophages
first_introduced: "Schmidt, Krebs, Ulas et al. 2016 Cell Research"
date_updated: 2026-06-03
related_concepts:
  - open-chromatin-predefined-macrophage-activation-tr
  - tissue-specific-lineage-determining-factors-macrophage
---

## Definition
The observation that networks of transcriptional/epigenetic regulators fall into two regulatory regimes: (1) an **activation regime** (inflammatory macrophage activation network) where the chromatin landscape is uniformly permissive and gene expression is gated transcriptionally; and (2) an **identity/tissue regime** (tissue-related and tissue-macrophage TR networks) where expression is tightly integrated with chromatin state — expressed TRs carry accessible promoters/strong enhancers and non-expressed TRs carry repressive/absent marks.

## Intuition
Plastic, rapidly responding cell states keep their regulator loci "open" and decide output transcriptionally, trading epigenetic economy for speed. Stable identity programs instead hard-wire output into the epigenome, silencing irrelevant regulators with repressive chromatin.

## Formal notation
Activation regime: chromatin ≈ open ∀ TR; output ~ transcription. Identity regime: open(TR) ↔ expressed(TR) (dichotomous distribution).

## Variants
- Human macrophage activation network (regime 1)
- Human 5-tissue TR network and murine 7-tissue-macrophage TR network (regime 2)

## Comparison
Generalizes the [[open-chromatin-predefined-macrophage-activation-tr]] concept by placing it opposite the classical integrated model embodied by [[tissue-specific-lineage-determining-factors-macrophage]].

## When to use
When predicting whether a cell's regulator program is chromatin-gated or transcription-gated based on whether the program encodes identity versus inducible activation.

## Known limitations
Tissue comparisons rely on consortium (Roadmap) and murine (Amit et al.) data rather than matched human tissue macrophages.

## Open problems
- Whether the two regimes are discrete or a continuum
- What molecular machinery keeps activation-network loci constitutively open

## Key papers
- [[transcriptional-regulator-network-human-inflammatory-macrophages]]

## My understanding
The conceptual payoff of the paper: a single framework distinguishing "ready-to-fire" activation networks from "locked-in" identity networks by their mode of regulation.
