---
title: "scpDeconv — domain-adversarial proteome deconvolution"
slug: scpdeconv-proteomics-deconvolution
domain: methods
status: mainstream
aliases:
  - scpDeconv
first_introduced: "2023"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1038/s42256-023-00737-y"
---

## Definition

scpDeconv is a deep domain-adversarial neural network for deconvolving cell-type mixtures in tissue proteome profiling. It uses single-cell proteomics as reference and a domain-adversarial component to align single-cell-derived training data with bulk tissue proteomes.

## Intuition

Single-cell and bulk proteomes differ systematically (domain shift). A domain-adversarial network learns features that are predictive of composition yet indistinguishable between source (single-cell-derived) and target (bulk) domains, transferring the deconvolution model across the gap.

## Formal notation

Feature encoder trained jointly with a label predictor (proportions) and a domain discriminator via gradient reversal, so encoded features become domain-invariant.

## Key variants

None widely established.

## Known limitations

- Proteomics-specific; not designed for transcriptomic or metabolomic data.
- Single-omics.

## Open problems

Extending adversarial alignment to a unified multi-omics setting.

## Relevance to active research

The proteomics-specific predecessor whose adversarial-alignment idea is generalized by universal multi-omics frameworks such as DECODE; a standard proteomic deconvolution baseline.
