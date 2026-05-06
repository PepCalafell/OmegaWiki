---
title: "TP53 SNVs are recurrently associated with elevated tumor hypoxia across multiple tumor types"
slug: tp53-snvs-recurrently-associated-with-hypoxia
status: supported
confidence: 0.9
tags:
  - TP53
  - hypoxia
  - SNV
  - mutation
  - pancancer
  - selection
domain: "oncology / cancer-genomics"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "Pancancer association of TP53 SNVs with elevated hypoxia in BRCA (Bonferroni P=4.38×10⁻⁶¹), LUAD (P=1.83×10⁻¹²), LIHC (P=1.64×10⁻⁵), HNSC (P=2.26×10⁻³), KIRC, KIRP, PAAD, and localized PRAD. Bridges across BRCA molecular subtypes (Bonferroni P=4.38×10⁻⁶¹ overall, individual subtype effects also significant). Quote (p.309): 'TP53 mutations are enriched in hypoxic tumors within each breast cancer subtype, thus supporting the idea that they are a genomic consequence of tumor hypoxia.' Authors propose hypoxia → apoptosis selection → enrichment of mutant TP53 subclones (Graeber 1996 mechanism)."
conditions: "Holds in solid tumors with sufficient TP53 SNV frequency. May not hold in TP53-near-universal tumor types (HGSOC ovarian, where TP53 is mutated in ~95% of cases regardless of hypoxia)."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

TP53 single-nucleotide variants are statistically enriched in hypoxic tumors across multiple cancer types in TCGA, with the strongest association in BRCA (Bonferroni P=4.38×10⁻⁶¹) and significant signals in LUAD, LIHC, HNSC, KIRC, KIRP, PAAD, and localized prostate cancer. The association persists within molecular subtypes of breast cancer, ruling out subtype confounding. The authors propose this enrichment reflects hypoxia-driven *selection* of apoptosis-deficient subclones — a genomic *consequence* of the hypoxic microenvironment rather than an independent oncogenic event.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary evidence: significant enrichment in 7+ tumor types, multiple statistical adjustments, persistence across BRCA subtypes.
- Mechanistic prior: Graeber et al. 1996 *Nature* — hypoxia-mediated selection of cells with diminished apoptotic potential in solid tumors.

## Conditions and scope

- Tumor types with sufficient WT-vs-mutant TP53 dynamic range.
- Not necessarily linear with hypoxia score — typically a binary mutation enrichment in the hypoxic vs normoxic split.
- May not generalize to tumor types where TP53 is near-universal (HGSOC).

## Counter-evidence

- Direct causal proof requires longitudinal models or genetically engineered systems.
- Some confounders (clonal hematopoiesis, germline modifiers, TMB) not fully ruled out.

## Linked ideas

(none yet)

## Open questions

- Is the association purely selective (hypoxia kills WT-TP53, leaves mutant) or partly mutagenic (hypoxia + repair deficit drives TP53 mutation directly)?
- Why is the BRCA signal so much stronger than LUAD/HNSC?
- Does ancestry-specific hypoxia (BRCA: White < Asian/African) contribute to ancestry differences in TP53 mutation rate?
