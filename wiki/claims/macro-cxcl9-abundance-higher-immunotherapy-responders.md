---
title: "Macro-CXCL9 abundance is higher in immunotherapy responders across multiple cohorts"
slug: macro-cxcl9-abundance-higher-immunotherapy-responders
status: supported
confidence: 0.7
tags: [CXCL9, macrophage, ICB-response, biomarker, deconvolution]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.4): 'The responder (R) group in this cohort showed a significantly higher proportion of Macro-CXCL9 (P < 0.001).' and 'Tumors responsive to treatment after therapy exhibited higher levels of Macro-CXCL9 compared to non-responsive tumors.'"
conditions: "CIBERSORTx deconvolution of IMvigor210 bulk RNA-seq; validated by re-analysis of three scRNA-seq ICB cohorts (breast cancer, RCC)."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

CXCL9⁺ macrophage (Macro-CXCL9) abundance is significantly higher in immune checkpoint blockade responders, shown by CIBERSORTx deconvolution of IMvigor210 (P<0.001) and corroborated by re-analysis of breast cancer and renal cell carcinoma scRNA-seq ICB cohorts.

## Evidence summary

Cross-cohort correlational evidence from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]. Aligns with [[concepts/ifng-mac-cxcl9-tam-ici-responder]] and [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]].

## Conditions and scope

Deconvolution-derived proportions in bulk cohorts; retrospective datasets; association, not causation.

## Counter-evidence

Deconvolution with an incomplete reference can bias proportions ([[concepts/deconvolution-with-incomplete-reference]]).

## Linked ideas

## Open questions

- Does Macro-CXCL9 abundance add predictive value beyond existing CXCL9:SPP1 ratio biomarkers?
