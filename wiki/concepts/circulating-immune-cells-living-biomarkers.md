---
title: "Circulating immune cells as living biomarkers"
aliases:
  - living biomarkers
  - cells as living biomarkers
tags:
  - biomarker
  - liquid-biopsy
  - diagnostics
  - PBMC
  - precision-medicine
maturity: emerging
key_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
first_introduced: "Jiménez-Gracia et al. 2026 Nature Medicine"
date_updated: 2026-06-04
related_concepts:
  - inflammation-atlas-circulating-immune-cells
  - patient-classification-reference-embedding-projection
---

## Definition

The concept that peripheral blood immune cells, read at single-cell resolution, act as "living biomarkers": their transcriptional states encode disease identity and activity, so a blood draw can serve as a minimally invasive diagnostic substrate for inflammatory diseases rather than relying on tissue biopsy or single soluble analytes.

## Intuition

A classical biomarker is a static molecule (a protein level, an autoantibody). A "living biomarker" is the cell itself: its activation, migration, cytotoxicity and antigen-presentation programs jointly form a high-dimensional signature that responds to disease state. Circulating immune cells continuously sample the body, so their states reflect systemic inflammation.

## Formal notation

Per-patient diagnosis is inferred from the joint transcriptional state of the circulating immune compartment, e.g. cell-type-resolved expression or embedding profiles fed to a classifier.

## Variants

- Soluble single-analyte biomarkers (classical) versus cell-state (living) biomarkers.
- Gene-level discriminative markers (e.g. CYBA, IFITM1) versus whole-compartment classifiers.

## Comparison

Complements liquid-biopsy concepts in oncology (ctDNA) by using the immune cells themselves as the signal source for inflammatory disease.

## When to use

When framing blood single-cell profiling as a diagnostic or disease-monitoring tool, or when motivating discriminative-gene discovery in PBMCs.

## Known limitations

- Requires demonstrating that circulating states reflect tissue-resident inflammation.
- Clinical use needs prospective, multicenter, batch-controlled validation.

## Open problems

- How faithfully circulating immune programs mirror organ-specific disease activity.
- Standardization needed to deploy single-cell diagnostics in clinics.

## Key papers

- [[papers/interpretable-inflammation-landscape-circulating-immune-cells]] — proposes circulating immune cells as living biomarkers and a PBMC-based disease classifier.

## My understanding

The framing is the paper's clinical thesis: it reframes single-cell atlases from descriptive resources into diagnostic instruments. The bottleneck is generalization across centers/chemistries, not the in-principle information content of the cells.
