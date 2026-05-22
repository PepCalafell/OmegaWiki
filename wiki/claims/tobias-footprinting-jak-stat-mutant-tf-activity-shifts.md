---
title: "TOBIAS footprinting reveals mutant-specific TF activity: RUNX2 (Stat5-hyp T), EOMES & FOS::JUN (Stat5-KO T), GATA1::TAL1 (Stat5-KO Mac), NFKB2 (Stat6-KO Mac), ZBED1 depletion (Stat4-KO T)"
slug: tobias-footprinting-jak-stat-mutant-tf-activity-shifts
status: supported
confidence: 0.75
tags: [tobias, atac-footprinting, tf-activity, runx2, eomes, ap1, gata1, tal1, nfkb2, zbed1, jak-stat]
domain: immunology
source_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
evidence:
  - source: jak-stat-signaling-maintains-homeostasis-cells
    type: supports
    strength: strong
    detail: "Fig. 5c: TOBIAS BINDetect on ATAC-seq with JASPAR2022 PFMs identifies condition-specific TF footprint changes — RUNX2 enriched in Stat5-hyp T cells; EOMES and FOS::JUN heterodimer in Stat5-KO T cells; GATA1::TAL1 in Stat5-KO macrophages; NFKB2 in Stat6-KO macrophages; ZBED1 depleted in Stat4-KO T cells (decreased-accessibility regions)."
conditions: "Mouse spleen homeostatic CD8+ T cells and macrophages; bulk ATAC-seq; JASPAR2022 core non-redundant PFMs."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

TOBIAS-based differential TF footprinting on bulk ATAC-seq from JAK-STAT mutant mouse spleen immune cells identifies condition-specific TF activity shifts that propose mechanistic intermediaries downstream of each JAK-STAT perturbation: RUNX2 in Stat5-hyp T cells (cell-cycle / oncogenic); EOMES and AP1 (FOS::JUN) in Stat5-KO T cells; GATA1::TAL1 in Stat5-KO macrophages; NFKB2 in Stat6-KO macrophages; ZBED1 depletion in Stat4-KO T cells. These predictions are motif-based and are not yet ChIP-validated.

## Counter-evidence

- TOBIAS footprint calls are motif-based, so any TF sharing the same motif family could explain a given footprint. Direct ChIP / CUT&RUN validation is not provided.
