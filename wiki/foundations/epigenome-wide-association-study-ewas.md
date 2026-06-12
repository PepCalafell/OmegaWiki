---
title: "Epigenome-wide association study (EWAS)"
slug: epigenome-wide-association-study-ewas
domain: methods
status: mainstream
aliases: ["EWAS", "epigenome-wide association study"]
first_introduced: "2011"
date_updated: 2026-06-12
source_url: "https://www.ewascatalog.org"
---

## Definition

An EWAS systematically tests association between epigenetic marks (most commonly CpG DNA methylation measured on arrays) across the genome and a phenotype, trait, or exposure, analogous to a GWAS but for the methylome.

## Intuition

By scanning hundreds of thousands of CpG sites, an EWAS identifies loci whose methylation correlates with a condition (e.g. vaccination, cytokine response), after controlling for confounders such as age, sex, batch, and cell composition.

## Formal notation

Per-CpG regression (often linear mixed-effects with subject random effects for longitudinal designs); significance by FDR < 0.05, with a common suggestive threshold P < 1×10⁻⁵. M-values (log2(β/(1−β))) are used for modeling.

## Key variants

Cross-sectional vs longitudinal EWAS; differential methylation of positions (DMP) vs regions (DMR); meta-EWAS.

## Known limitations

Confounding by cell-type composition, tissue specificity (whole blood masks cell-specific signals), array coverage (EPIC covers ~3% of CpGs), and reverse causation.

## Open problems

Distinguishing causal from reactive methylation changes; integrating EWAS with genetics (mQTL) and transcription.

## Relevance to active research

Core analytical framework for identifying BCG-induced methylation changes and methylation–cytokine associations; results curated in the EWAS Catalog for cross-trait lookup.
