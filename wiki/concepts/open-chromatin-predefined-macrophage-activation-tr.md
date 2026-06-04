---
title: "Open-chromatin-predefined macrophage activation TR network"
aliases:
  - open-chromatin TR network
  - pre-defined transcriptional regulator network
  - constitutively accessible TR promoters
tags:
  - macrophage
  - epigenetics
  - transcription-factors
  - network-biology
maturity: emerging
key_papers:
  - transcriptional-regulator-network-human-inflammatory-macrophages
first_introduced: "Schmidt, Krebs, Ulas et al. 2016 Cell Research"
date_updated: 2026-06-03
related_concepts:
  - dichotomous-epigenetic-versus-transcriptional-regulation-tr
  - macrophage-activation-core-regulatory-hubs
  - spectrum-model-macrophage-activation
  - epigenetic-potential-macrophage
---

## Definition
The network of transcriptional and epigenetic regulators (TRs) that governs human inflammatory macrophage activation whose member loci share constitutively **accessible (permissive) promoters across all activation conditions**, independent of the activating signal. Because the chromatin state of these promoters is uniform and "pre-set," differences in TR expression between stimuli are driven by a second, transcriptional layer of regulation rather than by changes in the epigenetic landscape.

## Intuition
For most genes, accessible chromatin predicts expression and inaccessible chromatin predicts silencing (the "general model"). The macrophage activation TR network is an exception to the rule: its promoters are open regardless of whether the encoded TR is expressed in a given activation state. Open chromatin is therefore a *prerequisite* — a loaded launchpad — that allows rapid, signal-specific deployment of master TRs without first remodeling chromatin.

## Formal notation
For TR loci in the activation network: P(accessible promoter | activation state) ≈ constant (> 92%), while expression(TR | activation state) varies by stimulus. Contrast with tissue networks where P(accessible) ≈ P(expressed).

## Variants
- Activation TR network (open-chromatin-predefined) — this concept
- Tissue/tissue-macrophage TR networks (epigenetically + transcriptionally integrated) — the contrasting regime

## Comparison
Distinct from the [[spectrum-model-macrophage-activation]] (which is about transcriptome diversity) and from [[macrophage-activation-core-regulatory-hubs]] (the connectivity hubs); this concept adds the epigenetic dimension showing why network TRs need no chromatin remodeling to switch states.

## When to use
Invoke when reasoning about why macrophage activation is fast and plastic, or when interpreting open-chromatin/ATAC/ChIP data over regulator loci that does not track expression.

## Known limitations
Defined from in-vitro GM-CSF-differentiated monocyte-derived macrophages under four stimuli; tissue-resident macrophage validation in human remains incomplete.

## Open problems
- Whether M-CSF differentiation yields a comparable open-chromatin TR network
- Whether the predefined-open-chromatin regime generalizes to other plastic cell types

## Key papers
- [[transcriptional-regulator-network-human-inflammatory-macrophages]]

## My understanding
This is the headline conceptual contribution: it decouples chromatin accessibility from expression specifically for the regulator network of an activatable cell, reframing inflammatory activation as transcriptionally (not epigenetically) gated.
