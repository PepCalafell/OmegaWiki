---
title: "PTEN (Phosphatase and Tensin Homolog)"
slug: pten-tumor-suppressor
domain: "molecular-biology / oncology / signaling"
status: mainstream
aliases:
  - "PTEN"
  - "MMAC1"
  - "TEP1"
  - "phosphatase and tensin homolog deleted on chromosome 10"
  - "PI(3,4,5)P3 3-phosphatase"
  - "PIP3 phosphatase"
  - "tumor suppressor on chromosome 10q23"
  - "PTEN/PI3K/AKT axis suppressor"
first_introduced: "Li et al. 1997 Science; Steck et al. 1997 Nat Genet"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprot/P60484"
---

## Definition

PTEN is a dual-specificity protein and phosphoinositide phosphatase that dephosphorylates phosphatidylinositol-3,4,5-trisphosphate (PIP3) to PIP2, antagonizing PI3K signaling and thereby restraining AKT/mTOR-driven proliferation, growth, and survival. PTEN is one of the most frequently lost tumor-suppressor genes in human cancer (chromosome 10q23.31), with loss-of-heterozygosity, deletion, point mutation, and promoter methylation as recurrent loss mechanisms.

## Intuition

Think of PTEN as the brake on the PI3K-AKT growth-survival axis. Loss of one or both alleles releases AKT, drives anabolic metabolism, suppresses apoptosis, and enables genomic instability through indirect destabilization of DNA-repair pathways. PTEN loss is almost universally associated with poor prognosis in solid tumors, especially in prostate cancer where allelic loss is a major prognostic biomarker.

## Formal notation

- Encoded by PTEN gene (chr10q23.31 in human)
- Protein: 403 aa; phosphatase domain (residues 14–185) + C2 domain
- Catalytic activity: PIP3 → PIP2 (lipid phosphatase) and protein-tyrosine/serine/threonine phosphatase
- Major loss-of-function classes: nonsense / frameshift / missense in catalytic core (e.g., R130G/Q/L); deep deletion; allelic loss with retained wild-type allele; promoter hypermethylation
- Functional readouts: pAKT (S473) elevated, pS6 elevated, mTORC1 active

## Key variants

- Germline PTEN mutations: PTEN hamartoma tumor syndromes (Cowden syndrome, Bannayan–Riley–Ruvalcaba)
- PTEN hypomorphic alleles in mouse models (PtenL/L) recapitulate prostate intraepithelial neoplasia and progression
- Cytoplasmic vs nuclear PTEN: nuclear PTEN supports genome integrity beyond canonical PIP3 function

## Known limitations

- "PTEN loss" can mean very different molecular states (allelic loss with intact mRNA vs deep deletion vs missense in catalytic core); these have different functional consequences but are often pooled in clinical assays.
- IHC for PTEN is technically demanding; loss calls vary across pathology centers.

## Open problems

- Whether PTEN loss is a *cause* or *consequence* of tumor hypoxia in localized prostate cancer is debated; bidirectional links via HIF1A stabilization (Zundel et al. 2000) and TERT regulation are described but mechanism in vivo is incompletely resolved.
- Therapeutic strategies for PTEN-loss tumors (PI3K-α/β inhibitors, mTOR inhibitors, synthetic lethality with PARP) have had mixed clinical results.

## Relevance to active research

PTEN allelic loss is one of the central axes in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]: hypoxia and PTEN loss synergistically predict poor outcome in localized PCa (HR=4.4, p=1.95×10⁻³), and PTEN mRNA is negatively correlated with TERT mRNA in a hypoxia-dependent manner. PTEN status is a defining feature of the "nimbosus" aggressive phenotype proposed by Bhandari et al. 2019.
