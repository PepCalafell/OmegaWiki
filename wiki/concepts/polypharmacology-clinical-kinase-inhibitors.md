---
title: "Polypharmacology of clinical kinase inhibitors"
aliases:
  - "CKI polypharmacology"
  - "kinase inhibitor off-target effects"
tags:
  - kinase-inhibitors
  - polypharmacology
  - off-target
  - drug-selectivity
  - pharmacology
maturity: active
key_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
first_introduced: "Klaeger et al. 2017 *Science*; revisited by Gualdrini et al. 2024"
date_updated: 2026-06-03
related_concepts:
  - epigenome-based-functional-profiling-kinase-inhibitors
  - discordance-between-vitro-kinase-inhibitor-selectivity
---

## Definition

The property that most clinical kinase inhibitors (CKIs) inhibit multiple kinases beyond their intended target(s). Because the ATP-binding pocket is conserved across the kinome, ATP-competitive CKIs show broad cross-activity; the resulting combination of on- and off-target effects shapes both therapeutic efficacy and toxicity, and is largely responsible for the cellular effect spectrum of each drug.

## Intuition

A "kinase inhibitor" is rarely a single-target drug. Its real-world effect is the sum of everything it binds at the concentration used. Two drugs nominally targeting the same kinase can behave completely differently in cells because their off-target portfolios differ.

## Formal notation

- Clinical CKIs show selectivity profiles comparable to early-preclinical molecules (Klaeger et al. 2017); low selectivity does not preclude approval.
- CKIs can also engage non-kinase ATP-binding enzymes (NQO2, TOP2B, ACOX3).

## Variants

- Designated/clinical target annotation vs kinobeads-measured target set vs in-cell functional target set — three often-discordant views.

## Comparison

Against the idealized "magic bullet" single-target model: polypharmacology means cellular phenotype must be measured, not inferred from the intended target.

## When to use

Invoke when interpreting why same-target inhibitors diverge, or when predicting side effects/repurposing opportunities from a drug's broader target portfolio.

## Known limitations

- Full off-target portfolios are unknown (kinome coverage of assays is partial).
- On- vs off-target attribution requires orthogonal genetic/functional experiments.

## Open problems

- Predicting which off-targets drive efficacy vs toxicity for a given indication.
- Systematic functional (not just binding) deconvolution of polypharmacology.

## Key papers

- [[papers/integrative-epigenome-based-strategy-unbiased-functional]] — shows off-target effects dominate the measured cellular (epigenomic) response, even at sub-inhibitory concentrations of the intended target.

## My understanding

The central pharmacological premise the paper leverages: polypharmacology is not noise to be removed but information that a high-content functional readout can exploit to map a drug's true cellular action.
