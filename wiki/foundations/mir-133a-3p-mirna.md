---
title: "miR-133a-3p (microRNA-133a-3p)"
slug: mir-133a-3p-mirna
domain: "molecular-biology / non-coding-RNA / prostate-cancer"
status: mainstream
aliases:
  - "miR-133a"
  - "miR-133a-3p"
  - "hsa-miR-133a-3p"
  - "MIR133A1"
  - "MIR133A2"
  - "miR-133a-1"
  - "miR-133a-2"
  - "muscle-enriched microRNA-133a"
  - "myomiR-133a"
  - "tumor-suppressor miR-133a"
first_introduced: "Sempere et al. 2004 Genome Biol; Chen et al. 2006 Nat Genet (myomiRs)"
date_updated: 2026-05-06
source_url: "https://www.mirbase.org/mirna/MI0000450/"
---

## Definition

miR-133a-3p is a microRNA encoded by two genomic loci (MIR133A1 on chr18q11 and MIR133A2 on chr20q13.33) that produces an identical mature -3p strand. Originally characterized as a muscle-enriched myomiR with cardiac and skeletal-muscle developmental roles, miR-133a-3p has since been shown to function as a tumor suppressor in multiple cancers, including prostate cancer, where its abundance is downregulated under hypoxia and its targets include the tumor suppressor BIN1 and the metabolic enzyme PGM5.

## Intuition

miR-133a-3p is a "brake" microRNA whose loss under hypoxia removes restraint on aggressive growth and invasion programs in prostate cancer. Reintroducing it to hypoxic prostate cancer cells decreases viability and invasion, demonstrating direct tumor-suppressor function downstream of hypoxia. This makes miR-133a-3p one of the rare hypoxia-modulated miRNAs with both pancancer correlative evidence and in vitro causal validation.

## Formal notation

- Two host genes: MIR133A1 (chr18q11.2, intronic to MIB1) and MIR133A2 (chr20q13.33, intronic to AGAP1)
- Both produce mature 22-nt miR-133a-3p
- Often co-expressed with miR-1 (myomiR cluster organisation)
- Known mRNA targets in cancer:
  - BIN1 (tumor suppressor, MYC-binding) — Sakamuro 1996 Nat Genet
  - PGM5 (phosphoglucomutase 5) — Edwards 1995 Genomics
  - WDR33, LDB3, DCAF16, VPS18, PYGM, SNRNP40, ASAP2, SDPR (validated correlatively in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] CPC-GENE)

## Key variants

- miR-133b — paralog, slightly different seed; co-expressed in muscle but not always in cancer
- miR-1 (myomiR cluster partner) — often co-expressed; combined miR-1/miR-133a regulation common in muscle development

## Known limitations

- Two genomic loci complicate locus-specific knockout / overexpression studies; most assays measure pooled mature -3p
- Plasma / urinary miR-133a-3p assays variable; circulating-biomarker utility unclear

## Open problems

- Mechanism by which hypoxia downregulates miR-133a-3p (transcriptional vs post-transcriptional) is not characterized.
- Whether miR-133a-3p mimics could be developed as a therapeutic for hypoxic prostate cancer is open.
- Tissue specificity: muscle expression is high; the prostate-tumor pool is much lower — does the tumor-suppressor effect depend on baseline expression level?

## Relevance to active research

miR-133a-3p is the strongest hypoxia-associated miRNA in localized prostate cancer in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] (TCGA: FDR=2.08×10⁻¹¹, ρ=−0.40), validated in CPC-GENE and Taylor cohorts. In vitro, a miR-133a-3p mimic decreases viability in 22Rv1, DU145, PC3 and decreases PC3 invasion (P=5.45×10⁻³). The miR-133a-3p–BIN1–MYC axis is a candidate mechanism linking hypoxia to MYC-pathway dysregulation in PCa.
