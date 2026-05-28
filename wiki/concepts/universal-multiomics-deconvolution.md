---
title: "Universal multi-omics deconvolution"
aliases:
  - cross-omics deconvolution
  - universal deconvolution framework
tags: [deconvolution, multiomics, methods]
maturity: emerging
key_papers:
  - decode-deep-learning-based-common-deconvolution
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts: [cell-type-abundance-from-bulk-tissue-rnaseq, metabolomics-deconvolution, cell-state-deconvolution]
---

## Definition

A single deconvolution framework that estimates cell-type (or cell-state) abundances from tissue-level data across multiple omics modalities — transcriptomics, proteomics and metabolomics — rather than using a separate, modality-specific algorithm for each. The goal is methodologically consistent composition estimates that can be compared across omics layers and cohorts.

## Intuition

Deconvolution historically followed a specialized paradigm: MuSiC/CIBERSORTx for transcriptomics, scpDeconv for proteomics, RCTD/SPOTlight for spatial, and nothing for metabolomics. Using a different tool per omics introduces method-specific error sensitivities, so abundance comparisons across omics carry unquantifiable systematic biases. A universal framework removes that confound by applying one error model everywhere.

## Formal notation

Estimate proportion vector p for tissue sample x regardless of omics modality m, with a shared architecture f(x; m) trained per dataset but identical in form across m.

## Variants

- Cell-type vs. cell-state targets (same framework, different labels).
- Standard deconvolution (complete reference) vs. relative deconvolution (unknown cell types present).

## Comparison

Versus single-omics tools (MuSiC, CIBERSORTx, scpDeconv): trades bespoke distributional assumptions (Poisson/NB counts) for a distribution-agnostic learned mapping, gaining cross-omics consistency at the cost of needing a trainable model per dataset.

## When to use

When a multi-omics cohort study needs cell-abundance estimates that are directly comparable across transcriptomic, proteomic and metabolomic layers without per-tool calibration.

## Known limitations

Requires a single-cell reference in each omics; metabolomics references remain scarce. Consistency across omics is empirical, not guaranteed.

## Open problems

Extending to additional layers (DNA methylation, spatial) within the same framework; guaranteeing rather than measuring cross-omics consistency.

## Key papers

- [[decode-deep-learning-based-common-deconvolution]] — introduces the concept via DECODE.

## My understanding

The key value proposition for the user's multi-omics cohort work is error-model consistency: comparing immune-cell abundance shifts across transcriptomic vs. proteomic vs. metabolomic cohorts becomes meaningful only when one method underlies all of them.
