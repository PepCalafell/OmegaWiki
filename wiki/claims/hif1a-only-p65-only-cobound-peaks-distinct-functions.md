---
title: "HIF1α-only, p65-only, and cobound peaks map to functionally distinct gene sets: glycolysis, immune differentiation/adhesion, LPS signaling"
slug: hif1a-only-p65-only-cobound-peaks-distinct-functions
status: supported
confidence: 0.85
tags:
  - HIF1A
  - p65
  - ChIP-seq
  - GO-enrichment
  - GSEA
  - glycolysis
  - LPS-signaling
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "GO enrichment + GSEA on gene sets corresponding to HIF1α-only, p65-only, and cobound peaks in mMAC1 (Calafell 2024 Fig. 4G-H). HIF1α-only: glycolysis-related categories. p65-only: immune differentiation/adhesion. Cobound: LPS-mediated signaling pathway. GSEA: HIF1α-bound up only with hypoxia; p65-bound up only with LPS; cobound up with either."
conditions: "Peak-to-gene assignment by nearest TSS; GO Biological Process; GSEA on hypoxia/LPS DEG comparisons."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The three classes of TF binding sites (HIF1α-only, p65-only, cobound by HIF1α + p65) in mMAC1 map to functionally distinct gene programs: HIF1α-only sites drive glycolytic metabolism; p65-only sites drive immune cell differentiation and adhesion; cobound sites drive LPS-mediated signaling. GSEA confirms each gene set is up-regulated only by its specific input (hypoxia, LPS, or either) consistent with a non-redundant division of labor between HIF1α and p65.

## Evidence summary

- GO biological process enrichment per peak set (Calafell 2024 Fig. 4G).
- GSEA across hypoxia-axis and LPS-axis comparisons (Fig. 4H).
- iMAC1 *down*-regulation of p65-bound genes (paradox of unstimulated hypoxic MACs).

## Conditions and scope

- Peak-to-gene assignment by nearest TSS — distal regulatory contributions may be missed.
- GO terms are based on standard databases.

## Counter-evidence

- Some cobound peaks may be functionally redundant rather than non-redundant; deeper perturbation experiments are needed.

## Linked ideas

- Concept: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]].
- Implies distinct chromatin-context interpretations for HIF1α vs p65 binding readout.

## Open questions

- Whether the cobound set is functionally non-redundant or simply combinatorially upregulated.
- Single-cell ATAC + RNA to deconvolve direct vs indirect targets.
