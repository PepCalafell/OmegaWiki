---
title: "HGNC — HUGO Gene Nomenclature Committee gene symbols"
slug: hgnc-gene-nomenclature-standard
domain: genomics / annotation
status: mainstream
aliases:
  - HGNC
  - HUGO Gene Nomenclature Committee
  - HGNC gene symbols
first_introduced: "HGNC (genenames.org); Seal et al. 2023 NAR"
date_updated: 2026-05-28
source_url: "https://www.genenames.org"
---

## Definition

HGNC is the authority that assigns unique, stable, approved symbols and names to human genes. Aligning expression data to HGNC-approved symbols gives a canonical, one-symbol-per-gene vocabulary, in contrast to raw annotations (e.g., GENCODE/Ensembl) where a single gene symbol can map to multiple Ensembl IDs via haplotypes, patches, or pseudoautosomal regions.

## Intuition

If you want one input channel per gene, you need exactly one canonical name per gene. HGNC provides that canonical list, removing one-to-many symbol ambiguity that would otherwise create duplicate/conflicting channels.

## Formal notation

n/a (controlled vocabulary).

## Key variants

- HGNC approved symbols vs Ensembl/GENCODE identifiers.

## Known limitations

- Symbol revisions over time; cross-mapping legacy datasets requires care.

## Open problems

- Stable cross-annotation mapping across releases and species.

## Relevance to active research

AlphaCell filters its input to a definitive 19,253 protein-coding genes aligned to HGNC, establishing a strict bijective gene→model-channel mapping that underpins its "informational completeness" argument.
