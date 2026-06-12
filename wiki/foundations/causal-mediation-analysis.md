---
title: "Causal mediation analysis"
slug: causal-mediation-analysis
domain: methods
status: mainstream
aliases: ["mediation analysis", "causal mediation analysis", "mediation R package"]
first_introduced: "2014"
date_updated: 2026-06-12
source_url: "https://cran.r-project.org/package=mediation"
---

## Definition

Causal mediation analysis decomposes the effect of an exposure on an outcome into a direct effect and an indirect effect transmitted through an intermediate variable (mediator), under stated identification assumptions.

## Intuition

It asks not just whether X affects Y, but how much of that effect "flows through" a mediator M (e.g. how much of a SNP's effect on cytokine response is carried by a DNA-methylation change).

## Formal notation

For y = f(x, m) and m = g(x), estimates average causal mediation effect (ACME) and average direct effect (ADE); proportion mediated = ACME / total effect. The `mediation` R package (Tingley et al.) provides estimation and inference.

## Key variants

Single-mediator vs multiple-mediator; bidirectional mediation (testing both directions M↔outcome).

## Known limitations

Requires no-unmeasured-confounding assumptions; observational in silico mediation cannot prove causality; direction can be ambiguous.

## Open problems

Robust mediation with high-dimensional, correlated omics mediators.

## Relevance to active research

Used for bidirectional mediation between SNPs, DNA-methylation changes, and trained-immunity cytokine changes, inferring in silico causal direction.
