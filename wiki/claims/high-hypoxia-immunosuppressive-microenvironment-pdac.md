---
title: "High hypoxia score in TCGA-PAAD is associated with an immunosuppressive TME (lower naïve B, higher M0 macrophages, lower immune/stromal/ESTIMATE scores)"
slug: high-hypoxia-immunosuppressive-microenvironment-pdac
status: supported
confidence: 0.7
tags: [hypoxia,PDAC,immune-microenvironment,CIBERSORT,ESTIMATE,naive-B-cells,M0-macrophage,immune-exclusion]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.9–10, Results): 'the high hypoxia group exhibited higher tumor purity and lower immune, stromal, and ESTIMATE scores (Fig 6A), suggesting a negative correlation between hypoxia scores and immune cell infiltration... a reduced presence of anti-tumor immune cells such as naive B cells in the high hypoxia group, while macrophages M0 were predominantly enriched (Fig 6B)'. ESTIMATE for purity / immune / stromal scoring; CIBERSORT (LM22) for 22 immune subsets."
conditions: "Single cohort (TCGA-PAAD); deconvolution-based — no spatial or single-cell verification of the M0 macrophage enrichment claim."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

In TCGA-PAAD, patients in the high-hypoxia group (13-gene model) show: (i) higher tumour purity and lower immune, stromal, and ESTIMATE scores; (ii) reduced naïve B cell infiltration; (iii) enriched M0 (undifferentiated) macrophages. The pattern is consistent with an immunosuppressive, immune-excluded TME concomitant with the hypoxic niche.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 6A–C). Mechanism-consistent with [[concepts/hypoxia-pd-l1-tam-immune-evasion]] and [[claims/hypoxia-impairs-nk-perforin-granzyme-nkg2d]].

## Conditions and scope

- Deconvolution-based (CIBERSORT LM22), bulk transcriptome; M0 macrophage enrichment is the deconvolution category and may not correspond cleanly to a single-cell M0 state.
- Naïve B cell reduction is biologically plausible but not validated by IHC or spatial transcriptomics in this paper.

## Counter-evidence

None within paper scope.

## Linked ideas

## Open questions

- Does the M0 macrophage signal correspond to the hypoxia-responsive macrophage cluster 1 identified in the scRNA-seq arm, or to a different population?
- Is the naïve B cell reduction predictive of immunotherapy non-response in PDAC?
