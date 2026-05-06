---
title: "PU.1 / SPI1 — master transcription factor of myeloid lineages"
slug: spi1-pu1-master-tf
domain: cell biology / immunology / transcriptional regulation
status: mainstream
aliases:
  - "PU.1"
  - "SPI1"
  - "Spi1"
  - "Sfpi1"
  - "SFFV proviral integration 1"
  - "purine-rich box-1 binding protein"
  - "myeloid lineage-determining transcription factor"
  - "master macrophage TF"
  - "ETS family transcription factor SPI1"
first_introduced: "Klemsz 1990 (PU.1 cloning); Scott 1994 (PU.1 KO myeloid arrest); reviewed across the field"
date_updated: 2026-05-06
source_url: ""
---

## Definition

PU.1 (encoded by *SPI1*) is an ETS-family transcription factor and the master regulator of myeloid (monocyte / macrophage / granulocyte / dendritic cell) and B-cell lymphoid differentiation. It binds purine-rich GGAA core motifs (and extended GGAAGT) and sets up the macrophage enhancer landscape together with cMAF and IRF8. PU.1 is required for emergence of all macrophage lineages — embryonic (yolk-sac EMP-derived) and adult (HSC-derived) — and acts hierarchically with tissue-specific lineage-determining factors (LDFs) such as SALL1, ID3, PPARγ, SPI-C, GATA6 to specify TRM identity.

## Intuition

PU.1 establishes the *core macrophage program* — cells expressing PU.1 are committed to myeloid identity and become permissive to LDF-driven tissue specialization. PU.1 dose matters: high levels favor macrophages, lower levels favor B cells. PU.1 collaborates with cMAF and IRF8 in macrophages and with EBF1 in B cells to dictate cell-fate divergence. PU.1 KO mice have a complete block in macrophage and granulocyte production.

## Formal notation

- Gene: *SPI1* (PU.1) — chromosome 11p11
- Family: ETS (E-twenty-six) transcription factor family
- DNA-binding: ETS domain → purine-rich GGAA / GGAAGT motif
- Protein partners: IRF8 (forms PU.1-IRF8 heterodimer at composite ETS-IRF elements), cMAF, C/EBPα, RUNX1
- Hierarchy: PU.1 (core) → tissue-specific LDFs (SALL1, ID3, PPARγ, SPI-C, GATA6, NFATc1)
- KO phenotypes:
  - *Spi1⁻/⁻ mouse*: complete loss of macrophages, granulocytes, B cells; embryonic lethal
  - Conditional *Spi1*-KO in HSC: arrests myeloid differentiation
- Disease relevance:
  - PU.1 dysregulation in AML
  - SPI1 SNP polymorphisms increase Alzheimer's risk via microglial regulation
  - PU.1 binding occupies most macrophage enhancers (Lavin 2014; Gosselin 2014)

## Key variants

- PU.1-IRF8 cooperative binding: extends macrophage enhancer specificity beyond ETS-only sites.
- PU.1 phosphorylation: modulates binding affinity and partner choice.
- SPI-B (homologue): partial overlap in B-cell function; not relevant in macrophages.

## Known limitations

- PU.1 is required *throughout* macrophage life — distinguishing developmental from maintenance roles requires conditional / tunable systems.
- Cross-species conservation is high but binding motif preferences differ subtly between mouse and human.
- ChIP-seq for PU.1 captures binding sites but not necessarily *active* regulation; integration with ATAC-seq and RNA-seq is needed.

## Open problems

- Mechanism of PU.1-IRF8 cooperative occupancy at composite elements vs solo PU.1 sites.
- The role of PU.1 in disease-associated microglia (DAM) state during neurodegeneration.
- How LDFs interact with PU.1 to establish tissue-specific enhancers — collaborative binding vs sequential displacement.

## Relevance to active research

For my hypoxia-NF-κB work: PU.1 is upstream of every macrophage I study. NF-κB and PU.1 interact at enhancers — NF-κB binding can require pre-existing PU.1 occupancy at "primed" enhancers. Whether HIF1α also requires PU.1-pre-marked chromatin, or whether HIF1α can engage independently of PU.1, is an underexplored ChIP-seq question that bears on whether hypoxia repurposes the existing macrophage enhancer landscape or installs a parallel one.
