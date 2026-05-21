---
title: "Most SVG-detection methods produce poorly calibrated p-values under spatial-null conditions"
slug: most-svg-methods-poorly-calibrated
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - calibration
  - statistics
  - benchmarking
domain: spatial-transcriptomics-methods
source_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "QQ plot against expected uniform on shuffled-spot 10x Visium mouse olfactory bulk and 10x Xenium human colon cancer null data. Only SPARK and SPARK-X produce well-calibrated p-values. 6 methods over-conservative (SpatialDE, Spanve, SOMDE, scGCO, nnSVG, BOOST-GP), 4 over-liberal (SpaGFT, GPcounts, SpaGCN, Moran's I). Replicated across two ST platforms."
conditions: "Null constructed by random spot shuffling on real Visium and Xenium datasets. Calibration measured by K-S distance between observed p-value distribution and U(0,1)."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

Of 14 SVG-detection methods evaluated under a spatially-shuffled null on 10x Visium mouse olfactory bulb and 10x Xenium colon cancer data, only SPARK and SPARK-X produce well-calibrated p-values. The rest systematically over- or underestimate significance, breaking either type I or type II error control.

## Evidence summary

Quote (p.8): "SPARK-X and SPARK produced well-calibrated p-values. In contrast, other methods showed poor calibration… Specifically, six methods (SpatialDE, Spanve, SOMDE, scGCO, nnSVG, and BOOST-GP) generated over-conservative p-values, indicating a failure to control type II error. Conversely, four methods (SpaGFT, GPcounts, SpaGCN, and Moran's I) generally overestimated the p-values, failing to control type I errors."

The SPARK/SPARK-X advantage is attributed to the Cauchy combination rule for combining p-values from multiple kernels (p.8).

## Conditions and scope

Holds on the two specific Visium and Xenium null datasets. Not separately validated on imaging-based ST (MERFISH, seqFISH) nulls. The authors recommend selecting SVGs by a fixed top-N rank threshold rather than by p-value significance to mitigate the practical impact of miscalibration.

## Counter-evidence

None reported within the paper. Prior benchmarking studies (Charitakis et al. 2023; Zhang et al. 2024) also observe miscalibration but were less systematic.

## Linked ideas

(none yet)

## Open questions

- How well-calibrated are these methods on subcellular-resolution data (MERFISH, Xenium HD, CosMx)?
- Do the Cauchy-combination kernels generalise to new technologies, or do they need re-tuning per platform?
