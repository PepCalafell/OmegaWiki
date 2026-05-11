---
title: "HIF-2α small-molecule inhibitors targeting the PAS-B pocket are selective for HIF-2α/ARNT dissociation without affecting HIF-1"
slug: hif2a-pas-b-pocket-small-molecule-inhibitors-selective
status: supported
confidence: 0.90
tags:
  - HIF2A
  - PAS-B
  - small-molecule-inhibitor
  - Belzutifan
  - MK-6482
  - PT2385
  - ARNT
  - HIF-1
  - selectivity
  - structural-biology
  - allosteric-inhibition
domain: "pharmacology / oncology / structural-biology"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.13-14) reviews HIF-2α PAS-B-pocket small-molecule inhibitors Belzutifan (MK-6482) and PT2385 (and successors DFF332, NKT2152). Despite the high sequence identity between HIF-2α and HIF-1α, these inhibitors are highly selective in dissociating the HIF-2α/ARNT heterodimer while having no effect on HIF-1. Selectivity arises from a unique cavity in the HIF-2α PAS-B domain not present in HIF-1α."
conditions: "Structural-biology-validated selectivity; biochemical and cellular assays confirm no off-target HIF-1 activity at therapeutic doses."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

HIF-2α and HIF-1α share high sequence identity in their bHLH-PAS architecture. However, the PAS-B domain of HIF-2α contains a unique internal cavity (~290 Å³ pocket lined by hydrophobic residues) that is absent in HIF-1α. Allosteric small-molecule inhibitors of HIF-2α — Belzutifan (MK-6482), PT2385 (first-in-class), and successors DFF332 and NKT2152 — exploit this PAS-B pocket. When the small molecule binds, it sterically perturbs the HIF-2α dimerization interface with ARNT, dissociating the HIF-2α/ARNT heterodimer and preventing HRE transcription. Because the analogous pocket in HIF-1α is much smaller and structurally distinct, these inhibitors do NOT bind HIF-1α PAS-B and do NOT inhibit HIF-1α/ARNT — providing pharmacological isoform selectivity. This is the structural basis for Belzutifan's clinical utility in ccRCC (where HIF-2α is the dominant oncogenic driver in pVHL-null cells) without disrupting HIF-1α's homeostatic erythropoiesis and metabolic functions.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Concept: [[concepts/hif-2a-pas-b-small-molecule-inhibition]].
- Foundations: [[foundations/belzutifan-mk-6482]], [[foundations/pt2385-hif2a-inhibitor]].
- Primary structural-biology: Scheuermann 2009 PNAS (PAS-B cavity discovery); Wallace 2016 Cancer Res (PT2385 mechanism).

## Conditions and scope

- Selectivity is structural and biochemical, demonstrated at the protein-level affinity (Kd HIF-2α >> HIF-1α).
- Cellular and in vivo evidence confirms HIF-1α target genes are unaffected at therapeutic doses.

## Counter-evidence

- At very high concentrations (10-100× clinical), some off-target effects on HIF-1α and other PAS-domain proteins (AhR) become detectable.
- Resistance to PT2385 in ccRCC has been mapped to G323E mutation in HIF-2α PAS-B (disrupting drug binding while preserving HIF-2α function).

## Linked ideas

(none yet)

## Open questions

- Are there other PAS-domain proteins (AhR, Period proteins) where analogous selective allosteric pockets could be exploited for isoform-selective inhibition?
- Can resistance-conferring HIF-2α mutations be overcome by next-generation drugs (DFF332, NKT2152) or by combination strategies?
