---
title: "HIF2α (Hypoxia-Inducible Factor 2α / EPAS1)"
slug: hif2a
domain: "molecular-biology / hypoxia-signaling"
status: mainstream
aliases:
  - "HIF2A"
  - "HIF-2α"
  - "EPAS1"
  - "Hypoxia-Inducible Factor 2 alpha"
  - "endothelial PAS domain-containing protein 1"
  - "HLF (HIF-like factor)"
  - "MOP2"
first_introduced: "Ema et al. 1997; Tian et al. 1997"
date_updated: 2026-05-13
source_url: "https://www.uniprot.org/uniprot/Q99814"
---

## Definition

HIF2α (EPAS1) is the second paralog of the α-subunits of the Hypoxia-Inducible Factor family. Like HIF1α, it is oxygen-regulated via PHD-mediated prolyl hydroxylation and pVHL-dependent ubiquitination, dimerizes with HIF1β/ARNT, and binds hypoxia-response elements (HREs). However, HIF2α is expressed in restricted tissues (endothelium, kidney, liver, lung, CNS macrophages) and drives a partially distinct transcriptional program emphasizing erythropoiesis (EPO), constitutive VEGF, MYC/E2F target gene activation, lipoprotein metabolism, and a long-term adaptation phenotype.

## Intuition

HIF1α dominates the acute hypoxic response; HIF2α dominates chronic / long-term hypoxic adaptation. In clear cell renal cell carcinoma (ccRCC), VHL loss leads to constitutive HIF2α activation that is the principal oncogenic driver — exploited therapeutically by belzutifan (MK-6482, PT2977), PT2385 and PT2399. HIF2α also promotes sorafenib resistance in HCC via TGF-α/EGFR/COX-2.

## Formal notation

- Encoded by EPAS1 gene (chr2p21 in human)
- O₂-dependent degron: Pro405, Pro531 (hydroxylated by PHD1/2/3 — PHD2 preferred for HIF1α, PHD1/PHD3 contribute for HIF2α)
- Active complex: HIF2α/ARNT heterodimer
- DNA binding: 5′-RCGTG-3′ HRE (shared with HIF1α; selectivity comes from coactivators and chromatin context)
- Small-molecule pocket: PAS-B domain — drug-targetable (belzutifan binding site)

## Key variants

- VHL-mutant ccRCC: HIF2α constitutively stabilized; HIF1α often lost
- HIF2α-driven endothelial program: distinct angiogenic & EPO axis
- Pseudohypoxic HIF2α activation: SDH/FH/IDH-mutant tumors

## Known limitations

- Belzutifan efficacy in VHL-disease ccRCC is real but partial (≈49% objective response in pivotal trial).
- Adverse events: anemia, hypoxia (off-target erythropoiesis-suppression and HVR effects).
- HIF1α/HIF2α "switch" with chronic hypoxia is not fully mapped in non-renal cancers.

## Open problems

- HIF2α-specific drug resistance mechanisms in ccRCC.
- Therapeutic role in non-ccRCC tumors (HCC, glioblastoma).
- Tissue-specific HIF1α/HIF2α selectivity rules.

## Relevance to active research

HIF2α is the load-bearing target of belzutifan ([[foundations/belzutifan-mk-6482]]) and is the dominant α-subunit in many late/chronic-hypoxic phenotypes. In [[papers/hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic]], HIF2α drives sorafenib resistance in HCC (TGF-α/EGFR/COX-2 pathway), promotes IL-10 release from HCC via STAT3 to inhibit NK killing, regulates 5-FU resistance via DPD in macrophages, and stimulates ITPR1 to inhibit NK granzyme B. The PAS-B pocket of HIF2α is exploited by [[foundations/pt2385-hif2a-inhibitor]] and [[foundations/belzutifan-mk-6482]].
