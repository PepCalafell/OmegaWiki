---
title: "Statistical necessity of enrichment for rare cell types in single-cell DE"
aliases:
  - "rare cell type enrichment requirement"
  - "pseudobulk power limit for rare populations"
tags: [single-cell, rna-seq, power-analysis, experimental-design, rare-cell-types]
maturity: emerging
key_papers:
  - depower-approximate-power-analysis-deseq2
first_introduced: "Gorin, Guruge & Goodman 2026 (DEPower)"
date_updated: 2026-06-03
related_concepts: [analytical-power-analysis-deseq2-model]
---

## Definition

The design principle, made quantitative by analytical DESeq2 power analysis, that standard "unbiased" single-cell RNA-seq cannot reach stringent differential-expression significance for rare cell populations at feasible sample sizes — so cell-type enrichment (sorting, selective capture) is effectively mandatory.

## Intuition

A rare cell type contributes few cells per sample, so its pseudobulk expression and effective information are low, inflating the standard error of the log-fold change. Once genome-wide multiple-testing correction is applied, the required number of biological replicates balloons into the dozens — often cost-prohibitive — unless the population is enriched first.

## Formal notation

Worked example: a cell type at 1% of 10,000 cells with average expression >0.1 molecules/cell gives pseudobulk expression ≈10; detecting \(\log_2\mathrm{FC}=1\) at nominal \(p=0.05\) needs ~6 samples/condition, rising to 28 (Bonferroni) or 22 (BH, \(q=0.1\)) across ~10,000 genes.

## Variants

- Enrichment strategies: FACS/MACS sorting, antibody-based capture, nucleus enrichment.

## Comparison

- Contrasts with the common assumption that deeper sequencing or more cells (not more biological replicates) solves rare-population DE.

## When to use

- Planning single-cell/single-nucleus studies whose biological question centers on a rare population.

## Known limitations

- Conclusion follows from order-of-magnitude assumptions; exact thresholds depend on dispersion and effect size.

## Open problems

- Quantifying the power gain from each enrichment strategy relative to its cost and bias.

## Key papers

- [[papers/depower-approximate-power-analysis-deseq2]]

## My understanding

A concrete, sobering design rule for single-cell work on rare cell types — directly relevant to any plan that targets a minority population without enrichment.
