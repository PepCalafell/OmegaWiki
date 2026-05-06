---
title: "HIF1α (Hypoxia-Inducible Factor 1α)"
slug: hif1a
domain: "molecular-biology / hypoxia-signaling"
status: mainstream
aliases:
  - "HIF1A"
  - "HIF-1α"
  - "Hypoxia-Inducible Factor 1 alpha"
  - "HIF1"
  - "EPAS1 paralog (HIF2α)"
  - "alpha subunit of HIF-1"
first_introduced: "Semenza & Wang 1992"
date_updated: 2026-05-05
source_url: "https://www.uniprot.org/uniprot/Q16665"
---

## Definition

HIF1α is the oxygen-regulated subunit of the Hypoxia-Inducible Factor 1 (HIF-1) transcription factor complex. Under normoxia, HIF1α is hydroxylated by prolyl hydroxylase domain (PHD) enzymes on key proline residues, recognized by the von Hippel-Lindau (VHL) E3 ligase, and degraded by the proteasome. Under hypoxia (low O₂), PHD activity drops, HIF1α stabilizes, dimerizes with the constitutive HIF1β/ARNT subunit, and binds hypoxia-response elements (HREs, consensus 5′-RCGTG-3′) to activate transcription of metabolic, angiogenic, and inflammation-modulating genes.

## Intuition

HIF1α is the cell's master oxygen sensor's output: when O₂ is plentiful, it gets degraded; when O₂ drops, it accumulates and rewires transcription toward glycolysis, angiogenesis (VEGF), erythropoiesis (EPO), and a subset of inflammatory programs. Dysregulation is central to cancer metabolism, ischemic disease, and hypoxic immune reprogramming.

## Formal notation

- Encoded by HIF1A gene (chr14q23.2 in human)
- O₂-dependent degron: Pro402, Pro564 (hydroxylated by PHD1/2/3)
- Asparagine hydroxylation by FIH at Asn803 blocks p300 recruitment under normoxia
- Active complex: HIF1α/ARNT heterodimer + p300/CBP coactivator
- DNA binding motif: 5′-RCGTG-3′ (HRE)

## Key variants

- HIF2α (EPAS1): paralog with overlapping but distinct target sets (VEGF, erythropoietin emphasis)
- HIF3α (HIF3A): often inhibitory, multiple isoforms

## Known limitations

- Cell-type-specific target gene sets — same TF, different transcriptional output across tissues.
- HIF1α and inflammation: literature is contradictory (pro-inflammatory in some contexts, anti-inflammatory in others), as the present paper foregrounds.

## Open problems

- Therapeutic targeting (HIF inhibitors like PX-478, belzutifan/HIF2α-specific): tissue-specificity and toxicity.
- Mapping HIF1α to immune cell subsets at single-cell resolution.

## Relevance to active research

HIF1α is foundational to any study on hypoxic gene regulation. In [[papers/nf-kb-tet2-promote-macrophage-reprogramming]], HIF1α is the dominant transcriptional regulator in hypoxic resting MACs but is overtaken by STAT2/IRF1/RELA after LPS activation. HIF1α and p65 (NF-κB) cooperate at a subset of cobound chromatin regions without strong physical interaction. PX-478, a HIF1α inhibitor, was used to dissect HIF1α-dependent vs NF-κB-dependent contributions. In [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], 51 of 85 HIF1A target genes correlate strongly with mRNA hypoxia score in localized prostate cancer (CPC-GENE / TCGA), and TERT — a direct HIF1A target — anchors a three-way hypoxia × PTEN × TERT interaction modulating telomere length.
