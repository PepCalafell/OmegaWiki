---
title: "CellCharter outperforms STAGATE/BayesSpace/SEDR/DR-SC/SOTIP/UTAG on joint DLPFC clustering"
slug: cellcharter-outperforms-stagate-bayesspace-sedr-dr
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - benchmark
  - clustering
  - DLPFC
  - methodological
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: strong
    detail: "DLPFC Visium benchmark: best mean ARI ~0.62 (CellCharter) vs 0.45–0.51 (BayesSpace, SEDR, DR.SC, STAGATE) and 0.36 (UTAG) on joint clustering of 9 test samples; statistically significant (P<0.05 to P=1e-7 across pairwise t-tests)."
conditions: "Joint multi-sample clustering on DLPFC Visium. Single-sample clustering is dominated by STAGATE."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

In joint multi-sample spatial clustering of the human dorsolateral prefrontal cortex (DLPFC) Visium benchmark, CellCharter achieves higher mean ARI than STAGATE, BayesSpace, SEDR, DR-SC, SOTIP, and UTAG.

## Evidence summary

Fig. 1d–e: CellCharter mean ARI ≈ 0.62, STAGATE ≈ 0.49, DR.SC ≈ 0.51, BayesSpace ≈ 0.45, SEDR ≈ 0.45, UTAG ≈ 0.36. Two-sided t-test P values: 0.04, 1×10⁻⁷, 4.7×10⁻⁵, 5.6×10⁻³, 2.4×10⁻⁵.

## Conditions and scope

Holds for joint clustering of 9 held-out DLPFC samples with batch correction. On single-sample clustering, STAGATE achieves the best ARI (Extended Data Fig. 1g) — so the result is conditional on the joint multi-sample setting that CellCharter targets.

## Counter-evidence

STAGATE's superior single-sample performance is the main caveat. SOTIP and SEDR (GPU) could not jointly cluster all Visium samples because of memory constraints, so they are partially excluded from the comparison.

## Linked ideas

— none yet.

## Open questions

- Do these rankings hold on imaging-based platforms (CosMx, MERFISH) where panel size is smaller?
- How does CellCharter compare on the newer Visium HD / Xenium platforms?
