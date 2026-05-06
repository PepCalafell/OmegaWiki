---
title: "TRMs (not BMMs) induce EMT in KP tumour cells in 3D spheroid co-culture"
slug: trm-induce-emt-program-tumor-cells-spheroids
status: supported
confidence: 0.9
tags:
  - TRM
  - EMT
  - 3D-spheroid
  - tumor-invasiveness
  - TWIST1
  - E-cadherin
domain: "oncology / cell biology"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: strong
    detail: "3D Matrigel spheroid co-culture: KP-GFP cells alone vs with sorted alveolar TRMs vs with bone-marrow monocytes (BMMs). FACS-sorted KP cells (DAPI⁻CD45⁻GFP⁺) profiled by RNA-seq. TRM co-culture induces EMT-associated DEGs (Vegfa, Wnt11, Pld2, Flt1, Pdgfb, Itgb1, Sema3f/4c/6b, Rhoa, Lamc2, Plau, Acvr1, Fn1) — distinct from BMM co-culture (cell-cycle / DNA replication genes Cdk4, Mcm4, Brca1/2, Chek1). Confocal IF: TRM co-culture reduces E-cadherin protein, induces TWIST1; tMDM and BMM co-cultures do not. Live spheroid imaging: TRMs increase tumour cell dispersion area over time. 3D Matrigel: KP+TRM spheroids form invasive protrusions; KP+tMDM/+BMM spheroids form colonies without protrusions. Five pooled independent experiments; one-way ANOVA, P<0.0001."
conditions: "3D Matrigel spheroid co-culture; KP-GFP cells (2,500/well) + 5,000 TRMs or BMMs; 7-day culture; GM-CSF for TRM medium and M-CSF for BMM medium; FACS sort of KP cells for RNA-seq."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In 3D Matrigel spheroid co-culture, alveolar TRMs (but not bone-marrow monocytes BMMs or tumour-associated MDMs) selectively induce an epithelial-mesenchymal transition (EMT) programme in KP NSCLC tumour cells: reduced E-cadherin protein, TWIST1 induction, upregulation of EMT-associated genes (VEGFA, ITGB1, PLAU, FN1, RHOA, etc.), and the formation of invasive protrusions in matrix.

## Evidence summary

- 3D spheroid RNA-seq of KP-GFP cells co-cultured with TRMs vs BMMs
- TRM-induced DEGs: EMT / migration / invasion programme (VEGFA, WNT11, PLD2, FLT1, PDGFB, ITGB1, RHOA, LAMC2, PLAU/uPA, FN1)
- BMM-induced DEGs: cell-cycle / DNA replication (CDK4, MCM4, BRCA1/2, CHEK1) — distinct programme
- Confocal IF: reduced E-cadherin and induced TWIST1 in KP+TRM but not KP+BMM or KP+tMDM
- Live time-lapse imaging: TRM co-culture increases dispersion area
- 3D Matrigel: invasive protrusions in KP+TRM spheroids only
- Five pooled independent experiments; one-way ANOVA P<0.0001

## Conditions and scope

- Mouse-derived TRMs vs BMMs vs tMDMs in 3D Matrigel co-culture
- KP-GFP cell line (KrasG12D Trp53⁻/⁻)
- 7-day timeline; 1×10³ KP cells seeded; 5×10⁴ macrophages added at day 7

## Counter-evidence

- Selectivity is shown for KP cells; whether it extends to other lung adenocarcinoma cell lines or human NSCLC cells is untested
- The relative contribution of contact-dependent vs soluble signalling not fully resolved (CM works, suggesting soluble; co-culture is stronger, suggesting contact augments)
- Bulk-sorted TRMs may contain heterogeneous subpopulations; intra-TRM variation unaccounted

## Linked ideas

(none yet)

## Open questions

- Identification of the specific TRM-secreted factor(s) responsible for EMT induction
- Cross-validation in human alveolar macrophage + NSCLC organoid co-cultures
- Whether the TRM-EMT axis can be blocked by anti-TGFβ, anti-uPAR, or other targeted interventions
