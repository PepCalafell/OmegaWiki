---
title: "DoRothEA TF activity inference identifies c-Myc as the top-enriched regulon in Hif1a⁻/⁻ BMDMs (HIF1A most negative)"
slug: bmdm-hif1a-loss-derepresses-myc-regulon-dorothea
status: supported
confidence: 0.8
tags: [HIF1A,MYC,BMDM,DoRothEA,transcription-factor-activity,regulon,RNA-seq]
domain: immunometabolism / computational
source_papers:
  - hif-regulates-mitochondrial-function-bone-marrow
evidence:
  - source: hif-regulates-mitochondrial-function-bone-marrow
    type: supports
    strength: moderate
    detail: "DoRothEA mouse-regulon TF enrichment on Hif1a-/- vs Hif1a+/+ BMDM DEGs: HIF-1α regulon most negatively enriched (as expected); c-Myc most positively enriched. Concordant E2F1-4, LEF1, GIL2, TFDP1 (pro-growth) up; FOXO, TCF12, MAF, ONECUT down (Fig. 6A,B,C,D)."
conditions: "RNA-seq logFC ≤1, p ≤0.05; DoRothEA mouse regulon collection; baseline BMDM comparison."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Computational TF activity inference (DoRothEA) on Hif1a⁻/⁻ BMDM transcriptomes reveals that the c-Myc regulon becomes the most positively enriched program when HIF-1α is lost, with a concordant set of pro-growth/cell-cycle TFs (E2F1-4, LEF1, GIL2, TFDP1) and reciprocally suppressed glucose-homeostasis / cell-cycle-arrest TFs (FOXO, TCF12, MAF, ONECUT). This is the transcriptional signature underlying the metabolic and proliferative phenotype of HIF-1α-deficient BMDMs.

## Evidence summary

[[papers/hif-regulates-mitochondrial-function-bone-marrow]] Fig. 6A,B,C,D.

## Conditions and scope

In silico inference from bulk RNA-seq; not direct ChIP confirmation. Mouse only.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Direct ChIP-seq of c-Myc in Hif1a-/- vs WT BMDMs to validate the inferred activity shift; whether c-Myc protein levels (not only target footprint) increase.
