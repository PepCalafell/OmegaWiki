---
title: "Druggable genome / undruggable proteome"
aliases: [druggable genome, undruggable proteome, drug-target space]
tags: [drug-discovery, pharmacology, genomics]
maturity: active
key_papers:
  - wealth-discovery-built-human-genome-project
first_introduced: ""
date_updated: 2026-06-10
related_concepts: [network-medicine, superstar-gene-attention-skew]
---

## Definition

The druggable genome is the subset of the ~20,000 human proteins that can be modulated by drug-like molecules. As of the source analysis, only ~10% (2,149 proteins) are targeted by approved drugs; experimental drugs raise this to 3,119. The remaining ~90% of the proteome is untouched by pharmacology.

## Intuition

The HGP revealed ~20,000 proteins as *potential* drug targets, but actual targeting is highly uneven and sparse. The skew may reflect genuine biology (some proteins matter more, some are undruggable) or risk-averse research/funding behaviour leaving many viable targets unexplored.

## Formal notation

Not applicable — a coverage statistic over the proteome.

## Variants

- Approved-drug target set (2,149) vs. experimental-drug target set (3,119).
- "Network drug" targeting: most successful drugs hit proteins 1–2 interactions from the disease gene — see [[network-medicine]].

## Comparison

Direct disease-gene targeting (minority of successful drugs) versus network-neighbour targeting (majority). The COVID-19 repurposing example: only ~1% of promising candidates targeted a viral protein.

## When to use

When scoping target space, assessing repurposing opportunities, or reasoning about why the proteome is under-exploited pharmacologically.

## Known limitations

- "Druggable" is not fixed — new modalities (PROTACs, RNA therapeutics) keep expanding it.
- Coverage statistics depend on the drug-target database used (DrugBank-derived here).

## Open problems

- Whether the untargeted 90% holds many viable targets if researchers, funders, and publishers were less risk-averse.

## Key papers

- [[wealth-discovery-built-human-genome-project]] — quantifies proteome drug-target coverage and the ADRA1A attention-skew example.

## My understanding

Reinforces that target-space coverage, like gene-study coverage, follows a heavy-tailed attention pattern; relevant when prioritizing tractable targets in immune/hypoxia contexts.
