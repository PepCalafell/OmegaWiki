---
title: "MeCP2 — Methyl-CpG-Binding Protein 2"
slug: mecp2-methyl-cpg-binding-protein
domain: "biology / epigenetics / neuroscience"
status: mainstream
aliases:
  - "MeCP2"
  - "Mecp2"
  - "methyl-CpG-binding protein 2"
  - "Rett syndrome gene"
  - "mCH/mCA reader"
first_introduced: "Lewis et al. *Cell* 1992"
date_updated: 2026-05-27
source_url: "https://www.uniprot.org/uniprotkb/P51608"
---

## Definition

MeCP2 is the prototypical methyl-CpG-binding protein and a chief reader of both mCG and non-CpG (mCH/mCA) methylation marks. Through its methyl-binding domain (MBD), MeCP2 recognises symmetrically methylated CpG and methylated CpA in mammalian neurons, recruits NCoR/SMRT and HDAC co-repressors, and modulates neuronal gene expression. Loss-of-function MECP2 mutations cause Rett syndrome.

## Intuition

CpG islands store epigenetic state; MeCP2 reads it. In post-mitotic neurons, MeCP2 also reads the unusually high mCA load that accumulates postnatally — making it the canonical link between non-CpG methylation and transcriptional silencing in the mammalian brain. Loss of MeCP2 → derepression of long genes with high mCA load → Rett syndrome phenotype.

## Formal notation

- Binding: 5mCpG ≫ 5mCpA ≫ 5mCpT/5mCpC (with affinity proportional to mCH density at gene body).
- Co-repressor recruitment: NCoR/SMRT → HDAC3 → deacetylation of nearby histones.
- Brain-specific abundance: ~10⁷ molecules per neuron, comparable to histone H1.
- mCA-dependent gene silencing model: long genes with high gene-body mCA become repressed in mature neurons.

## Key variants

- **MeCP2_e1 / MeCP2_e2**: alternative N-terminal isoforms.
- **Rett-associated mutants**: R106W, R133C, T158M, R168X (loss-of-function variants).
- **Duplications** (MECP2 duplication syndrome): gain-of-dose phenotype.

## Known limitations

- Genome-wide ChIP-seq mostly mirrors mC density — limited locus-resolution gain over methylome data.
- mCH reading is brain-specific; outside neurons MeCP2's role is restricted to mCG.

## Open problems

- Quantifying MeCP2 occupancy in single neurons / single spatial pixels.
- Direct in vivo coupling of mCA accumulation, MeCP2 binding, and gene silencing in spatial context.

## Relevance to active research

MeCP2 expression in space and time was mapped in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], with higher expression in E13 vs E11 embryonic brain and prominent expression in the P21 cortex — consistent with the postnatal onset of mCA accumulation that MeCP2 reads. The paper directly couples mCA spatial patterns with gene expression at MeCP2-target loci (Cux1, Bcl11b).
