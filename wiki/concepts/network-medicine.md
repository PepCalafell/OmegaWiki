---
title: "Network medicine"
aliases: [network pharmacology, network drugs]
tags: [network-science, systems-biology, drug-discovery, genomics]
maturity: active
key_papers:
  - wealth-discovery-built-human-genome-project
first_introduced: "2007"
date_updated: 2026-06-10
related_concepts: [druggable-genome, superstar-gene-attention-skew]
---

## Definition

Network medicine treats disease and therapy through the lens of the cell's interaction network — protein–protein, protein–DNA, and regulatory interactions — rather than through single genes in isolation. A key empirical claim is that most successful drugs do not directly target a disease gene; they target proteins one or two interactions away, modulating the consequences of faulty components ("network drugs").

## Intuition

Biological function arises from the *interactions* between components, not just the parts list. So perturbing the network neighbourhood of a disease gene is often more therapeutically effective (and more druggable) than hitting the disease gene itself. This complements the Mendelian single-gene perspective.

## Formal notation

Disease modules and drug targets are analyzed on an interactome graph; therapeutic effect is modeled as propagation/perturbation across edges, with "network proximity" between drug-target sets and disease modules used as a predictor.

## Variants

- Disease-module detection on the interactome.
- Network-proximity-based drug repurposing (e.g., COVID-19 repurposing screens where ~99% of promising candidates modulated human, not viral, proteins).

## Comparison

Versus the single-gene/Mendelian view: network medicine predicts effective targets that single-gene reasoning would miss, and explains why so few disease genes are themselves the direct drug target.

## When to use

When reasoning about drug repurposing, polypharmacology, or why a target distant from the causal gene works.

## Known limitations

- Interactome maps are incomplete and noisy.
- Network proximity is correlative; causal validation still required.

## Open problems

- Completing and contextualizing the human interactome (>300,000 regulatory interactions charted so far, far from complete).

## Key papers

- [[wealth-discovery-built-human-genome-project]] — argues the HGP's lasting value is the network era of genomics it enabled, and that most drugs act on network neighbours of disease genes.

## My understanding

The Barabási framing reframes the HGP from "parts catalogue" to "scaffold for an interaction map". Relevant to [[druggable-genome]] (why 90% of the proteome is untargeted) and to thesis-adjacent systems-immunology network reasoning.
