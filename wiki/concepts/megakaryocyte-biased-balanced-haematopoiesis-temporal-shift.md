---
title: "Temporal shift from megakaryocyte-biased to balanced haematopoiesis"
aliases: []
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Zheng et al. 2025 (pseudodynamics+), building on Upadhaya 2018 and Kucinski 2024"
date_updated: 2026-06-03
related_concepts:
  - vwf-hsc-fast-megakaryocyte-differentiation-pathway
  - time-dependent-flux-parameters-long-timecourse
  - continuous-density-transport
---

## Definition

The observation, inferred from time-resolved population-aware flux modelling of in vivo mouse haematopoiesis, that the system progresses over months from an early, fast, megakaryocyte-biased output to a slower, balanced, homeostatic lineage output. Early timepoints show elevated megakaryocyte/erythroid/neutrophil progenitor proliferation and a megakaryocyte fate bias; relative differentiation rates and lineage output stabilize after roughly Day 76.

## Intuition

When stable labelling is induced, a small pool of fast, megakaryocyte-primed (vWF+) HSCs reaches downstream stages first and dominates early output; as slower, balanced HSCs catch up, the landscape settles into steady-state multi-lineage production. The system's apparent bias is therefore a transient of differential transit time, not a permanent skew.

## Variants

- Seen at the HSC level (vWF+ MK-biased HSC enrichment early) and the progenitor level (MEP transient Mk bias Day 12–27 → balanced Day 49+).

## Comparison

- Consistent with Upadhaya et al. 2018 (MK progenitors outpace others in week 1 post-tamoxifen) and Kucinski et al. 2024 (early MEP/MkP expansion).
- Confounded by possible tamoxifen perturbation of JAK-STAT signalling.

## When to use

- When interpreting label-propagation / persistent-labelling haematopoiesis time courses and their early-phase MK skew.

## Known limitations

- Inferred from a computational flux model on one dataset; early variation may partly reflect tamoxifen artefacts rather than intrinsic HSC heterogeneity.

## Open problems

- Disentangling intrinsic HSC kinetic heterogeneity from induction/perturbation effects experimentally.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — quantifies the shift via time-dependent rates and continuous density transport.

## My understanding

The headline biological finding: a "previously unrecognised shift" that is only visible once flux rates are allowed to change over time — a good demonstration of why the methodological advance matters.
