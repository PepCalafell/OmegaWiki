---
title: "HIF-α is hydroxylated by PHD1/2/3 and FIH under normoxia and degraded via pVHL ubiquitination"
slug: hif-phd-vhl-fih-canonical-degradation-axis
status: supported
confidence: 0.99
tags:
  - HIF1A
  - HIF2A
  - PHD
  - prolyl-hydroxylase
  - FIH
  - VHL
  - ubiquitin-proteasome
  - oxygen-sensing
  - canonical-axis
  - text-book
domain: "molecular-biology / hypoxia / oxygen-sensing"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
  - hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic
evidence:
  - source: hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic
    type: supports
    strength: strong
    detail: "Quote (p.3): 'Owing to the presence of the oxygen-dependent proline hydroxylase family (PHD), under sufficient oxygen conditions, the HIF-α protein is hydroxylated and interacts with von Hippel-Lindau tumor suppressor protein (pVHL) to promote HIF-1α ubiquitin-proteasomal degradation. However, under hypoxic conditions, enzymatic activity of PHD is inhibited, preventing HIF-α hydroxylation and ubiquitin-mediated proteasomal degradation, leading to abnormal accumulation of HIF-α in cells.'"
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.4-5) summarizes the canonical PHD/FIH/VHL oxygen-sensing axis: under normoxia HIF-α is hydroxylated at Pro402/Pro564 (HIF-1α) by PHD1/2/3 (2-OG + Fe(II) + O₂ dependent), recognized by pVHL E3 ligase, polyubiquitinated, and degraded by the 26S proteasome. FIH performs an asparagine hydroxylation that additionally blocks p300/CBP coactivator recruitment."
conditions: "Universal canonical axis across most cell types; the Kelly-Semenza 1995 / Maxwell-Ratcliffe 1999 foundational discovery."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Under normoxia, HIF-α subunits (HIF-1α, HIF-2α, HIF-3α) are hydroxylated at conserved proline residues by prolyl hydroxylase domain proteins PHD1, PHD2, and PHD3 (collectively the EGLN family), which require Fe(II), 2-oxoglutarate, ascorbate, and molecular O₂ as cofactors / substrate. The hydroxylated HIF-α is then recognized by the pVHL (von Hippel-Lindau) E3 ubiquitin ligase complex, polyubiquitinated at lysine residues, and rapidly degraded by the 26S proteasome (HIF-α half-life ~5 min under normoxia). Factor Inhibiting HIF (FIH) performs a parallel asparagine hydroxylation (Asn803 in HIF-1α) that additionally blocks recruitment of the p300/CBP coactivator complex, providing a transcriptional-activity off-switch independent of degradation. Under hypoxia, PHD/FIH lose activity → HIF-α stabilizes, accumulates, translocates to the nucleus, dimerizes with HIF-1β (ARNT), recruits p300/CBP, and binds the hypoxia response element (HRE; 5'-RCGTG-3') to drive transcription of >100 target genes.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundations: [[foundations/hif1a]], [[foundations/phd-prolyl-hydroxylases]], [[foundations/vhl-von-hippel-lindau]].
- Foundational discovery: Semenza & Wang 1992 (HIF-1 identification); Maxwell, Ratcliffe & Pugh 1999 (pVHL-HIF link); Bruick & McKnight 2001, Epstein 2001 (PHD identification); Lando 2002 (FIH identification).

## Conditions and scope

- Canonical across most cell types; PHD2 is the rate-limiting isoform under normoxia.
- HIF-1α has stronger pVHL affinity than HIF-2α — see [[claims/hif1a-stronger-vhl-affinity-than-hif2a]].
- Non-canonical activators (PIM1, iASPP) can bypass this axis — see [[claims/hif-uncoupled-from-oxygen-pim1-iaspp]].
- Direct HIF-independent O₂ sensors (KDM6A, KDM5A) operate in parallel — see [[claims/kdm6a-kdm5a-direct-oxygen-sensors]].

## Counter-evidence

- The PHD oxygen-sensing axis is the dominant but not the only O₂ sensor: JmjC histone demethylases provide a parallel chromatin-level axis.
- HIF-3α has at least three splice variants with non-canonical functions (some inhibitory of HIF-1α / HIF-2α).

## Linked ideas

(none yet)

## Open questions

- Why does PHD2 dominate over PHD1 and PHD3 in most cell types — kinetic vs expression-level reasons?
- How does the canonical axis interact with the KDM-axis O₂ sensors under physiological tumor hypoxia (pO₂ 5-20 mmHg)?
