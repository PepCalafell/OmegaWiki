---
title: "Seven TAM cluster signatures (5_StressMac, 6_SPP1AREGMac, 8_IFNGMac, 11_MetalloMac, 17_IFNMac3, 21_HemeMac, 22_IFNMac4) meet 'gold-standard' criteria for bulk-RNAseq deconvolution"
slug: seven-gold-standard-tam-bulk-signatures
status: supported
confidence: 0.9
tags: [bulk-RNAseq,deconvolution,gold-standard,TAM-signature,UCell]
domain: computational-biology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (Methods): 'This gave us a set of \"gold-standard\" signatures that should be reliable for profiling in bulk RNA data, including 5_StressMac, 6_SPP1AREGMac, 8_IFNGMac, 11_MetalloMac, 17_IFNMac3, 21_HemeMac and 22_IFNMac4'."
conditions: "All-cell-type atlas of 482,677 cells (refs 30, 31, 39: breast/CRC/OV/lung + ccRCC + lung); per-cluster top-10 DEG signature; UCell scoring; Metric1 (top - second-top mean UCell) > 0.1; Metric2 (best-hit cluster matches signature in ≥3 of 5 cancer types)."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Of 23 TAM cluster signatures, seven (5_StressMac, 6_SPP1AREGMac, 8_IFNGMac, 11_MetalloMac, 17_IFNMac3, 21_HemeMac, 22_IFNMac4) consistently identify their respective clusters when assessed via UCell scores in an all-cell-type atlas and across multiple cancer types — meeting the authors' "gold-standard" criterion for bulk-RNAseq deconvolution.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Methods + Supplementary Data 5-6).

## Conditions and scope

Criterion thresholds (Metric1 > 0.1; ≥3 of 5 cancer types) are conservative; signatures outside this set may still be useful in specific deployments.

## Counter-evidence

Signatures from non-gold-standard clusters (e.g., 18_ECMMac, 3_ICIMac1, 4_ICIMac2) are still used in CPI1000+ analyses despite failing the criterion — caveats about cell-type contamination apply.

## Linked ideas

## Open questions

- Performance benchmark of these signatures against reference-based deconvolution tools (CIBERSORTx, BayesPrism) is not in the paper.
