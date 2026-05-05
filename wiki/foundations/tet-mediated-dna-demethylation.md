---
title: "TET-mediated DNA demethylation"
slug: tet-mediated-dna-demethylation
domain: "epigenetics / molecular-biology"
status: mainstream
aliases:
  - "TET enzymes"
  - "ten-eleven translocation methylcytosine dioxygenases"
  - "TET1, TET2, TET3"
  - "active DNA demethylation pathway"
  - "5mC oxidation to 5hmC/5fC/5caC"
  - "α-KG/Fe(II)-dependent demethylation"
  - "TET-driven hydroxymethylation"
first_introduced: "Tahiliani et al. 2009"
date_updated: 2026-05-05
source_url: "https://www.ncbi.nlm.nih.gov/gene/80312"
---

## Definition

Active DNA demethylation in mammals is initiated by ten-eleven translocation (TET) methylcytosine dioxygenases (TET1, TET2, TET3), which iteratively oxidize 5-methylcytosine (5mC) to 5-hydroxymethylcytosine (5hmC), 5-formylcytosine (5fC), and 5-carboxylcytosine (5caC). 5fC and 5caC are then excised by thymine DNA glycosylase (TDG) and replaced with unmodified cytosine via base-excision repair, completing demethylation. TET activity requires α-ketoglutarate (α-KG), Fe²⁺, and oxygen (O₂) as cofactors; ascorbate enhances activity.

## Intuition

TETs are the "erasers" of DNA methylation. They need oxygen, so under hypoxia their activity drops, leading to global DNA hypermethylation in tumors (Thienpont 2016 *Nature*). 5hmC accumulation at enhancers and gene bodies is a hallmark of active gene expression.

## Formal notation

- TET1, TET2, TET3 isoforms; TET2 is the most studied in hematopoiesis/myeloid biology
- Cofactors: α-KG, Fe²⁺, O₂; competitive inhibitor: 2-hydroxyglutarate (oncometabolite in IDH-mutant tumors)
- Reaction: 5mC →[TET]→ 5hmC →[TET]→ 5fC →[TET]→ 5caC →[TDG/BER]→ C
- Pharmacological inhibitors: 4-octyl itaconate (used in this paper), bobcat-339 (reported), DMOG (broader α-KG-dependent dioxygenase inhibitor)

## Key variants

- TET2: most prominent in myeloid lineage; loss-of-function mutations common in clonal hematopoiesis and AML.
- TET1: stem-cell biology, embryonic development.
- TET3: oocyte-to-zygote demethylation, neurons.

## Known limitations

- Chemical inhibitors are not isoform-specific (4-octyl itaconate inhibits broader α-KG-dependent dioxygenases).
- 5hmC quantification is technically challenging and often confounds 5mC measurement.
- TET catalytic activity vs scaffold/recruitment functions are not always separable.

## Open problems

- Rules for TET recruitment to specific genomic loci (likely TF-mediated; mechanism varies).
- TET-isoform redundancy and specificity.
- Direct vs indirect role of TETs in transcriptional regulation independent of demethylation.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] shows that hypoxic TET inhibition can be locally overridden at NF-κB-bound enhancers (cluster C2). 4-octyl itaconate (TET2 inhibitor) blocks both demethylation and gene expression at C2 loci, establishing TET dependence. The paper attributes the override to NF-κB-mediated recruitment/licensing of TET activity at proinflammatory loci, though TET-isoform specificity is not formally resolved.
