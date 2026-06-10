---
title: "scDblFinder — doublet detection for single-cell data"
slug: scdblfinder-doublet-detection
domain: "methods / single-cell / quality control"
status: mainstream
aliases:
  - scDblFinder
  - scDblFinder doublet detection
first_introduced: "Germain et al. 2021, scDblFinder (R/Bioconductor)"
date_updated: 2026-06-10
source_url: "https://bioconductor.org/packages/scDblFinder"
---

## Definition

scDblFinder is an R/Bioconductor tool that identifies and removes doublets (droplets containing two or more cells) in single-cell RNA-seq data. It generates artificial doublets by combining real cells, then trains a classifier on the real-plus-artificial mixture to score each barcode's doublet likelihood.

## Intuition

A doublet looks like a blend of two transcriptomes; by synthesizing such blends from observed cells you create labeled positives and learn to spot the real ones, removing artifactual "hybrid" clusters before downstream analysis.

## Key variants

- Related simulation-based tools include DoubletFinder and Scrublet, which give concordant results in practice.

## Known limitations

- Homotypic doublets (two cells of the same type) are hard to detect because they resemble singlets.
- Detection rate depends on assumed doublet rate, which scales with loaded cell number.

## Relevance to active research

A standard QC step in droplet scRNA-seq pipelines; removing doublets prevents spurious "intermediate" or mixed-lineage clusters that would otherwise be misinterpreted as novel cell states.
