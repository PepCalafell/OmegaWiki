---
title: "mMAC1 gene and DNA-methylation signatures enrich in MoMac-VERSE clusters IL4I1 Mac (#6), IL1B Mo (#15), ISG Mo (#4) — not TREM2/FOLR2 MACs"
slug: mmac1-signature-enriched-momac-verse-il4i1-il1b-isg
status: supported
confidence: 0.85
tags:
  - mMAC1
  - MoMac-VERSE
  - IL4I1
  - IL1B-Mo
  - ISG-Mo
  - signature-projection
  - in-vivo-correlate
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
  - cross-tissue-single-cell-landscape-human
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Signature projection onto MoMac-VERSE 13-tissue MNP atlas (Calafell 2024 Fig. 5A-C, fig. S5A). mMAC1 gene-expression and C2-methylation signatures preferentially enrich in clusters #15 (IL1B Mo), #6 (IL4I1 Mac), #4 (ISG Mo). TREM2 Mac (#3) and FOLR2 Mac (#2) are negative controls, not enriched."
conditions: "Mulder 2021 MoMac-VERSE atlas; signature scoring per cluster; UMAP overlays."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The in vitro mMAC1 transcriptomic and DNA-methylation signatures find their in vivo correlates in three MoMac-VERSE clusters from the Mulder 2021 pan-tissue human MNP atlas: cluster #6 (IL4I1 Mac), #15 (IL1B Mo), #4 (ISG Mo). TREM2 Mac (#3) and FOLR2 Mac (#2) are negative controls and are not enriched.

## Evidence summary

- Signature gene expression dot plot + UMAP overlay (Calafell 2024 Fig. 5A-C, fig. S5A-C).
- Cell coexpression analysis: cells coexpressing combinations of mMAC1 mRNA / methylation / TF-binding signatures concentrate in IL4I1 / IL1B Mo / ISG Mo clusters (fig. S5C).

## Conditions and scope

- MoMac-VERSE provides 13-tissue MNP scRNA-seq atlas (Mulder 2021).
- Signature projection by gene expression score; methylation signature projected via cluster-specific gene sets.

## Counter-evidence

- Some IL4I1 Mac context-dependent immunosuppression (e.g., tryptophan / AHR / PD-L1) — the mMAC1 ↔ IL4I1 mapping is signature-level not function-level.

## Linked ideas

- Concept: [[concepts/mmac1-hypoxic-inflammatory-macrophage]], [[concepts/il4i1-tumor-associated-macrophage]], [[concepts/momac-verse-mnp-verse-atlas]].
- Foundation for in vivo validation of mMAC1.

## Open questions

- Functional validation (cytokine secretion, T-cell coculture) of sorted IL4I1 MACs in matched protocols.
- Whether IL1B Mo, ISG Mo, IL4I1 Mac represent maturation states of the same lineage or distinct populations.
