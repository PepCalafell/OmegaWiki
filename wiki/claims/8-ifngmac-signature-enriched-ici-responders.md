---
title: "8_IFNGMac, 17_IFNMac3, 14_ProliMac, 11_MetalloMac, 4_ICIMac2, 3_ICIMac1 and 20_TDoub signatures are significantly enriched in ICI responders in CPI1000+"
slug: 8-ifngmac-signature-enriched-ici-responders
status: supported
confidence: 0.9
tags: [TAM,8_IFNGMac,ICI-response,CPI1000,fgsea,biomarker,CXCL9]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.5, Fig. 4a): '20_TDoub and 8_IFNGMac signatures were both significantly enriched in responding patients (fgsea, q-value = 0.001668273617609862 and 0.000000000013715289 respectively)... signatures 17_IFNMac3, 14_ProliMac, 11_MetalloMac, 4_ICIMac2 and 3_ICIMac1 were significantly enriched in responders'."
conditions: "CPI1000+ bulk RNAseq cohort (n=1446); DESeq2 with tumour type + response; fgsea with cluster-specific 10-gene signatures; FDR q<0.1."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Seven TAM cluster signatures are significantly enriched in ICI responders in CPI1000+: 8_IFNGMac (q≈1.4e-11), 17_IFNMac3 (q≈1.8e-8), 14_ProliMac (q≈6.1e-12), 11_MetalloMac (q=0.036), 4_ICIMac2 (q=2.8e-3), 3_ICIMac1 (q=0.028), and 20_TDoub (q=1.7e-3).

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4a).

## Conditions and scope

Pan-tumour cohort; cluster-specific signatures, not single-gene markers. The 20_TDoub signal is expected because it is composed of T-cell+macrophage doublets.

## Counter-evidence

TREM2+ clusters (3_ICIMac1, 4_ICIMac2) being responder-associated is *opposite* to the prevailing TREM2-as-ICI-resistance hypothesis from mouse models (ref 71) — see [[claims/trem2-tams-recapitulate-melanoma-ici-resistance]].

## Linked ideas

## Open questions

- Why do TREM2+ TAM clusters associate with response in pan-cancer human bulk data despite mouse TREM2-inhibition data suggesting they should suppress response?
