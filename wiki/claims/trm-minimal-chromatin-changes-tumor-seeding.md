---
title: "TRMs show minimal global chromatin accessibility changes in response to tumour seeding"
slug: trm-minimal-chromatin-changes-tumor-seeding
status: supported
confidence: 0.8
tags:
  - TRM
  - NSCLC
  - ATAC-seq
  - chromatin-accessibility
  - tissue-imprint
domain: "immunology / oncology / epigenetics"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: moderate
    detail: "ATAC-seq on sorted alveolar TRMs from healthy / day-15 / day-30 KP tumour-bearing lungs (50,000 cells per sample, n=3 biological replicates per condition). Minimal genome-wide accessibility changes between tumour-associated and healthy-lung TRMs. Most accessibility changes occurred early at the Mmp12/Mmp13 loci. MHC-II loci remained accessible across all conditions. Reduced accessibility at Ripor2/Dgkg gene-coding regions."
conditions: "Mouse KP orthotopic NSCLC; ATAC-seq via Buenrostro 2013 protocol; Bowtie2 mm10 alignment; MACS2 peak calling; DESeq2 differential analysis at P<0.05."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Despite extensive transcriptional reprogramming (1,670 DEGs), tumour-associated tissue-resident macrophages in KP NSCLC show minimal global ATAC-seq chromatin accessibility changes compared to healthy-lung TRMs. The few significant accessibility changes are concentrated early (day 15) at MMP12/MMP13 loci. This suggests that tumour-induced reprogramming of TRMs operates largely within the existing tissue-imprinted chromatin landscape rather than requiring de novo enhancer activation.

## Evidence summary

- ATAC-seq, n=3 replicates per condition (healthy / day 15 / day 30)
- 50,000 sorted TRMs per sample; standard Buenrostro pipeline
- Minimal global accessibility changes; localised gains at MMP12/MMP13
- MHC-II loci accessible across conditions
- Localised losses at Ripor2/Dgkg loci

## Conditions and scope

- Mouse KP NSCLC; bulk ATAC-seq, modest n
- "Minimal" defined relative to expected scale of accessibility remodelling in inflammatory or differentiation contexts; not absent

## Counter-evidence

- Bulk-level analysis may obscure focal accessibility changes within TRM subpopulations
- Single-cell ATAC-seq might reveal heterogeneity not captured here
- 3 biological replicates is modest for chromatin-accessibility differential analysis

## Linked ideas

(none yet)

## Open questions

- Single-cell ATAC-seq in tumour TRMs to resolve subset-level chromatin dynamics
- Whether the existing accessible enhancer landscape is sufficient to encode the tumour-induced transcriptional programme via TF re-distribution
- Whether other epigenetic layers (DNA methylation, histone modifications) show stronger tumour-induced changes
