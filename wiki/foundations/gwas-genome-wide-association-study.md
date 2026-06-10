---
title: "Genome-wide association study (GWAS)"
slug: gwas-genome-wide-association-study
domain: genomics
status: mainstream
aliases: [GWAS, genome-wide association studies]
first_introduced: ""
date_updated: 2026-06-10
source_url: ""
---

## Definition

A genome-wide association study (GWAS) scans common genetic variants — chiefly single nucleotide polymorphisms (SNPs) — across many individuals to identify variants statistically associated with a trait or disease. GWAS were enabled by reference variation catalogues (HapMap, 1000 Genomes) combined with advances in statistical analysis.

## Intuition

By profiling common differences across thousands of individuals cheaply, GWAS turned population-scale variation into a discovery engine for trait–variant associations, from height and obesity to complex diseases such as schizophrenia. A large fraction of the associations land in non-coding, regulatory regions rather than in protein-coding sequence.

## Formal notation

Association is typically tested per variant (e.g., logistic/linear regression of phenotype on genotype) with genome-wide significance thresholds (~5×10⁻⁸) to control multiple testing.

## Key variants

- Case–control vs. quantitative-trait GWAS.
- Trans-ethnic and meta-analysis GWAS; polygenic risk scores derived downstream.

## Known limitations

- Most hits are associations, not causal mechanisms; effect sizes are often small.
- "Missing heritability" and difficulty interpreting non-coding hits.

## Open problems

- Mapping GWAS hits to causal regulatory elements and target genes.

## Relevance to active research

[[wealth-discovery-built-human-genome-project]] notes there are now >30,000 papers per year linking SNPs and traits, with a large fraction of associations in once-dismissed non-coding regions. Related: [[hapmap-project]], [[1000-genomes-project]].
