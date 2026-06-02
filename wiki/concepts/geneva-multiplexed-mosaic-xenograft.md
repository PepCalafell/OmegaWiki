---
title: "GENEVA multiplexed mosaic xenograft platform"
aliases:
  - GENEVA
  - genetically diverse and endogenously controlled phenotypic variation assay
tags:
  - xenograft
  - scrna-seq
  - functional-genomics
  - platform
  - in_vivo
maturity: emerging
key_papers:
  - systemic-hypoxia-suppresses-solid-tumor-growth
first_introduced: "GENEVA platform (ref 29); applied to hypoxia here (2026)"
date_updated: 2026-06-02
related_concepts: []
---

## Definition

A highly multiplexed in vivo assay in which a pool of genetically diverse cancer cell lines forms mosaic tumors in a shared host, enabling lineage-resolved single-cell transcriptomic and phenotypic (fitness, cell-cycle) profiling of responses to perturbations such as systemic hypoxia.

## Intuition

By assaying many genotypes simultaneously in the same host environment, natural phenotypic heterogeneity is used to correlate molecular changes (e.g. purine-gene expression) with lineage-specific fitness, separating universal from context-specific effects.

## Formal notation

SNP-based deconvolution quantifies each line's abundance pre/post-treatment; fold-change scaled by tumor volume yields a relative fitness score per line.

## Variants

Applied with 20 human cancer lines in NSG mice under 21% vs 8% O2 with 10x 3' scRNA-seq.

## Comparison

An in vivo, single-cell, pooled alternative to one-line-at-a-time xenograft studies; complementary to CRISPR essentiality screens.

## When to use

When dissecting heterogeneous, lineage-dependent responses to a systemic perturbation in vivo.

## Known limitations

Immunocompromised host (NSG) excludes adaptive immunity; correlative fitness inference.

## Open problems

Generalization across host genotypes and perturbations.

## Key papers

- [[systemic-hypoxia-suppresses-solid-tumor-growth]] — Midha, Chew et al., bioRxiv 2026

## My understanding

The platform that revealed heterogeneous hypoxia sensitivity and the purine-fitness correlation in this paper.
