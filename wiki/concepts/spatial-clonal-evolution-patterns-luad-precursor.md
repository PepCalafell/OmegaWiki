---
title: "Spatial clonal evolution patterns from lung precursor to invasive LUAD"
aliases:
  - spatial clonal architecture LUAD precursor
  - patient-specific clonal pattern precursor LUAD
  - shared vs distinct clones precursor invasive
  - LUAD evolutionary pattern 1a
  - LUAD evolutionary pattern 1b
  - LUAD evolutionary pattern 2
  - spatial phylogeny lung precursor
  - clonal sharing AAH AIS LUAD
  - branched vs linear LUAD progression
  - synchronous precursor-invasive evolution
  - SpatialInferCNV phylogeny
  - lung precursor-invasive clonal heterogeneity
tags:
  - lung
  - luad
  - precursor
  - clonal-evolution
  - phylogeny
  - spatial-genomics
maturity: emerging
key_papers:
  - multimodal-spatial-omics-reveal-co-evolution
  - mapping-inflammatory-origins-lung-cancer
first_introduced: "2026"
date_updated: 2026-06-03
related_concepts:
  - field-cancerization-clonal-expansion-normal-tissue
---

## Definition

A three-pattern classification of clonal relationships between paired precursor (AAH, AIS) and invasive (LUAD) lesions, derived from [[foundations/spatialinfercnv-spatial-cna]] applied to Visium ST data and validated by paired snRNA-seq and WES.

## Variants

- **Pattern 1a (n=5)**: all precursor clones are present in the paired LUAD, which acquired additional subclones. Linear progression. KRAS mutations notably **absent**.
- **Pattern 1b (n=13, most common)**: precursor and invasive share some clones but each harbors stage-specific clones. Mixed evolution. EGFR/KRAS/MET driver mutations predominantly enriched here.
- **Pattern 2 (n=5)**: precursor and invasive clones are entirely disjoint — parallel or polyclonal origin within the same field.
- One case (P22) chromosomally stable; one (P7) uncategorized (two LUADs).

## When to use

When interpreting bulk WES or single-region biopsies of synchronous precursor+invasive lesions, the three-pattern framework warns that sampling bias may misrepresent evolutionary inference.

## Known limitations

Visium spots contain mixtures of tumor and non-tumor cells, lowering CNA inference fidelity; future spatial DNA-seq (spot- or single-cell SNV/CNA) is needed to validate phylogenies.

## Key papers

- [[papers/multimodal-spatial-omics-reveal-co-evolution]] — Peng et al. 2026 Cancer Cell, defines the three patterns over 25 patients with paired precursor and LUAD lesions.

## Open problems

- Why are KRAS mutations selectively absent from pattern 1a but enriched in pattern 1b?
- Can pre-resection biopsy stratify patients to a pattern, informing surveillance versus surgery?
- How do epithelial-proinflammatory niches map onto each pattern's clonal topology?
