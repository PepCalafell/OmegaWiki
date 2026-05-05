---
title: "mMAC1 / hypoxic-inflammatory MAC signature correlates with better survival in immune-infiltrated cancers"
slug: mmac1-signature-correlates-better-cancer-survival
status: supported
confidence: 0.75
tags:
  - cancer
  - prognosis
  - macrophage
  - tumor-microenvironment
  - bladder-cancer
  - ovarian-cancer
domain: "oncology / immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "TCGA pan-cancer survival analysis: mMAC1 signature → better OS in 10/12 cancers; iMAC1 in 7/12; IL4I1 in 7/12. BLCA Kaplan-Meier: mMAC1-high HR=0.491 (P=0.003); BLCA C2-low-methylation HR=1.72 (P=0.00589). Strong T-cell co-correlation (r=0.74, P=2.2×10⁻⁶⁷)."
conditions: "Bulk-deconvolution-based correlation; causal mechanism inferred from CellChat L-R analysis but not validated in vivo."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

Patients whose tumors have high estimated infiltration of hypoxic inflammatory MACs (mMAC1 signature, IL4I1 MAC signature, low C2 methylation) display significantly better overall survival than low-infiltration patients across multiple immune-infiltrated cancer types, including bladder urothelial carcinoma (BLCA) and ovarian carcinoma (OC).

## Evidence summary

- TCGA pan-cancer (12 cancer types, public data): mMAC1 → better OS in 10/12; iMAC1 in 10/12; IL4I1 MAC in 7/12.
- mMAC21 / iMAC21 / TREM2 / FOLR2 signatures associate with worse OS in 10/12, 10/12, 7/12, 6/12 respectively.
- BLCA Kaplan-Meier: high mMAC1 → better OS (HR=0.491, 95% CI 0.302–0.797, P=0.003); high mMAC21 → worse OS (HR=2.266, P<0.001).
- BLCA: low C2 methylation → better OS (HR=1.72, 95% CI 1.169–2.53, P=0.00589).
- BLCA cell-type correlations: mMAC1 % vs T-cell % r=0.74, P=2.2×10⁻⁶⁷; iMAC21 % vs T-cell % r=−0.27, P=5×10⁻⁸.
- Sorted IL4I1 MACs from primary OC recapitulate mMAC1 epigenetic signature.

## Conditions and scope

- TCGA cohorts (bulk RNA-seq + bulk methylation, deconvolved with CIBERSORTx).
- Strongest separation in BLCA; effect sizes vary across cancer types.
- Correlational, not causal — conditional on the validity of the signature deconvolution.

## Counter-evidence

- TREM2 MACs (poor-prognosis correlate) and IL4I1 MACs co-occur in many tumors; deconvolution may not cleanly separate them.
- Some cancer types show no association in either direction (2/12 for mMAC1 / mMAC21).

## Linked ideas

(none yet)

## Open questions

- Causal validation: does depleting mMAC1 in murine tumor models worsen outcomes?
- Does the C2 methylation signature predict immune-checkpoint-inhibitor response?
- Generalizability beyond BLCA/OC to colorectal, breast, melanoma, etc.
