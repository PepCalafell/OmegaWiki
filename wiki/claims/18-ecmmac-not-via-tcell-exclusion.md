---
title: "18_ECMMac-associated ICI resistance is not explained by general T-cell exclusion in CPI1000+ (T-cell signature is higher in high-ECM samples)"
slug: 18-ecmmac-not-via-tcell-exclusion
status: supported
confidence: 0.85
tags: [18_ECMMac,T-cell-exclusion,ICI-resistance,CPI1000,mechanism]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.5, Fig. 4b): 'we observed significantly higher (Two-sided Mann-Whitney U test; nlower = 362, nupper = 723; p < 0.0001; W = 74219... T-cell signatures associated in the upper quartile of ECM signature samples in the CPI1000+, indicating that general T cell exclusion might not be the mechanism of association between response and this cluster'."
conditions: "CPI1000+ bulk RNAseq; generalised T-cell signature of 19 T-cell-specific genes (ref 109)."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

In CPI1000+, the generalised T-cell signature is significantly *higher* (not lower) in the upper quartile of the 18_ECMMac signature (Mann-Whitney W=74,219; p<0.0001; n_lower=362, n_upper=723). Therefore the mechanism by which 18_ECMMac associates with ICI non-response is not bulk T-cell exclusion — pointing instead toward TAM-fibroblast-T-cell functional interactions or ECM-mediated dysfunction.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4b).

## Conditions and scope

Bulk-RNAseq T-cell-signature based; spatial T-cell exclusion (peritumoural vs intratumoural) not directly assessed.

## Counter-evidence

Bulk T-cell signature does not distinguish exhausted vs functional T cells; T-cell dysfunction (not exclusion) could still be the mechanism.

## Linked ideas

## Open questions

- Is T-cell *function* (exhaustion / dysfunction) — rather than infiltration — the actual mediator of 18_ECMMac-associated ICI resistance?
