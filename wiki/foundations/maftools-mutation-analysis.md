---
title: "maftools — Bioconductor toolkit for somatic mutation analysis"
slug: maftools-mutation-analysis
domain: "methods / genomics"
status: mainstream
aliases:
  - "maftools"
  - "MAF tools"
  - "Mutation Annotation Format toolkit"
  - "TMB calculator (maftools)"
  - "oncoplot generator"
  - "waterfall plot maftools"
first_introduced: "Mayakonda et al. 2018 Genome Research"
date_updated: 2026-05-25
source_url: "https://bioconductor.org/packages/release/bioc/html/maftools.html"
---

## Definition

A Bioconductor R package for parsing and summarising Mutation Annotation Format (MAF) files. Provides standard outputs: oncoplots / waterfall plots, mutual exclusivity tests, TMB calculation (mutations per megabase), driver gene enrichment, mutation-signature decomposition (COSMIC SBS), and clinical-correlate plotting.

## Intuition

A one-stop toolkit for moving from raw MAF tables to publication-grade somatic mutation summaries with a unified API.

## Formal notation

- TMB = total non-synonymous mutations / exome size in Mb (default exome-size constant 38–40 Mb).
- Standard outputs: `oncoplot`, `mafSummary`, `tmb`, `somaticInteractions`, `oncodrive`, `signatures`.

## Key variants

- TCGAbiolinks pre-prepared MAFs as input.
- Combined with deconstructSigs / SigProfiler for signature analysis.

## Known limitations

- TMB depends on calling pipeline upstream; cross-cohort comparisons are sensitive to filter choices.
- Driver-gene enrichment relies on dN/dS-like assumptions.

## Open problems

- Standardisation of cohort-cross-cohort TMB normalisation.

## Relevance to active research

maftools is the standard SNV summary tool for TCGA cohorts, used in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] for TMB calculation, waterfall plots, and top-mutated-gene comparison between high and low hypoxia groups in TCGA-PAAD.
