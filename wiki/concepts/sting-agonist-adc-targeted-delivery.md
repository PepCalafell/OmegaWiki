---
title: "STING-agonist antibody-drug conjugates and cell-targeted delivery"
aliases:
  - STING ADC
  - immunoSTING
  - exoSTING
  - albumin-hitchhiking STING
  - TAK-500
  - XMT-2056
tags:
  - cgas-sting
  - antibody-drug-conjugate
  - targeted-delivery
  - her2
  - ccr2
maturity: emerging
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2022"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

Conjugation of STING agonists (CDN or non-CDN) to targeting moieties (antibodies, nanobodies, extracellular vesicles, albumin-binders) to restrict STING activation to defined cell types (tumor cells expressing HER2/NaPi2b/EGFR, CCR2+ myeloid cells, or albumin-rich tumor regions) and lower systemic cytokine release.

## Intuition

Direct response to the T-cell cytotoxicity problem and pharmacokinetic limitations of free STING agonists — targeted delivery achieves an inherently narrower therapeutic window by concentrating the agonist where it helps and away from where it harms (T cells, healthy vasculature).

## Variants

- XMT-2056 (Mersana): non-CDN diABZI conjugated to anti-HER2 antibody, ~10× lower systemic cytokines than free agonist, Phase 1 (NCT05514717)
- TAK-500 (Takeda): TAK-676 CDN conjugated to anti-CCR2 antibody for myeloid-targeted delivery, 100× lower effective dose preclinically — but terminated for futility in combo with pembrolizumab
- CDK-002 / exoSTING (Codiak): extracellular vesicles loaded with CDN, preferentially taken up by APCs
- Albumin-hitchhiking diABZI: nanobody-conjugated for enhanced tumor accumulation
- SABER molecules: STING-agonist-based ER-targeting molecules for DC antigen co-presentation

## When to use

When designing next-generation STING-targeted strategies. The choice of targeting moiety should depend on which TME cell-type-specific output (tumor cell-intrinsic, myeloid-MDSC reprogramming, EC normalization, DC cross-presentation) is desired.

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]]

## Open problems

- TAK-500 clinical futility suggests CCR2-targeted myeloid STING activation may not be sufficient — what's the right myeloid subset?
- Selecting tumor surface antigens (HER2 vs others) whose expression correlates with intact downstream STING machinery
- Whether ADC payload release at the cell surface vs internalized release affects the canonical-vs-non-canonical STING bias

## My understanding

The most active translational front in STING therapeutics. TAK-500's failure is informative: cell-type-targeted delivery alone doesn't solve the problem if the targeted cells (here CCR2+ MDSCs) aren't the productive ones. The HER2-STING ADC (XMT-2056) is the most-watched ongoing trial.
