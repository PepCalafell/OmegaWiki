---
title: "TGFβ1 and IL-1β are inferred shared upstream ligands activating both eFibro_CTHRC1 and Macro_SLPI"
slug: tgfb1-il1b-shared-upstream-cthrc1-slpi-ecotype
status: supported
confidence: 0.7
tags:
  - tgfb1
  - il1b
  - ecotype
  - cthrc1
  - slpi
  - nichenet
  - profibrotic
  - smad
  - nfkb
domain: cell signaling / tumor stroma
source_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
evidence:
  - source: spatiotemporal-analyses-pan-cancer-single-cell
    type: supports
    strength: medium
    detail: NicheNet ligand-target inference ranks TGFβ1 and IL-1β as top upstream ligands for both eFibro_CTHRC1 and Macro_SLPI (Fig. 5e); concordant with known SMAD and NF-κB / STAT activation of CAFs and fibrotic macrophages in lung fibrosis and COVID-19.
conditions: "Computational inference (NicheNet) on pan-cancer scRNA-seq; not perturbation-validated in this paper."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

NicheNet identifies TGFβ1 and IL-1β as the top shared upstream ligands activating both the eFibro_CTHRC1 ECM-remodeling CAF phenotype and the Macro_SLPI profibrotic TAM phenotype, providing a single convergent signaling axis (SMAD + NF-κB / STAT) for the profibrotic ecotype.

## Conditions and scope

Direct quote: "NicheNet analyses... indicated a tight connection between the activity of TGFβ1 and interleukin-1β (IL-1β) ligands and the eFibro_CTHRC1 phenotype... TGFβ1 and IL-1β could also stimulate the Macro_SLPI phenotype" (Han 2025, p.11, Fig. 5e).

## Linked ideas

- Anti-TGFβ + anti-IL-1β combination as anti-ecotype therapeutic strategy.
- Temporal continuity from early IL1B-IL1R1 epithelial niche to late TGFβ1/IL-1β profibrotic ecotype.
