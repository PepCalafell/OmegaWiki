---
title: "Skin-cancer GWAS heritability maps spatially to melanocytes, dysplastic/cornified keratinocytes, and fibroblasts"
slug: gsmap-skin-cancer-heritability-cell-type-mapping
status: supported
confidence: 0.75
tags: [gwas, heritability, spatial-omics, skin-cancer, fibroblast]
domain: statistical genetics
source_papers:
  - integrating-12-spatial-single-cell-technologies
evidence:
  - source: integrating-12-spatial-single-cell-technologies
    type: supports
    strength: strong
    detail: "gsMAP applied to GWAS (SCC/BCC: Seviiri 2022; melanoma: Landi 2020, 30,143 cases) mapped heritability to spatial cells: melanoma→melanocytes & KC-differentiating; cSCC→KC-dysplastic; BCC→KC-hair; KC-cornified shared; fibroblast strong across all. Tumor-region spots had highest spatial heritability; genome-wide top signals matched melanoma markers MITF, TYR, MX2. (p.13-14, Fig 8)"
conditions: "GWAS summary statistics from >300,000 individuals projected onto Visium/CosMx."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Using gsMAP, skin-cancer GWAS heritability localises to specific spatial cell types — melanoma risk to melanocytes and differentiating keratinocytes, cSCC/BCC risk to dysplastic/hair/cornified keratinocytes — with fibroblasts showing consistent association across all three, and tumour-region spots capturing the strongest spatial heritability.

## Evidence summary

Spatial heritability mapping with Cauchy-aggregated significance per cell type/region; genome-wide concordance with canonical melanoma markers (MITF, TYR, MX2). (p.13-14)

## Conditions and scope

Large GWAS but small spatial cohort; LD-based SNP-to-gene mapping.

## Counter-evidence

Enrichment, not causation; reference-quality dependent.

## Linked ideas

## Open questions

Whether keratinocyte-mediated cis-regulation explains some melanoma risk loci.
