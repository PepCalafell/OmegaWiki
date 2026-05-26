---
title: "Epigenetic regulation of AHR and its target genes — DNA methylation, histone modifications, microRNAs as a major axis of AHR context specificity"
aliases:
  - AHR epigenetic regulation
  - AHR promoter methylation
  - AHRR methylation cg05575921
  - CYP1A1 enhancer methylation
  - AHR target gene epigenetics
  - DNA methylation of AHR pathway
  - histone modifications AHR
  - miRNA regulation of AHR
  - HK2 AHR demethylation
  - TET2 NT5E demethylation
  - AHR tumour suppressor methylation
  - smoking AHRR hypomethylation
tags:
  - AHR
  - epigenetics
  - DNA-methylation
  - histone-modifications
  - microRNA
  - AHRR
  - CYP1A1
  - TET2
  - HK2
  - smoking
  - cancer-epigenetics
maturity: active
key_papers:
  - complex-biology-aryl-hydrocarbon-receptor-activation
first_introduced: ""
date_updated: 2026-05-26
related_concepts:
  - ahr-context-specificity-pleiotropy
  - ahr-canonical-signalling-pathway
  - ahr-cyp1a1-negative-feedback-clearance
---

## Definition

Layered epigenetic control of (a) AHR itself (promoter methylation, histone modifications, miRNA targeting of AHR mRNA) and (b) its target genes (enhancer/promoter methylation of CYP1A1/CYP1B1/AHRR/NRF2/tumour suppressors). These epigenetic marks determine whether AHR is expressed, whether its targets are inducible, and which target genes respond to ligand activation in each cell.

## Intuition

Even when AHR is expressed and a ligand is present, the receptor cannot drive transcription if the relevant XRE is buried in methylated CpG islands or in repressive chromatin. Cell-type-specific methylation/histone landscapes therefore act as a *permission gate* on AHR signalling. Conversely, AHR can itself shape this landscape (via TET2 induction, recruitment of HDACs, CPS1-driven H1K34 carbamylation).

## Formal notation

Documented epigenetic events:

**On AHR itself**
- AHR promoter hypermethylation → SP1 cannot bind → AHR silenced. Observed in 33% of ALL patients and multiple lymphoid + solid cell lines.
- HDAC inhibitors (TSA, butyrate, panobinostat, vorinostat) restore AHR expression in many but not all contexts (MCF-7 refractory).
- miR-124, miR-375, miR-548, miR-122 directly target the AHR 3'UTR.

**On AHR target genes**
- CYP1A1 enhancer methylation blocks AHR binding; differential methylation explains cell-line-specific CYP1A1 inducibility.
- TCDD induces H3K4me3/H4Ac at the CYP1A1 promoter (active marks).
- AHRR methylation: hypomethylated by smoking (lung); hypermethylated and silenced in many other cancers.
- AHR-mediated promoter hypermethylation silences tumour suppressors p16(INK4a), p53, BRCA1.
- HK2 is an AHR target that drives AHR promoter demethylation (positive feedback).
- AHR-Kyn binding to TET2 promoter induces TET2 → NT5E/CD73 demethylation → adenosine production in Tregs/B cells; downregulated in SLE.
- AHR-KLF6 binding to NC-XREs recruits CPS1 → homocitrullination of H1K34 → PAD2 induction.

## Variants

- **Cell-line-specific methylation landscapes** dominate the literature — pan-cancer / pan-tissue maps of AHR-relevant CpGs are still incomplete.
- **Direct vs indirect AHR-driven methylation**: AHR-recruited DNMTs (direct) vs AHR-induced metabolic changes that alter methylation (indirect, e.g. via HK2).

## Comparison

- Versus pure-TF view: highlights why AHR antagonism alone is insufficient — the epigenetic landscape primed by chronic AHR activity persists even after acute inhibition.

## When to use

- When interpreting AHR-pathway methylation biomarkers (AHRR cg05575921 for smoking; AHR promoter methylation in ALL).
- When integrating EPIC methylation arrays with scRNA-seq atlases for cancer biology.
- When considering AHR-pathway therapy combinations with DNMT or HDAC inhibitors.

## Known limitations

- Most evidence rests on bulk DNA from blood or cell lines. Single-cell methylation resolution of AHR loci is still rare.
- Cause-vs-consequence ambiguity: does AHR drive the methylation pattern, or vice versa?

## Open problems

- Reconciling opposite-direction smoking-related methylation at AHRR (hypo) vs CYP1A1 (hyper).
- Pan-cancer integrative atlas of AHR-pathway methylation, expression, and AHR activity.
- Mechanism of HK2-driven AHR promoter demethylation.

## Key papers

- [[papers/complex-biology-aryl-hydrocarbon-receptor-activation]] — Opitz et al. 2023 Biochem Pharmacol §10.

## My understanding

Highly relevant to the hypoxia/skin work in my thesis: AHRR methylation biomarkers (cg05575921) overlap directly with smoking-driven epigenetic age acceleration, and AHR-pathway methylation may be a mediator of microenvironmental signals (hypoxia, smoke, microbial metabolites) in skin tumourigenesis. Worth probing AHR-pathway methylation in any EPIC array in my project.
