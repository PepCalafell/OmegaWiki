---
title: "Patient classification by reference-embedding projection"
aliases:
  - patient-level reference-mapping classifier
  - embedding-pseudobulk patient classifier
tags:
  - reference-mapping
  - classification
  - diagnostics
  - single-cell
  - majority-voting
maturity: emerging
key_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
first_introduced: "Jiménez-Gracia et al. 2026 Nature Medicine"
date_updated: 2026-06-04
related_concepts:
  - scrna-atlas-as-reference-projection
  - circulating-immune-cells-living-biomarkers
---

## Definition

A framework that turns a single-cell reference atlas into a patient-level diagnostic by (1) projecting a query patient's cells into the reference embedding (scANVI), (2) forming a per-cell-type pseudobulk in embedding space by averaging each patient's cells, (3) training one classifier per cell type to predict disease, and (4) resolving the patient's diagnosis by majority voting across cell-type classifiers.

## Intuition

Instead of classifying individual cells, treat each patient as an ensemble of cell-type embedding profiles. Each cell type "votes" for a diagnosis; the consensus is robust even when some cell types (e.g. plasma, UTC) classify poorly. The reference embedding provides a common coordinate system so unseen patients can be mapped and diagnosed.

## Formal notation

For patient p and cell type c, embedding pseudobulk z_{p,c} = mean of scANVI latents over p's cells of type c; classifier g_c predicts disease from z_{p,c}; final label = mode over c of g_c(z_{p,c}).

## Variants

- Evaluation scenarios: cross-validation (S1), unseen patients (S2), unseen studies (S3).
- Centralized single-chemistry training to reduce batch confounding.
- Integration backbone: scANVI vs Harmony/Symphony vs scGen vs scPoli.

## Comparison

Extends [[concepts/scrna-atlas-as-reference-projection]] from cell-type annotation to patient-level disease diagnosis, and complements existing patient classifiers (scPoli, MultiMIL) by stress-testing unseen-study generalization.

## When to use

When deploying an atlas as a diagnostic that must classify whole patients from query single-cell data.

## Known limitations

- Generalization collapses across unseen studies due to batch effects (S3).
- Requires label transfer quality and sufficient cells per cell type.

## Open problems

- Achieving robust unseen-study generalization without single-chemistry centralization.
- Whether linear backbones (Harmony) beat VAEs when no query labels are available for tuning.

## Key papers

- [[papers/interpretable-inflammation-landscape-circulating-immune-cells]] — introduces the embedding-pseudobulk majority-voting patient classifier and its three-scenario evaluation.

## My understanding

The novelty is using the *embedding* (not gene space) pseudobulk per cell type plus majority voting as a robust aggregator. The honest negative result on unseen studies — and its recovery on a centralized dataset — is what makes the framework credible and points to batch standardization as the real clinical bottleneck.
