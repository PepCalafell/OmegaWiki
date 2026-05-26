---
title: "DNMT3A — de novo DNA methyltransferase 3A"
slug: dnmt3a-de-novo-dna-methyltransferase
domain: epigenetics / chromatin
status: mainstream
aliases:
  - "DNMT3A"
  - "DNA methyltransferase 3A"
  - "de novo DNA methyltransferase"
  - "Dnmt3a"
  - "DNMT3A R882H"
  - "DNMT3A CHIP mutation"
  - "haematopoietic DNMT3A"
  - "DNA cytosine-5 methyltransferase 3A"
first_introduced: "Okano 1999 Cell; reviewed in Lyko 2018 Nat Rev Genet"
date_updated: 2026-05-26
source_url: ""
---

## Definition

DNMT3A is one of two mammalian de novo DNA methyltransferases (DNMT3A / DNMT3B) that catalyze methyl-group transfer from S-adenosylmethionine (SAM) to the C5 position of cytosine in CpG dinucleotides. It is the dominant de novo methyltransferase active in adult haematopoietic stem cells, mature macrophages, and other postnatal somatic lineages; loss-of-function or dominant-negative mutations (notably DNMT3A R882H) are the most common driver of clonal haematopoiesis of indeterminate potential (CHIP) and are linked to acute myeloid leukaemia and elevated cardiovascular disease risk.

## Intuition

DNMT3A writes methylation marks at sites that were previously unmethylated — establishing context-specific repression of enhancers, promoters, and gene bodies during cell-fate decisions. In mature macrophages, it can be acutely engaged by exogenous SAM (e.g., from efferocytosed apoptotic cells) to repress regulatory genes such as Dusp4, thereby switching downstream signalling output.

## Formal notation

- Gene: DNMT3A (chr2p23); protein with PWWP, ADD, and methyltransferase domains
- Cofactor: S-adenosylmethionine (SAM), donating methyl group, generating S-adenosylhomocysteine (SAH)
- Specificity: CpG sites; also non-CpG methylation in stem cells and neurons
- Conditional alleles: Dnmt3afl/fl × Vav1Cre (haematopoietic KO) — used in Ampomah 2022 and other myeloid studies
- Disease associations:
  - Clonal haematopoiesis of indeterminate potential (CHIP): heterozygous loss-of-function expands a clone with cardiovascular and AML risk
  - DNMT3A R882H: dominant-negative mutation, most common in AML
  - Tatton-Brown-Rahman syndrome: germline loss-of-function → overgrowth syndrome
- Pharmacology: no selective small-molecule inhibitors; pan-DNMT inhibitors (decitabine, azacitidine) target DNMT1 primarily

## Variants

- DNMT3A vs DNMT3B: DNMT3A dominates in postnatal somatic cells; DNMT3B in early embryogenesis
- DNMT3L: accessory subunit boosting DNMT3A/B activity
- Soluble vs chromatin-bound pools; PWWP domain reads H3K36me2/3 marks

## Known limitations

- Lack of selective DNMT3A inhibitors limits pharmacological dissection
- Antibody quality variable across vendors
- Off-target genetic effects in conditional KOs may overlap with DNMT3B compensation

## Open problems

- How DNMT3A is recruited to specific loci (e.g., Dusp4 promoter) by transcription factors or post-translational signals
- Whether AC-derived methionine specifically routes to DNMT3A vs other methyltransferases
- Mechanistic basis for CHIP-associated cardiovascular risk

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*) where macrophage DNMT3A is the obligate enzyme writing methylation marks on the Dusp4 promoter during efferocytosis, using SAM derived from apoptotic-cell methionine. The paper proposes this mechanism as a candidate link between DNMT3A CHIP mutations and coronary artery disease risk (impaired efferocytosis-resolution in plaques).
