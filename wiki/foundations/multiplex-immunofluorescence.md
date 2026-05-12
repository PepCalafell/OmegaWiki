---
title: "Multiplex immunofluorescence (mIF) staining and spatial analysis"
slug: multiplex-immunofluorescence
domain: "imaging / spatial-biology"
status: established
aliases:
  - "mIF"
  - "multiplex immunofluorescence"
  - "multiplex IF"
  - "tyramide signal amplification"
  - "TSA-mIF"
  - "Opal multiplex"
  - "Vectra Polaris"
  - "spatial mIF"
  - "tissue mIF"
  - "multiplex IHC"
  - "mIHC"
  - "spatial immunofluorescence"
tags:
  - imaging
  - spatial-biology
  - immunology
  - tumor-microenvironment
  - histology
maturity: established
date_updated: 2026-05-12
---

## Definition

Multiplex immunofluorescence (mIF) is a histology technique that visualizes multiple protein markers in a single tissue section using sequential antibody staining coupled with tyramide-based fluorophore deposition (e.g., Opal/Akoya panel) and automated whole-slide imaging (e.g., Vectra Polaris, PhenoImager). It allows simultaneous identification of cell types and their spatial arrangement, typically supporting 6–9 markers per slide plus DAPI counterstain.

## Workflow

1. Sequential primary antibody → HRP-secondary → Opal-tyramide fluorophore deposition; antibody stripping between rounds.
2. Whole-slide multispectral imaging and unmixing.
3. Cell segmentation (DAPI-anchored nuclear segmentation, often via inForm or HALO software).
4. Phenotype calling (e.g., CD68+PD-L1+ vs CD68+PD-L1− TAMs, CD3+CD8+ T cells, cytokeratin+ cancer cells).
5. Spatial analysis: neighborhood/cell-cell distance, density mapping, KDE, niche identification.

## Spatial cell-cell interaction quantification

A common convention treats cells whose nuclei lie within 20 μm of each other as "potentially interacting." This threshold approximates the typical cell-cell contact range and is used (e.g., Wang et al. 2024 Cell Rep Med) to quantify TAM↔T-cell and TAM↔cancer-cell engagement preferences.

## Strengths and limitations

- Preserves spatial architecture lost in scRNA-seq / flow cytometry.
- Antibody panel limits (typically ≤9 markers) constrain phenotype resolution; spatial transcriptomics or IMC/CODEX can extend dimensionality.
- Antigen retrieval and TSA cycling may distort epitopes and bias intensity quantification.
- Inter-laboratory reproducibility depends on panel validation, scanner calibration, and segmentation pipelines.
