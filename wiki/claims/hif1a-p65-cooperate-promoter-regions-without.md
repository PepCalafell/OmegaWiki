---
title: "HIF1α and p65 cooperatively bind chromatin at cobound peaks without obligate physical interaction (Pearson r = 0.13)"
slug: hif1a-p65-cooperate-promoter-regions-without
status: supported
confidence: 0.8
tags:
  - HIF1A
  - p65
  - RELA
  - ChIP-seq
  - chromatin-cooperation
  - non-physical-interaction
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "ChIP-seq for HIF1α and p65 in all four conditions, with peak co-occurrence analysis in mMAC1 (Calafell 2024 Fig. 4A-F). HIF1α and p65 cobound peaks (~15% of HIF1α H2 cluster) show binding intensity correlation Pearson r = 0.13, P = 2.5×10⁻⁴ — statistically significant but very weak linear relationship, ruling out stoichiometric physical complex."
conditions: "ChIP-seq cobinding analysis; cobound peaks defined as HIF1α H2 ∩ p65 P1."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

HIF1α and p65 ChIP-seq peaks in mMAC1 overlap at a meaningful subset of regions (~15% of HIF1α H2 cluster), and their binding intensities on these cobound peaks are positively correlated. However, the Pearson r = 0.13 (P = 2.5×10⁻⁴) indicates a very weak linear relationship inconsistent with a stoichiometric physical HIF1α-p65 complex. The cooperation is "non-physical" — likely mediated by shared cofactors, sequential recruitment, or cooperative chromatin opening.

## Evidence summary

- HIF1α + p65 ChIP-seq, all 4 MAC conditions, consensus peaks (Calafell 2024 Fig. 4A).
- Cobound peak set defined by overlap of HIF1α and p65 significant peaks in mMAC1 (Fig. 4B).
- Motif enrichment in HIF1α-centered vs p65-centered analyses of cobound peaks (Fig. 4C-D).
- Cobound peak binding intensity correlation: r = 0.13, P = 2.5×10⁻⁴ (Fig. 4F).

## Conditions and scope

- mMAC1 cobound peaks specifically.
- ChIP-seq cannot distinguish direct vs indirect chromatin binding.

## Counter-evidence

- Statistical significance (P = 2.5×10⁻⁴) shows the correlation is real but weak.
- Alternative interpretation: stoichiometric binding may occur at a subset of cobound peaks not captured in the bulk correlation.

## Linked ideas

- Concept: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]].
- Direct mechanistic follow-up: proximity ligation assay (PLA), BioID, CUT&Tag for chromatin readers, co-IP under non-stringent conditions.

## Open questions

- Identity of bridging cofactors (p300/CBP, BRD4, mediator complex?).
- Whether HIF1α priming is sufficient to recruit p65, or whether NF-κB-target sequences are also required.
- Cell-cycle / activation-state dependence of the cooperation.
