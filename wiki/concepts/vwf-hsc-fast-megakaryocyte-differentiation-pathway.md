---
title: "vWF+ HSC fast megakaryocyte differentiation pathway"
aliases:
  - vWF+ HSC
  - megakaryocyte-biased HSC
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Sanjuan-Pla et al. 2013; Carrelha et al. 2018/2024; revisited dynamically in Zheng et al. 2025"
date_updated: 2026-06-03
related_concepts:
  - megakaryocyte-biased-balanced-haematopoiesis-temporal-shift
---

## Definition

A non-canonical haematopoietic route in which a subgroup of von-Willebrand-factor-expressing (vWF+) haematopoietic stem cells is specialized to rapidly produce megakaryocytes (and platelets), bypassing much of the conventional stepwise progenitor hierarchy. These platelet-primed HSCs sit atop a fast megakaryocyte pathway and are molecularly distinguishable from multi-lineage-balanced HSCs.

## Intuition

Not all HSCs are equivalent: a platelet-biased subset can shortcut to the megakaryocyte fate, especially under stress or in early post-induction windows, contributing disproportionately to early megakaryocyte output before balanced HSCs contribute.

## Formal notation

Marked by Vwf expression (see [[foundations/von-willebrand-factor-vwf]]); enriched for an alternative-MK / vWF+ P-HSC transcriptional signature relative to standard multi-lineage HSCs.

## Variants

- Steady-state platelet-biased HSCs vs stress-induced rapid megakaryopoiesis.

## Comparison

- Distinct from the canonical HSC → MPP → MEP → megakaryocyte hierarchy; complements [[concepts/hspc-differentiation-multiomics]].

## When to use

- When interpreting early megakaryocyte-biased output or platelet-priming signatures in HSC scRNA-seq.

## Known limitations

- vWF marks a graded bias, not an absolute committed fate.
- Evidence here is signature-based and computational, not clonal proof of the fast pathway in this dataset.

## Open problems

- Whether vWF+ bias is a stable subtype or a reversible primed state.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — finds early (Day 3–12) enrichment of vWF+ MK-biased HSCs scoring high in the alternative-MK signature (max p=0.00735).

## My understanding

The biological mechanism the paper invokes to explain its inferred early MK bias — a known platelet-primed HSC pathway, here observed through a time-resolved population-dynamics lens.
