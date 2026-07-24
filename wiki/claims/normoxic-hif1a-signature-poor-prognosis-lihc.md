---
title: "Huh7-derived normoxic and hypoxic HIF-1α protein signatures correlate with poor survival in LIHC (not HeLa/CESC)"
slug: "normoxic-hif1a-signature-poor-prognosis-lihc"
status: supported
confidence: 0.7
tags:
  - HIF1a
  - prognosis
  - LIHC
  - TCGA
  - GEPIA2
  - gene-signature
  - hepatocellular-carcinoma
domain: oncology / cancer-genomics
source_papers:
  - oxygen-independent-expression-hif-during-cell
evidence:
  - source: oxygen-independent-expression-hif-during-cell
    type: supports
    strength: moderate
    detail: "TCGA/GEPIA2: Huh7-derived normoxic (P=0.0023) and hypoxic (P=0.0081) HIF-1α-dependent protein signatures predict worse LIHC overall survival and correlate with HIF1A expression; HeLa-derived signatures show no CESC survival correlation (P=0.85 / P=0.4)."
conditions: "GEPIA2 analysis of TCGA LIHC and CESC; four gene signatures from HIF-1α-upregulated proteins; Kaplan–Meier overall survival."
date_proposed: 2026-07-24
date_updated: 2026-07-24
---

## Statement

The HIF-1α-dependent protein-expression signatures identified in Huh7 HCC cells — under both normoxia and hypoxia — correlate with HIF1A expression and with poor overall survival in liver hepatocellular carcinoma (LIHC) patients (TCGA/GEPIA2), whereas the analogous HeLa-derived signatures do not predict survival in cervical carcinoma (CESC), supporting the clinical relevance of the HCC-specific normoxic HIF-1α program.

## Evidence summary

- **oxygen-independent-expression-hif-during-cell** (p.3156–3157) — TCGA/GEPIA2 correlation + Kaplan–Meier.
  - Quote: "Kaplan-Meier survival analysis showed a significant correlation between higher expression of our normoxic (P = 0.0023) or hypoxic (P = 0.0081) HIF-1α-dependent signatures derived from Huh7 cells and poor outcomes for LIHC patients."
  - Quote: "there was no significant correlation of overall survival with the expression of the HeLa-derived normoxic ... (P = 0.85) or ... hypoxic protein signature (P = 0.4)."

## Conditions and scope

Signatures scored at the mRNA level (bulk RNA-seq) as a proxy for the protein signatures; associations are correlative, not causal. LIHC and CESC cohorts only.

## Counter-evidence

None recorded. mRNA-based survival readout for protein-derived signatures; no multivariable adjustment reported.

## Linked ideas

_None yet._

## Open questions

- Do the normoxic vs hypoxic Huh7 signatures carry independent prognostic value in LIHC after adjustment for stage and HIF1A?
