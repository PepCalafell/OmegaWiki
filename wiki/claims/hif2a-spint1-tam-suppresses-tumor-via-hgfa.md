---
title: "HIF-2α-induced Spint1 secreted by TAMs blocks HGFA-mediated HGF activation, inhibiting tumor cell proliferation"
slug: hif2a-spint1-tam-suppresses-tumor-via-hgfa
status: supported
confidence: 0.70
tags:
  - HIF2A
  - Spint1
  - HGFA
  - HGF
  - c-Met
  - TAM
  - serine-protease-inhibitor
  - tumor-suppression
  - dual-edged-hypoxia
domain: "immunology / oncology / hypoxia-signaling"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.11) summarizes that HIF-2α (specifically, not HIF-1α) highly expressed in TAMs induces secretion of the serine protease inhibitor Spint1. Spint1 enters the TME and blocks HGFA, preventing cleavage of pro-HGF into active HGF, reducing c-Met activation in tumor cells, and reducing tumor cell proliferation. This is a tumor-suppressing TAM mechanism, contrary to the dominant tumor-promoting role of TAMs."
conditions: "Documented in specific TAM populations under chronic hypoxia; suggests HIF-2α-driven TAM phenotype is not uniformly pro-tumorigenic."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The dominant narrative casts hypoxic-HIF-α-high TAMs as pro-tumorigenic. The Spint1 mechanism is a counter-example: HIF-2α specifically (not HIF-1α) induces transcription of Spint1 (SPINT1; serine-protease-inhibitor Kunitz-type 1) in TAMs. Secreted Spint1 enters the TME and binds HGFA (HGF activator), blocking HGFA's protease cleavage of inactive pro-HGF into active HGF. Reduced active HGF → reduced c-Met activation on tumor cells → reduced tumor cell proliferation. This is a tumor-suppressing TAM output of hypoxia, and a concerning pharmacological implication: HIF-2α inhibitors (Belzutifan, PT2385) intended to block tumor-cell-intrinsic HIF-2α may also unintendedly remove this TAM-side Spint1 brake on HGF signaling.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Adjacent claim: [[claims/belzutifan-first-fda-approved-hif2a-inhibitor-vhl]] (potential confounder).

## Conditions and scope

- HIF-2α-specific (HIF-1α does not induce Spint1 to the same degree).
- TAM-specific (not tumor-cell-intrinsic).
- Documented in specific cancer models (e.g. mammary, lung).

## Counter-evidence

- The Spint1 mechanism is one of several hypoxia outputs; its quantitative contribution to overall TAM-tumor balance may be small relative to the pro-tumorigenic M2-polarization output.
- HGF / c-Met signaling has many other regulators (HGFA, matriptase, hepsin) that may compensate when Spint1 is increased.

## Linked ideas

(none yet)

## Open questions

- Does Belzutifan's clinical efficacy in ccRCC partially work against itself by removing the TAM-Spint1 brake on HGF? Combinatorial outcomes with c-Met inhibitors (cabozantinib) may benefit.
- Are there pharmacological strategies to *selectively* spare the Spint1 output while inhibiting HIF-2α tumor-cell-intrinsic signaling (cell-type-specific delivery, conditional HIF-2α antagonism)?
