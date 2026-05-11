---
title: "HIF1α binds cobound peaks earlier than p65 — HIF1α priming hypothesis on shared enhancers"
slug: hif1a-binds-earlier-than-p65-cobound-peaks
status: weakly_supported
confidence: 0.7
tags:
  - HIF1A
  - p65
  - ChIP-seq
  - priming
  - temporal-sequence
  - chromatin-cooperation
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "Cobound-peak binding intensity plotted across conditions (Calafell 2024 Fig. 4E). HIF1α binding already high in iMAC1 (resting hypoxic), whereas p65 binding mainly increases after activation (mMAC1). Authors infer HIF1α primes p65 recruitment on shared regions."
conditions: "Cobound peaks H2 ∩ P1; cross-condition binding intensity comparison."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

On HIF1α-p65 cobound enhancer/promoter regions, HIF1α binding is established earlier in the activation trajectory (already elevated in unstimulated hypoxic MACs, iMAC1) than p65 binding, which only peaks in mMAC1 after LPS activation. The authors interpret this as HIF1α priming the chromatin for subsequent p65 recruitment.

## Evidence summary

- Cross-condition binding-intensity profile on cobound peaks (Calafell 2024 Fig. 4E).
- Example loci in fig. S4C.
- Statistically not formally tested for "binding-order" inference; conclusion is descriptive.

## Conditions and scope

- Inferred from steady-state ChIP-seq at 4 conditions, not time-resolved ChIP-seq.

## Counter-evidence

- A time-resolved ChIP-seq series would be required to definitively establish the binding sequence. The 4-state snapshot is consistent with priming but does not prove it.

## Linked ideas

- HIF1α as a pioneer-like factor on cobound regions.
- Sequence-of-events for paired methylome-transcriptome analyses (one of the authors' suggested future directions).

## Open questions

- Direct time-resolved HIF1α and p65 ChIP-seq at 0, 0.5, 2, 6, 24, 48h post LPS in hypoxia.
- Whether HIF1α loss (PX-478 or HIF1A KO) reduces subsequent p65 binding at cobound peaks.
