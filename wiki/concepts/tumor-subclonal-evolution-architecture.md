---
title: "Tumor subclonal evolution architecture"
aliases:
  - "subclonal architecture"
  - "tumor subclonal architecture"
  - "subclonal phylogeny"
  - "monoclonal vs polyclonal tumor"
  - "trunk vs branch CNAs"
  - "evolutionary timing of mutations"
  - "early vs late tumor mutations"
  - "tumor phylogenetic reconstruction"
  - "PhyloWGS"
  - "tumor clonal evolution"
  - "intratumor clonal heterogeneity"
tags:
  - tumor-evolution
  - phylogenetics
  - subclonal
  - WGS
  - clonality
  - prostate-cancer
maturity: stable
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
  - tumour-hypoxia-driving-genomic-instability-tumour
first_introduced: "Nik-Zainal 2012 Cell (BRCA); Espiritu 2018 Cell (PRAD); Gerstung et al. 2017 PCAWG; Suvac, Ashton & Bristow 2025 Nat Rev Cancer (review)"
date_updated: 2026-05-13
related_concepts: []
---

## Definition

Tumor subclonal evolution architecture is the inferred phylogenetic structure of subclonal populations within a tumor, reconstructed from variant allele frequencies and copy-number profiles in bulk or multi-region sequencing. Key derived quantities include: number of subclones, monoclonal vs polyclonal status, *trunk* mutations (present in all subclones, hence early in evolution) vs *branch* mutations (present in subclones, hence late), and the subclonal expansion timeline.

## Intuition

A tumor is not a single monolithic clone but a population. Reconstructing the genealogy of that population — which mutations occurred first (trunk) and which arose later in branches — reveals what selective pressures acted *early* in tumor development versus *late*. Mutations preferentially placed in the trunk are interpreted as drivers of tumor initiation; mutations preferentially in branches reflect later adaptation (e.g. metastatic seeding, drug resistance). When 99% of hypoxia-associated CNAs land in the trunk ([[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], O/E=73, P=6.71×10⁻²⁴⁹), it means hypoxia is acting as an *early* selective pressure.

## Formal notation

- Cellular prevalence (CP): fraction of tumor cells carrying a mutation, inferred from VAF + copy-number + purity
- Trunk: CP ≈ 1 (in all subclones)
- Branch: CP < 1 (in some subclones only)
- Phylogenetic reconstruction tools: PhyloWGS, PyClone, DPClust, SciClone
- Monoclonal vs polyclonal: typically defined by number of detected subclones (1 vs >1)
- Trunk-bias enrichment: O/E ratio = (observed CNAs in trunk) / (expected under uniform distribution)

## Variants

- Multi-region (multi-sample) sequencing: enables higher-confidence phylogeny but rarely available
- Single-cell DNA sequencing: direct phylogeny without inference
- Mutational signatures by phase: SBS signatures change between trunk and branch (cf. PCAWG mutational-signature-trajectory work)

## Comparison

| Method | Resolution | Cost | Cohort scale |
|---|---|---|---|
| Bulk WGS + phylogeny inference | subclone-level (4–10 subclones) | low | thousands |
| Multi-region bulk WGS | subclone-level + spatial | medium | hundreds |
| Single-cell DNA-seq | per-cell | high | tens |

## When to use

- Mapping mutations / CNAs to trunk vs branch evolutionary timing
- Identifying *early* drivers vs *late* adaptive events
- Linking microenvironmental selective pressure (hypoxia, immune editing) to evolutionary timing
- Risk stratification: polyclonal tumors are typically more aggressive

## Known limitations

- Phylogeny reconstruction depends on tumor purity, mutation rate, copy-number complexity — accuracy degrades for low-purity or high-CNA tumors
- Bulk WGS can miss small subclones (< 5–10% prevalence)
- Trunk/branch annotations may be wrong for individual mutations even when overall phylogeny is correct
- Most public cohorts (TCGA) are single-region — phylogeny is inferential

## Open problems

- Spatial subclonality: where in the tumor each subclone resides
- Coupling phylogeny to microenvironmental data (hypoxia maps, immune infiltration)
- Validating bulk-derived phylogenies with single-cell data at scale
- How the immune system shapes branch-timed mutations through immune editing

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — 191 PCa tumors with reconstructed subclonal architecture; 99% of hypoxia-associated CNAs are in trunk

## My understanding

The trunk/branch dichotomy is one of the most powerful conceptual tools to interpret tumor genomics functionally. Bhandari et al. 2019 makes hypoxia an *early* event — meaning the molecular features it co-selects (PTEN loss, mutant TP53) become fixed at the population level rather than arising de novo in subclones. For HypoxiaVERSE, this matters because it implies hypoxia signatures are reading population-level features established early, not late adaptations.
