---
title: "IFITM1 discriminates COPD from asthma in lymphoid cells (high→COPD, low→asthma)"
slug: ifitm1-discriminates-copd-asthma-lymphoid-cells
status: weakly_supported
confidence: 0.7
tags:
  - IFITM1
  - biomarker
  - COPD
  - asthma
  - lymphoid
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "d-SHAP ranking highlighted IFITM1 across chronic diseases: importance was concentrated in lymphoid cells (CD4 non-naive T cells, ILCs), where higher IFITM1 expression drives classification toward COPD and lower expression toward asthma."
conditions: "CD4 non-naive T cells and ILCs; chronic airway diseases."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

IFITM1, an interferon-induced antiviral restriction factor, discriminates chronic airway diseases in lymphoid cells: in CD4 non-naive T cells and ILCs, higher IFITM1 expression drives classification toward COPD and lower expression toward asthma. The authors hypothesize chronic inflammation raises IFITM1 to facilitate lymphoid accumulation.

## Evidence summary

d-SHAP scatter plots for IFITM1 in T CD4 non-naive and ILC populations (Fig. 3d; Extended Data Fig. 6d,e; p.639), with mechanistic validation flagged as needed.

## Conditions and scope

Lymphoid cells; chronic airway disease; correlative.

## Counter-evidence

Mechanistic link to lymphoid accumulation is an explicit hypothesis pending validation.

## Linked ideas

- [[concepts/interpretable-ml-disease-discriminative-gene-discovery]]
- Foundations: [[foundations/ifitm1-interferon-induced-transmembrane-protein]]

## Open questions

- Does IFITM1 mechanistically drive lymphoid accumulation in COPD?
