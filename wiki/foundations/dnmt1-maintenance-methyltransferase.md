---
title: "DNMT1 — DNA (cytosine-5)-methyltransferase 1 (maintenance)"
slug: dnmt1-maintenance-methyltransferase
domain: "biology / epigenetics"
status: mainstream
aliases:
  - "DNMT1"
  - "Dnmt1"
  - "DNA methyltransferase 1"
  - "maintenance methyltransferase"
  - "hemimethylation-directed methyltransferase"
first_introduced: "Bestor et al. *PNAS* 1988"
date_updated: 2026-05-27
source_url: "https://www.uniprot.org/uniprotkb/P26358"
---

## Definition

DNMT1 is the principal maintenance DNA methyltransferase. It copies parental-strand 5mCpG patterns onto the daughter strand at replication forks, propagating CpG methylation through cell division. Recruited via UHRF1 binding to hemimethylated CpG dyads, DNMT1 ensures heritable transmission of methylation landscapes.

## Intuition

Replication transiently halves the cell's CpG methylation (parental strand methylated, daughter strand naive). DNMT1 sits at the fork, recognises the hemimethylated CpG dyad through UHRF1, and reinstates symmetric methylation. Without DNMT1, methylation patterns dilute by 50% per division — the molecular basis of partially methylated domains (PMDs) accumulating in proliferating cells.

## Formal notation

- Substrate preference: hemimethylated CpG ≫ unmethylated CpG.
- Recruitment: replication fork via PCNA + UHRF1 (recognises hemimethylated CpG via SRA domain).
- Loss-of-function: global hypomethylation, embryonic lethal (mouse Dnmt1 KO at E8–E9).
- Co-acts with de novo methyltransferases [[foundations/dnmt3a-de-novo-dna-methyltransferase]] and DNMT3B.

## Key variants

- **DNMT1o** (oocyte isoform): truncated, stored cytoplasmically in oocytes.
- **DNMT1s** (somatic): canonical isoform in dividing somatic cells.

## Known limitations

- Sequence-context-specific: maintains CpG methylation but does not act efficiently on non-CpG (mCH) sites.
- Activity declines under hypoxia / replicative stress, contributing to PMD methylation loss with successive divisions ([[concepts/partially-methylated-domains-mitotic-clock]]).

## Open problems

- Mechanism of DNMT1 fidelity drop in cancer-associated hypomethylation.
- Direct measurement of DNMT1 activity in single cells / spatial pixels.

## Relevance to active research

DNMT1 expression dynamics in space and time were directly captured in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] (E13 brain > E11 brain), suggesting upregulated maintenance capacity in mid-gestation neurogenesis. DNMT1 levels also constrain [[concepts/partially-methylated-domains-mitotic-clock]] as a readout of mitotic history.
