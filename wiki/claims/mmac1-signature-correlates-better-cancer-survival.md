---
title: "mMAC1 / IL4I1 signatures correlate with better overall survival in multiple TCGA cancer types, including bladder (HR=0.491) and ovarian carcinoma"
slug: mmac1-signature-correlates-better-cancer-survival
status: supported
confidence: 0.8
tags:
  - mMAC1
  - IL4I1
  - cancer-survival
  - TCGA
  - BLCA
  - ovarian-carcinoma
  - prognosis
domain: "oncology / immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "TCGA pan-cancer survival analysis (Calafell 2024 Fig. 5D, fig. S5D-E). mMAC1 high-signature: better OS in 10/12 cancer types. IL4I1 high-signature: better OS in 7/12 (including BLCA, OC). BLCA HR for mMAC1 = 0.491 (CI 0.302-0.797, P = 0.003). BLCA HR for mMAC21 = 2.266 (1.401-3.663, P < 0.001). C2 CpG low-methylation in BLCA: HR = 1.72 (P = 0.00589)."
conditions: "TCGA bulk RNA-seq; signature-score Cox regression; 12 cancer types."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

The in vitro mMAC1 transcriptomic signature, and its in vivo correlate IL4I1 MAC signature, both correlate with better overall survival across multiple TCGA cancer types. mMAC1 signature high → better OS in 10/12 cancer types; IL4I1 signature high → better OS in 7/12. In bladder urothelial carcinoma specifically, mMAC1 HR = 0.491 (P = 0.003); mMAC21 (normoxic) HR = 2.266 (P < 0.001). C2-CpG low methylation also predicts better BLCA OS (HR = 1.72, P = 0.006).

## Evidence summary

- Kaplan-Meier + Cox regression on TCGA bulk RNA-seq per signature (Calafell 2024 Fig. 5D, fig. S5D-E).
- Pan-cancer breakdown across 12 types (fig. S5D).
- BLCA-specific HR values (Fig. 5D).
- C2 methylation HR (Fig. 5E).

## Conditions and scope

- Correlation, not causation.
- TCGA bulk RNA-seq; deconvolution-derived signatures, not single-cell.
- 12 cancer types; not all show the same direction.

## Counter-evidence

- Some IL4I1 MAC roles are described as immunosuppressive (PD-L1, IDO1) — context-dependent. The OS-favorable correlation conflicts with that framing, suggesting the bulk signature captures the inflammatory subset of IL4I1 MACs rather than the immunosuppressive subset.
- Park 2024 (CRC efferocytosis) shows IL4I1 MACs at the tumor invasive front are favorable — consistent with this claim.

## Linked ideas

- Direct clinical translational anchor for mMAC1.
- Implies mMAC1 / IL4I1 MAC expansion may be a beneficial immunotherapy strategy.

## Open questions

- Causal vs correlational role of mMAC1 in the OS benefit.
- Whether mMAC1 signature predicts ICI response (PD-1/PD-L1 blockade).
- Single-cell validation of mMAC1 ↔ IL4I1 mapping in matched primary tumors.
