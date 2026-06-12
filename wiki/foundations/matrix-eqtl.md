---
title: "Matrix eQTL"
slug: matrix-eqtl
domain: methods
status: mainstream
aliases: ["Matrix eQTL", "MatrixEQTL"]
first_introduced: "2012"
date_updated: 2026-06-12
source_url: "https://github.com/andreyshabalin/MatrixEQTL"
---

## Definition

Matrix eQTL is an R package for ultra-fast association testing between large genotype matrices and molecular phenotypes (expression, methylation, cytokine QTL), using efficient large-matrix operations.

## Intuition

It enables genome-scale QTL mapping (e.g. SNP→cytokine, SNP→methylation) in seconds-to-minutes by vectorizing the per-feature linear regressions.

## Formal notation

Linear (or ANOVA) model per SNP–phenotype pair with covariate adjustment; supports cis/trans distinction and FDR control.

## Key variants

Linear, ANOVA, and linear-cross models; cis vs trans testing.

## Known limitations

Assumes additive linear effects; no nonlinear or interaction modeling by default.

## Open problems

Scalable mapping of context-specific and interaction QTLs.

## Relevance to active research

Used to identify cytokine-QTLs (SNP→IFN-γ) and SNP–methylation pairs feeding bidirectional mediation analysis.
