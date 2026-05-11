---
title: "Galectin-3 in hypoxic TAMs is regulated by ROS-NF-κB rather than HIF-1α"
slug: galectin-3-ros-nfkb-hypoxic-tam-not-hif1a
status: supported
confidence: 0.80
tags:
  - Galectin-3
  - LGALS3
  - ROS
  - NF-κB
  - HIF1A
  - hypoxic-TAM
  - VEGFA
  - angiogenesis
  - non-canonical-regulation
domain: "immunology / oncology / hypoxia-signaling"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.11) summarizes that although HIF-1α is elevated in hypoxic TAMs, HIF-1α inhibitors do NOT reduce Gal-3 expression in those cells. The regulation is instead via ROS → NF-κB. Galectin-3 in hypoxic TAMs drives tumor metastasis, angiogenesis, increased VEGFA secretion, and glucose consumption."
conditions: "Specific to hypoxic TAMs; HIF-1α inhibitor experiments establish the negative result that Gal-3 is HIF-1α-independent in this context."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Galectin-3 (LGALS3) is a β-galactoside-binding lectin highly expressed by hypoxic TAMs that drives tumor metastasis, angiogenesis, VEGFA secretion, and glucose consumption. Although HIF-1α is robustly stabilized in hypoxic TAMs, HIF-1α inhibitors (e.g. 2ME2) do NOT reduce Gal-3 expression in hypoxic TAMs — establishing that Gal-3 is HIF-1α-independent in this context. The actual regulator is the ROS-NF-κB axis: hypoxia-driven mitochondrial ROS activates NF-κB, which transcribes LGALS3. This is one of the rare hypoxic-TAM outputs that is HIF-independent yet still hypoxia-driven.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundation: [[foundations/galectin-3]].

## Conditions and scope

- Specific to hypoxic TAMs; primary cell-line evidence with HIF-1α inhibition controls.
- Generalizability to other macrophage subsets (M0, M1, MoMac-VERSE clusters) is unclear.

## Counter-evidence

- Some non-macrophage cancer contexts report HIF-1α-direct binding to the LGALS3 promoter (HRE consensus is present but possibly not used in macrophages).
- ROS-dependence is sensitive to mitochondrial function; cells with impaired oxidative phosphorylation may bypass this axis.

## Linked ideas

(none yet)

## Open questions

- Why does HIF-1α not regulate Gal-3 in hypoxic TAMs even though the HRE is present and HIF-1α is stabilized? Are p300 or HIF cofactors limiting?
- Does NF-κB-driven Gal-3 in hypoxic TAMs co-bind chromatin with HIF-1α at *other* hypoxia-NF-κB co-target loci, suggesting selective enhancer usage?
- Is Gal-3 inhibition (e.g. GR-MD-02 / belapectin) effective in pVHL-loss / HIF-1α-high tumors where it might otherwise be hypothesized ineffective?
