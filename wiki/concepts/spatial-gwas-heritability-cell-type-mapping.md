---
title: "Spatial mapping of GWAS heritability to cell types and domains"
aliases: ["spatial heritability mapping", "genetics-to-spatial cell-type mapping", "GWAS-to-spatial-domain"]
tags: [statistical-genetics, spatial-omics, gwas, heritability]
maturity: emerging
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2024"
date_updated: 2026-06-03
related_concepts: [spatial-multiomics-orthogonal-validation, differential-stromal-interactions-skin-cancer]
---

## Definition

A framework that attributes the heritability of a complex trait (from GWAS summary statistics) to specific cell types and spatial domains by overlaying genetic association onto spatial transcriptomics. Spatially-specific marker genes (gene specificity scores) are linked to SNPs by LD/distance, and the cumulative trait heritability captured at each spot/cell/region is tested against baseline SNPs.

## Intuition

GWAS identifies risk SNPs but not where in the tissue or in which cells they act. By projecting heritability onto spatial maps, this approach pinpoints the cellular and microanatomical context where genetic risk is realised (e.g. melanoma risk → melanocytes; cSCC/BCC risk → dysplastic/cornified keratinocytes; fibroblast association across all), connecting heritability to mechanism.

## Formal notation

Per spot s: GSS(s,g) for spatially specific genes; SNP→gene mapping by LD/TSS distance; heritability enrichment via S-LDSC; region/cell-type P by Cauchy aggregation (see [[gsmap-spatial-heritability]]).

## Variants

- Cell-type-level vs spatial-domain-level mapping
- Correlation of GSS with cell-type GWAS P to nominate genetic ligand-receptor pairs (e.g. IL34-CSF1R, LTB-LTBR)

## Comparison

Extends scRNA-seq cell-type heritability enrichment (e.g. LDSC-SEG) by adding spatial domains and neighbourhood context, and by linking association to interactions rather than to isolated cell types.

## When to use

When deeply profiled spatial data and well-powered GWAS are both available and the goal is to interpret heritability mechanistically in tissue context.

## Known limitations

- Depends on spatial reference quality and marker specificity
- LD-based SNP-to-gene mapping inherits assignment error
- Enrichment ≠ causation

## Open problems

- Causal interpretation and regulatory annotation integration
- Power with small spatial cohorts vs large GWAS

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — applies gsMAP to >300,000-individual skin-cancer GWAS, mapping heritability to melanocytes, dysplastic/cornified keratinocytes, and fibroblasts, and to T-cell–melanoma interactions.

## My understanding

The bridge from population genetics to spatial single-cell biology: heritability gets a cellular address, and even an interaction-level interpretation.
