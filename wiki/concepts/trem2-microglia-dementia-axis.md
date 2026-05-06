---
title: "TREM2 / DAP12 microglia–dementia axis"
aliases:
  - "TREM2 microglia"
  - "Nasu-Hakola disease"
  - "polycystic lipomembranous osteodysplasia"
  - "TREM2-DAP12 signaling"
  - "TREM2 Alzheimer's risk"
  - "TYROBP microglia"
  - "disease-associated microglia DAM"
  - "PLOSL"
  - "Nasu-Hakola TYROBP"
  - "TREM2 R47H Alzheimer"
  - "TREM2 lipid sensing macrophage"
tags:
  - microglia
  - TREM2
  - DAP12
  - dementia
  - Alzheimer
  - Nasu-Hakola
  - neurodegeneration
  - macrophage
  - lipid-sensing
maturity: active
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Paloneva 2002 (Nasu-Hakola TREM2/DAP12); Guerreiro 2013 NEJM (TREM2 R47H Alzheimer); Keren-Shaul 2017 Cell (DAM); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - microglia-synaptic-pruning-complement
  - csf1r-il34-csf2-trophic-axis
---

## Definition

The TREM2 / DAP12 axis links a single myeloid receptor to two distinct neurodegenerative diseases. (1) Bi-allelic loss-of-function mutations in TREM2 or its adapter DAP12/TYROBP cause Nasu-Hakola disease (PLOSL — polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy), a neurodegenerative + bone disease combining presenile dementia and bone cysts. (2) Common variants of TREM2 (most prominently R47H) substantially increase risk of late-onset Alzheimer's disease. The mechanistic substrate of both diseases is microglial dysfunction — TREM2 is a lipid-sensing receptor that shapes microglial states (especially the disease-associated microglia, DAM, programme).

## Intuition

TREM2 is a microglial sentinel that detects lipid-rich substrates — apoptotic cells, myelin debris, amyloid-associated lipids — and instructs the cell to phagocytose, restructure metabolism (mitochondrial/glycolytic), and adopt the DAM transcriptional state. Without TREM2 signaling, microglia fail to clear damage-associated material; debris accumulates, neurons lose support, and the cumulative effect over decades becomes neurodegeneration. The same receptor is also expressed on osteoclasts (multinucleated macrophages of bone), which is why TREM2/DAP12 LOF causes a combined CNS-bone disease (Nasu-Hakola) rather than a CNS-only one.

## Formal notation

- **TREM2**: triggering receptor expressed on myeloid cells 2; lipid-sensing immunoreceptor on microglia, osteoclasts, alveolar macrophages, TAMs
- **DAP12** (TYROBP): ITAM-bearing adapter; transduces TREM2 signal via SYK-PI3K-PLCγ
- **Diseases**:
  - Nasu-Hakola (PLOSL): bi-allelic TREM2 or TYROBP LOF → presenile dementia + bone cysts; rare autosomal recessive
  - Alzheimer's disease: heterozygous TREM2 variants (R47H most studied) → ~3-fold increased odds; common in European populations
  - Frontotemporal dementia: rare TREM2 homozygous LOF cases
- **Microglial state**: DAM (Keren-Shaul 2017) — TREM2-dependent transcriptional state characterized by APOE, CST7, SPP1, GPNMB, LPL upregulation; appears around amyloid plaques and after demyelination
- **Bone phenotype**: osteoclast TREM2 LOF → impaired multinucleated osteoclast function → bone cysts (Nasu-Hakola) and contributes to TREM2-LOF osteopetrosis

## Variants

- *DAM (disease-associated microglia)* — TREM2-dependent neurodegenerative microglial state
- *Lipid-associated macrophage (LAM)* — TREM2-dependent obesity / fatty-liver state; same receptor different tissue
- *Cancer-associated TREM2 macrophages* — TREM2⁺ TAMs in multiple cancers; marker of immunosuppressive state (overlaps with [[concepts/trem2-tumor-associated-macrophage]])

## Comparison

vs CSF1R disease genetics: both axes cause leukoencephalopathy phenotypes when LOF (CSF1R bi-allelic = absent microglia at birth; TREM2 bi-allelic = present-but-dysfunctional microglia). The phenotypic gradient maps to whether microglia are missing or merely impaired.
vs APOE in Alzheimer's: APOE is the lipid carrier that microglial TREM2 senses; APOE4 (Alzheimer-risk allele) and TREM2 variants interact within the same lipid-sensing pathway.
vs synaptic-pruning-complement axis: complement-pruning is the developmental mechanism; TREM2-DAM is the neurodegeneration mechanism. They share microglial machinery but differ in trigger and outcome.

## When to use

- Interpreting TREM2-conditional mouse phenotypes (often hidden under conditional-KO subtleties because TREM2 is microglial-specific within CNS but expressed broadly elsewhere).
- Designing microglia-targeted Alzheimer therapy (TREM2 agonist antibodies are in trials).
- Predicting bone phenotypes when modulating TREM2 (the receptor is shared between microglia and osteoclasts).

## Known limitations

- TREM2 has multiple ligands (lipids, APOE, β-amyloid, anionic lipids); ligand specificity is incomplete.
- DAM signature is partly conserved across species but the regulatory logic is mouse-derived.
- Heterozygous-vs-homozygous severity gradient is not fully mechanistic.

## Open problems

- Whether TREM2 agonists in late-stage Alzheimer's will help (DAM may be exhausted) or harm (overdrive of inflammation).
- The interaction between TREM2-DAM and complement-pruning machinery in synapse loss.
- Why some TREM2 variants are protective (T96K, L211P) while others are risk-increasing (R47H, R62H).

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review covers the TREM2/DAP12 → Nasu-Hakola disease link, the GWAS evidence for TREM2 in Alzheimer's, and disease-risk enhancer–promoter maps for microglia (Nott 2019)

## My understanding

The TREM2 axis is the most heavily-studied translation route between mouse macrophage biology and human Alzheimer therapy. For my hypoxia-NF-κB work, TREM2 is not directly relevant — but it appears in the wiki because TREM2⁺ macrophages are a recurrent immunosuppressive state in tumours (TREM2_Mac in MoMac-VERSE, TREM2-MARCO in Casanova-Acebes 2021 NSCLC). The dementia angle is a useful reminder that the *same receptor* configures totally different outcomes depending on the macrophage's tissue and pathology context.
