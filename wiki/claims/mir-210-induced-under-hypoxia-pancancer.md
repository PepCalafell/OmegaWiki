---
title: "miR-210 abundance is positively correlated with hypoxia score in 18 of 19 tumor types"
slug: mir-210-induced-under-hypoxia-pancancer
status: supported
confidence: 0.95
tags:
  - miR-210
  - hypoxia
  - microRNA
  - HIF1A
  - pancancer
  - canonical
domain: "oncology / non-coding-RNA / hypoxia"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "miR-210 abundance positively correlated with hypoxia score across all 18 tumor types tested (Spearman ρ range=0.20–0.66) in 8,006 tumors. Quote (p.311): 'miR-210 abundance was associated with elevated hypoxia score across all 18 tumor types (Spearman's ρ range=0.20–0.66).' Bridges to HIF1A-driven glycolysis: miR-210 ↔ LDHA protein in BRCA (ρ=0.72, FDR=5.66×10⁻⁷) and OV (ρ=0.42, FDR=6.21×10⁻⁴)."
conditions: "Holds across 18 of 19 TCGA tumor types where miRNA expression data were available. The single non-significant tumor type is not specified explicitly."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

miR-210 abundance is positively correlated with mRNA-based tumor hypoxia score across virtually all TCGA tumor types (18 of 19), with Spearman correlations ranging 0.20–0.66. This is the most universal pancancer hypoxia-miRNA association, consistent with prior studies establishing miR-210 as a direct HIF1A transcriptional target. miR-210 abundance further correlates with the protein abundance of LDHA — a glycolytic enzyme — in breast (ρ=0.72) and ovarian (ρ=0.42) cancer, bridging the miRNA layer to HIF1A-driven metabolic remodelling.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary pancancer evidence: 18/19 tumor types, ρ range 0.20–0.66.
- Mechanistic prior: Kulshreshtha 2007 *Mol Cell Biol*, Camps 2008 *Clin Cancer Res*, Huang 2009 *Mol Cell* — direct HIF1A binding at MIR210 promoter.

## Conditions and scope

- Holds across solid tumors with miRNA-seq data in TCGA.
- Bulk-tumor measurements; assumes both signature and miR-210 read predominantly the malignant compartment.

## Counter-evidence

- One tumor type (not explicitly named) did not show the association.
- Direction of miR-210 effect is context-dependent (pro-survival in mild hypoxia, pro-apoptotic with reoxygenation).

## Linked ideas

(none yet)

## Open questions

- Which tumor type breaks the pattern, and why?
- Single-cell vs bulk: how much of miR-210 signal is from malignant vs stromal cells?
- Does miR-210 in immune cells (macrophages, T cells) follow the same induction pattern?
