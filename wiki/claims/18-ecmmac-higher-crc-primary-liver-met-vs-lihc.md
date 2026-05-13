---
title: "18_ECMMac proportion differs significantly between primary CRC, CRC liver metastases, and primary LIHC (Propeller q=8.7e-7)"
slug: 18-ecmmac-higher-crc-primary-liver-met-vs-lihc
status: supported
confidence: 0.9
tags: [TAM,18_ECMMac,CRC,liver-metastasis,LIHC,Propeller,cell-composition]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.4, Fig. 3a): 'q-values for 6_SPP1AREGMac, 7_IFNMac, 8_IFNGMac, 16_ECMHomeoMac, 18_ECMMac were 0.029..., 0.086..., 0.039..., 0.016..., and 0.0000008703445 respectively'."
conditions: "Propeller v0.99.1 with arcsin transformation; FDR-corrected ANOVA across CRC primary, CRC liver metastasis, primary LIHC."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Cell-composition testing across primary CRC, CRC liver metastases, and primary LIHC shows 18_ECMMac proportions differ significantly (q=8.7e-7), with enrichment in CRC primary and CRC liver metastases relative to LIHC — implicating tumour genotype as a driver of ECM-modifying TAM differentiation.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 3a). Tested with [[foundations/propeller-cell-composition-analysis]].

## Conditions and scope

Compositional analysis only; no functional perturbation.

## Counter-evidence

None within paper's scope.

## Linked ideas

## Open questions

- Which CRC-specific tumour-cell signalling drives macrophage ECM-modifying differentiation in the liver metastatic niche?
