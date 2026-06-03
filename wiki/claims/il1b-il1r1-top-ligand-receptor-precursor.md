---
title: "IL1B-IL1R1 is among the top ligand-receptor pairs enriched between myeloid and epithelial cells in lung precursor lesions"
slug: il1b-il1r1-top-ligand-receptor-precursor
status: supported
confidence: 0.85
tags:
  - luad
  - precursor
  - cell-cell-interaction
  - il1b
  - il1r1
domain: lung cancer / cell signaling
source_papers:
  - multimodal-spatial-omics-reveal-co-evolution
evidence:
  - source: multimodal-spatial-omics-reveal-co-evolution
    type: supports
    strength: strong
    detail: Ligand-receptor inference on inflammatory response genes upregulated in KACs identifies IL1B-IL1R1 in the top 8 myeloid-epithelial LR pairs; uniquely highly expressed in KAC and precursor cells, absent in normal AT1/AT2.
  - source: mapping-inflammatory-origins-lung-cancer
    type: supports
    strength: weak
    detail: "Cancer Cell Preview: high IL1R1 in RPII/KACs and high IL1B in adjacent macrophages implicate IL-1β–IL1R1 coupling as a core driver of alveolar epithelial cell tumorigenesis."
conditions: "Human Visium ST + snRNA-seq. Effect strongest in KRAS-mutant precursor cases (100% LR enrichment)."
date_proposed: 2026-05-26
date_updated: 2026-06-03
---

## Statement

IL1B (macrophage-derived) — IL1R1 (KAC/precursor-derived) signaling is among the top spatially enriched myeloid-epithelial ligand-receptor pairs in precursor lesions, uniquely combining (i) precursor-cell-specific receptor expression and (ii) precursor-stage-restricted interaction frequency.

## Conditions and scope

Holds in CellChat-style LR inference on ST + snRNA-seq. In KRAS-mutant precursors, IL1B-IL1R1 enrichment reaches 100% of cases; in KRAS-WT precursors, no such precursor-specific enrichment is seen.

## Open questions

- Does the IL1B-IL1R1 LR signal predict progression risk independently of KRAS status?
- Could spatial LR inference on screening biopsies serve as an interception biomarker?
