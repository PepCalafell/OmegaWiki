---
title: "Relative transcriptional abundance"
aliases:
  - relative transcriptional abundance
tags:
  - epigenetics
  - transcription
  - chromatin-accessibility
  - macrophage
  - gene-regulation
maturity: emerging
key_papers:
  - integrated-time-series-analysis-high-content
first_introduced: "Traxler et al. 2025 Cell Systems"
date_updated: 2026-06-04
related_concepts:
  - epigenetic-potential-macrophage
---

## Definition
Relative transcriptional abundance is the state in which a gene's transcription level exceeds what is typically expected from genes with comparable promoter chromatin accessibility — i.e., gene expression higher than predicted from promoter ATAC-seq signal. It is the opposite divergence direction from [[epigenetic-potential-macrophage]].

## Intuition
Some immune genes are transcribed at high levels despite only moderate promoter accessibility, implying that mechanisms beyond promoter opening (e.g. enhancer activity, Pol II elongation, mRNA stability) drive their abundance. This provides a second, complementary path to rapid immune-gene induction.

## Formal notation
For gene g with expression E(g) and promoter accessibility A(g): relative transcriptional abundance when E(g) ≫ expected(E | A) among genes of similar accessibility. Genes can transition between epigenetic potential and relative transcriptional abundance over a stimulation time course.

## Variants
Baseline vs stimulus-induced relative transcriptional abundance; transient (cluster B) vs sustained (cluster A) abundance over the Listeria time course.

## Comparison
Mirror image of epigenetic potential; together they parameterize the decoupling between chromatin accessibility and transcription.

## When to use
To flag genes whose expression cannot be explained by promoter accessibility alone, prompting investigation of post-accessibility regulation.

## Known limitations
Relative to a reference population; promoter-centric; does not by itself identify the responsible mechanism.

## Open problems
Mechanistic drivers (elongation, splicing, stability) of relative transcriptional abundance in immune activation.

## Key papers
- [[papers/integrated-time-series-analysis-high-content]] — defines relative transcriptional abundance and tracks transitions with epigenetic potential during Listeria response.

## My understanding
A useful counterpart to poised-chromatin thinking: high expression at modest accessibility is itself informative and points to non-promoter regulatory layers.
