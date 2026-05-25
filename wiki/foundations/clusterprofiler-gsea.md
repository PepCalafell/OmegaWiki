---
title: "clusterProfiler — R package for functional enrichment / GSEA"
slug: clusterprofiler-gsea
domain: "methods / genomics-enrichment"
status: mainstream
aliases:
  - "clusterProfiler"
  - "clusterProfiler R package"
  - "GSEA clusterProfiler"
  - "enrichGO clusterProfiler"
  - "Yu Guangchuang clusterProfiler"
  - "GSEA KEGG MSigDB clusterProfiler"
first_introduced: "Yu et al. 2012 OMICS; major redevelopment in clusterProfiler 4.x (Yu 2021 Innovation)"
date_updated: 2026-05-25
source_url: "https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html"
---

## Definition

A widely used R/Bioconductor package for functional enrichment analysis: over-representation tests (`enrichGO`, `enrichKEGG`, `enricher`) and ranked-list Gene Set Enrichment Analysis (`gseGO`, `gseKEGG`, `GSEA`), with native plotting (dotplot, ridgeplot, GSEA running-score plots).

## Intuition

clusterProfiler unifies functional enrichment APIs across ontologies (GO, KEGG, MSigDB, Reactome) and supports both ORA and GSEA paradigms with a consistent input/output shape.

## Formal notation

- Inputs: ranked gene list (gene → metric) for GSEA; gene set + background for ORA.
- GSEA: ES, NES, p-value, q-value, permutations parameter (commonly 1000).
- Typical significance: |NES| > 1, FDR/q < 0.25, p < 0.05.

## Key variants

- `fgsea` provides a faster GSEA backend; clusterProfiler can wrap it.
- ReactomePA, DOSE — companion packages.

## Known limitations

- GSEA depends heavily on ranking metric choice (log2FC vs Wald stat vs t-stat).
- Default FDR threshold of 0.25 is permissive.

## Open problems

- Composite or hierarchical enrichment correction across overlapping gene sets.

## Relevance to active research

clusterProfiler is the workhorse for GSEA reporting in TCGA-style transcriptomic studies. Used in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] for GSEA between macrophage clusters 1 and 2, and between high vs low hypoxia groups in TCGA-PAAD.
