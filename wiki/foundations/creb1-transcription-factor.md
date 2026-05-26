---
title: "CREB1 — cAMP response element binding protein 1"
slug: creb1-transcription-factor
domain: transcription / signalling
status: mainstream
aliases:
  - "CREB1"
  - "CREB"
  - "cAMP response element binding protein"
  - "p-CREB"
  - "phospho-CREB"
  - "Creb1"
  - "CREB-1"
  - "bZIP CREB family TF"
first_introduced: "Montminy 1986; Gonzalez 1989"
date_updated: 2026-05-26
source_url: ""
---

## Definition

CREB1 is a basic leucine-zipper (bZIP) transcription factor that binds cAMP response elements (CRE; TGACGTCA) in target gene promoters. Activation requires phosphorylation at Ser133 by PKA (downstream of Gs-coupled receptors and cAMP), CaMKIV, or other kinases; phospho-CREB recruits CBP/p300 coactivators and drives gene transcription. CREB1 is a major effector of PGE2-EP2/EP4 signaling on macrophages, linking cAMP to inflammatory and resolution gene programs.

## Intuition

CREB1 is how cAMP signals reach the genome. When PGE2 binds EP2/EP4 on macrophages, it raises cAMP → PKA → p-CREB → transcription of TGFβ1 and other resolution-program genes. Loss of any node (DNMT3A-dependent CREB1 phosphorylation in Ampomah 2022) breaks this chain.

## Formal notation

- Gene: CREB1 (chr2q32)
- Activation: Ser133 phosphorylation by PKA, CaMKIV, RSK, MSK
- DNA binding: CRE consensus TGACGTCA (palindromic)
- Coactivators: CBP/p300, TORC (CRTC) family
- Targets: TGFB1, cyclin D1, BDNF, NR4A family, PEPCK
- Detection: anti-p-CREB Ser133 antibody (Western, IF, flow)
- Perturbation: siCreb1, CREB-DN dominant-negative (KCREB)

## Variants

- CREM, ATF1 — related bZIP TFs with overlapping CRE recognition
- CREB Ser142 phosphorylation — opposite effect

## Known limitations

- Antibody cross-reactivity with ATF1, CREM
- CRE motifs overlap with AP-1 sites
- Tissue specificity of CREB target genes large

## Open problems

- The DNMT3A-dependent step linking PGE2-EP2/4 to CREB1 phosphorylation observed in Ampomah 2022 is mechanistically unresolved
- Whether CREB1 cooperates with NF-κB or SMAD3 on TGFB1 induction

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): PGE2-induced p-CREB1 is abolished in DNMT3A-KO macrophages, and siCreb1 blocks both PGE2-induced and AC-induced Tgfb1 induction — establishing CREB1 as the obligate TF mediating PGE2→TGFβ1 in efferocytosis-driven resolution.
