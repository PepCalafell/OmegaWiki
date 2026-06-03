---
title: "Spatial multiomics orthogonal cross-platform validation"
aliases: ["orthogonal multiplatform validation", "cross-validated cell signatures spatial"]
tags: [spatial-omics, multiomics, methods, validation]
maturity: emerging
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts: [cross-platform-spatial-meta-community, spatially-constrained-ligand-receptor-inference]
---

## Definition

A strategy in which the same biological samples are measured by multiple complementary spatial and single-cell technologies (transcriptomic, proteomic, metabolomic/glycomic), so that cell signatures, spatial maps, and interactomes are accepted only when they are concordant across orthogonal platforms and modalities.

## Intuition

Any single platform has blind spots — scRNA-seq loses spatial context, Visium lacks single-cell resolution, CODEX lacks RNA markers for keratinocytes, glycomics has coarse cell typing. Requiring agreement across technologies that differ in resolution, sensitivity, and analyte class turns each platform's weakness into another's strength and yields high-confidence, reproducible findings.

## Formal notation

Not applicable. In practice: a finding (gene marker, cell type, interaction) is "orthogonally validated" if detected consistently across ≥2–3 platforms/modalities measuring the same or adjacent tissue.

## Variants

- Cross-platform within one modality (Visium + CosMx + Xenium for RNA)
- Cross-modality (RNA + protein + glycan on the same/adjacent sections)
- Computational-then-experimental validation (omics prediction → RNAScope/Opal/PLA)

## Comparison

Differs from single-platform atlasing by making concordance the unit of evidence; differs from simple batch integration in that platforms measure different analytes and resolutions rather than replicates of one assay.

## When to use

When building reference atlases or nominating biomarkers/interactions intended to be robust and actionable, and when guidelines for experimental design across platforms are a deliverable.

## Known limitations

- Expensive; requires access to many platforms and matched tissue
- Partially overlapping gene/protein panels complicate direct comparison
- Concordance can still propagate shared artefacts (e.g. annotation transfer)

## Open problems

- Principled statistical frameworks for "agreement across heterogeneous assays"
- Standardised cross-platform harmonisation pipelines

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — integrates 12 technologies to build orthogonally-validated signatures, maps, and interactomes for three skin cancers, with practical platform-selection guidelines.

## My understanding

The core methodological contribution behind multi-technology atlases: trust emerges from cross-validation, and the paper doubles as a practical guide to which platform answers which question.
