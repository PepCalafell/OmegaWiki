---
title: "The DP thymocyte proliferative wave is validated by a high G2M cell-cycle fraction"
slug: dp-thymocyte-proliferative-wave-validated-high
status: weakly_supported
confidence: 0.7
tags:
  - thymocyte
  - cell-cycle
  - G2M
  - validation
domain: "haematopoiesis / immunology"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "scRNA-seq cell-cycle phase scoring showed a high G2M proportion of cycling DP cells, independently corroborating the third proliferative burst predicted by pseudodynamics+ (which v1 did not capture)."
conditions: "Same mouse embryonic thymus dataset; cell-cycle phase from scRNA-seq scoring."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

The third (DP-cell) proliferative burst inferred by pseudodynamics+ is supported by an orthogonal readout: DP cells show a high G2M cell-cycle phase fraction.

## Evidence summary

Cross-validation of the inferred growth rate against scRNA-seq cell-cycle scoring strengthens the parameter estimate.

## Conditions and scope

Correlative agreement, single dataset.

## Counter-evidence

None reported.

## Linked ideas

## Open questions

- Direct quantification (e.g. EdU/Ki67) of DP proliferation to confirm the burst.
