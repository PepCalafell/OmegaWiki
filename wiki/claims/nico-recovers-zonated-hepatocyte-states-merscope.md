---
title: "NiCo annotates 375,161/391,679 (95.8%) cells in MERSCOPE mouse liver and correctly resolves portal-vs-mid-zonal-vs-central hepatocyte states co-localized with portal-vein, mid-zonal, and central-vein endothelial cells, where cell2location/Tangram/TACCO/uniPort struggle to separate mid-zonal and portal hepatocytes"
slug: nico-recovers-zonated-hepatocyte-states-merscope
status: supported
confidence: 0.85
tags: [MERSCOPE,liver,hepatocyte-zonation,annotation,benchmark]
domain: hepatology / spatial-transcriptomics
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: strong
    detail: "MERSCOPE liver atlas annotation; spatial localization of portal vs central vein ECs matches expected hepatic-lobule architecture; comparison vs cell2location, Tangram, TACCO, uniPort shows NiCo and TACCO/cell2location resolve hepatocyte zones, but separation of mid-zonal and portal hepatocytes weaker for non-NiCo methods (Fig. 5a–c, Suppl. Fig. 7)."
conditions: "Single MERSCOPE liver dataset (391,679 cells); no human liver validation."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

NiCo annotates 375,161/391,679 (95.8%) cells in MERSCOPE mouse liver and correctly resolves portal-vs-mid-zonal-vs-central hepatocyte states co-localized with portal-vein, mid-zonal, and central-vein endothelial cells, where cell2location/Tangram/TACCO/uniPort struggle to separate mid-zonal and portal hepatocytes.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — MERSCOPE liver atlas annotation; spatial localization of portal vs central vein ECs matches expected hepatic-lobule architecture; comparison vs cell2location, Tangram, TACCO, uniPort shows NiCo and TACCO/cell2location resolve hepatocyte zones, but separation of mid-zonal and portal hepatocytes weaker for non-NiCo methods (Fig. 5a–c, Suppl. Fig. 7).

## Conditions and scope

Single MERSCOPE liver dataset (391,679 cells); no human liver validation.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
