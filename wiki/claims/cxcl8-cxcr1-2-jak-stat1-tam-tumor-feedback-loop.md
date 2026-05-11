---
title: "Hypoxia drives a CXCL8 (macrophage) → CXCR1/2 (gastric cancer) → JAK/STAT1 → IL-10 → TAM M2 (NF-κB) positive feedback loop"
slug: cxcl8-cxcr1-2-jak-stat1-tam-tumor-feedback-loop
status: supported
confidence: 0.80
tags:
  - CXCL8
  - IL-8
  - CXCR1
  - CXCR2
  - JAK
  - STAT1
  - IL-10
  - NF-κB
  - TAM
  - M2-polarization
  - gastric-cancer
  - positive-feedback
  - hypoxia
domain: "immunology / oncology / cytokine-signaling"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.10) summarizes the four-step positive feedback loop in hypoxic gastric cancer: (1) macrophages secrete CXCL8/IL-8 under hypoxia → (2) CXCL8 binds CXCR1/2 on gastric cancer cells → (3) JAK/STAT1 activation in cancer cells → (4) STAT1 directly upregulates IL-10 transcription → (5) tumor IL-10 stimulates TAM M2 polarization via NF-κB → (6) further CXCL8 secretion (loop closure)."
conditions: "Documented in gastric cancer (in vitro and in vivo); generalizability to other cancer types requires validation."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

In hypoxic gastric cancer, a four-node positive feedback loop couples macrophage and tumor compartments:
1. Macrophages secrete CXCL8 (IL-8) under hypoxia.
2. CXCL8 binds CXCR1 / CXCR2 on gastric cancer cells.
3. JAK/STAT1 is activated in cancer cells; STAT1 directly upregulates IL-10 transcription.
4. Tumor-secreted IL-10 stimulates TAM M2 polarization through NF-κB signaling, which further drives CXCL8 secretion.

The loop creates a self-amplifying hypoxic-tumor / hypoxic-TAM crosstalk that simultaneously enhances tumor invasion, tumor proliferation, and TAM immunosuppression. Notable in this circuit: STAT1 is most often considered a pro-inflammatory M1 driver, yet here it drives the anti-inflammatory IL-10 output — a context-dependent role.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundations: [[foundations/cxcl8-il8]], [[foundations/nf-kb-p65-rela]].

## Conditions and scope

- Demonstrated in gastric cancer co-culture and xenograft models.
- The CXCR1/2 → JAK/STAT1 → IL-10 step is the most cancer-type-specific node; the CXCL8 hypoxia-induced secretion is more widely applicable.

## Counter-evidence

- In some cancers, CXCL8 binds CXCR1/2 to drive STAT3 (not STAT1) and a pro-inflammatory output.
- The STAT1-IL10 link is non-canonical and may reflect a tissue-specific transcription factor combination.

## Linked ideas

(none yet)

## Open questions

- Does CXCR1/2 antagonism (e.g. Reparixin) break this loop in vivo in hypoxic gastric cancer?
- Is the STAT1 → IL-10 axis a generalizable hypoxic-tumor response or a gastric-specific peculiarity?
