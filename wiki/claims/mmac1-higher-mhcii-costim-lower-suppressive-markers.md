---
title: "mMAC1 displays higher MHC-II and costimulatory marker expression and lower immunoregulatory marker expression than mMAC21"
slug: mmac1-higher-mhcii-costim-lower-suppressive-markers
status: supported
confidence: 0.9
tags:
  - macrophage
  - hypoxia
  - HLA-DR
  - CD80
  - CD86
  - CD14
  - CD163
  - CD206
  - antigen-presentation
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Flow cytometry MFI quantification (Calafell 2024 Fig. 1C, n=4). mMAC1 shows higher HLA-DR, CD86, CD80 and lower CD14, CD206, CD163 vs mMAC21 (all P<0.05; multiple P<0.01 or <0.001)."
conditions: "Human PB-MO-derived M-CSF MACs, 1% vs 21% O2, 48h LPS activation; flow cytometry; n=4."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Macrophages activated in hypoxia (mMAC1) display a surface phenotype shift toward antigen-presenting and away from immunoregulatory: higher HLA-DR, CD80, CD86 and lower CD14, CD163, CD206 compared to their normoxic counterparts (mMAC21).

## Evidence summary

- Flow cytometry on M-CSF MACs after differentiation/activation in 21% vs 1% O₂ (Calafell 2024 Fig. 1C).
- All six markers significantly different by Student's t-test; multiple at P < 0.01-0.001.
- The shift is consistent with the conventional M1-like / proinflammatory polarization framework (although the authors caution against the M1/M2 binary).

## Conditions and scope

- M-CSF MACs (not GM-CSF, not TRMs).
- Static 1% O₂ + LPS 48h.

## Counter-evidence

- TREM2+ tissue MACs (in vivo) also express HLA-DR but are immunosuppressive — surface phenotype alone is insufficient to predict function. mMAC1 is distinguished by also lacking CD163/CD206.

## Linked ideas

- Surface flow panel for sorting mMAC1-like cells from primary tumors.

## Open questions

- Single-cell co-expression: are all six markers shifted on the same cells or in distinct subpopulations?
- Stability after re-oxygenation.
