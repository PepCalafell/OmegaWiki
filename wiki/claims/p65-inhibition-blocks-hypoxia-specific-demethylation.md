---
title: "BAY11-7082 (p65 inhibitor) blocks hypoxia-specific C2 demethylation; PX-478 (HIF1α inhibitor) does not"
slug: p65-inhibition-blocks-hypoxia-specific-demethylation
status: supported
confidence: 0.9
tags:
  - BAY11-7082
  - PX-478
  - p65-inhibitor
  - HIF1A-inhibitor
  - DNA-demethylation
  - cluster-C2
  - pharmacological
domain: "pharmacology / epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Pretreatment of MAC21/MAC1 with BAY11-7082 (p65 inhibitor) or PX-478 (HIF1α inhibitor) for 3h before LPS, then 48h activation; EPIC methylation readout on C2 CpGs (Calafell 2024 Fig. 4K). BAY11-7082 alone restores C2 methylation to mMAC21 levels; PX-478 alone does not. Confirms p65 as the necessary driver of hypoxia-specific C2 demethylation."
conditions: "3h pretreatment, BAY11-7082 ~5 μM, PX-478 ~30 μM, M-CSF MACs."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

Pharmacological inhibition of p65 (BAY11-7082) is sufficient to block hypoxia-specific demethylation of cluster C2 CpGs in mMAC1, restoring methylation levels comparable to mMAC21. In contrast, HIF1α inhibition (PX-478) alone fails to block C2 demethylation. p65 is necessary and the primary driver of the C2 demethylation; HIF1α is not.

## Evidence summary

- Pretreatment with BAY11-7082 or PX-478 for 3h before LPS, then 48h activation (Calafell 2024 Fig. 4K).
- EPIC methylation array readout on C2 cluster.
- BAY11-7082 → C2 methylation rises to mMAC21-like levels; PX-478 → C2 methylation remains low (hypoxic-like).

## Conditions and scope

- Pharmacological doses chosen by authors; off-target effects of BAY11-7082 / PX-478 not fully controlled.
- Single-agent treatment; combination (BAY11 + PX-478) not tested separately for synergy in figure.

## Counter-evidence

- BAY11-7082 has documented off-target effects (cysteine modification, IκBα ubiquitination block). A clean genetic RELA KO would strengthen the conclusion.
- PX-478 has documented HIF1α-independent effects at high doses.

## Linked ideas

- Pharmacological anchor for p65-as-driver hypothesis.
- Suggests p65 inhibitors may suppress mMAC1 emergence in vivo — possibly counter-productive for ICI response.

## Open questions

- Genetic perturbation (RELA shRNA or KO) for orthogonal validation.
- TET2 recruitment by p65 (direct or indirect) at C2.
