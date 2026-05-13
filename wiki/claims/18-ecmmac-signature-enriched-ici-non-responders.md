---
title: "18_ECMMac signature is enriched in non-responders to ICI in the CPI1000+ bulk RNAseq cohort (fgsea q=3.8e-5)"
slug: 18-ecmmac-signature-enriched-ici-non-responders
status: supported
confidence: 0.9
tags: [TAM,18_ECMMac,ICI-resistance,CPI1000,fgsea,biomarker]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.5, Fig. 4a): '18_ECMMac was significantly enriched in non-responding patients (fgsea, q-value = 0.000038213695118505)'."
conditions: "CPI1000+ bulk RNAseq cohort (n=1446 ICI-treated patients: 552 bladder, 411 lung, 226 melanoma, 212 RCC, 45 gastric); DESeq2 design controls for tumour type + response; fgsea with 10-gene top-DEG signature."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

In an expanded CPI1000+ cohort of 1,446 ICI-treated patients across 5 cancer types, the top-10-gene signature of the 18_ECMMac cluster is significantly enriched in non-responders (fgsea q=3.8e-5), making it the most strongly resistance-associated cluster signature in the atlas.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4a). Mechanism is *not* T-cell exclusion ([[claims/18-ecmmac-not-via-tcell-exclusion]]).

## Conditions and scope

Bulk-RNAseq ICI-treated patients; pan-tumour effect controlled by DESeq2 design. The collagen signature confounds with fibroblasts; causal attribution to TAMs versus stromal cells is associative.

## Counter-evidence

The same 18_ECMMac genes are expressed by fibroblasts; cluster-level functional dissection requires single-cell or perturbation data not in this paper.

## Linked ideas

## Open questions

- Does isolated TAM-specific perturbation of collagen secretion reverse ICI resistance?
- Is the signal driven by 18_ECMMac per se or by an underlying TAM-fibroblast niche?
