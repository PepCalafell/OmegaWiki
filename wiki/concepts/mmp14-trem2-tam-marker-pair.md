---
title: "MMP14–TREM2 co-expression as TAM-specific marker pair"
aliases:
  - "MMP14-TREM2 TAM signature"
  - "MMP14-TREM2 co-expression"
tags:
  - TREM2
  - MMP14
  - tumor-associated-macrophage
  - tumor-microenvironment
  - protease
  - biomarker
maturity: emerging
key_papers:
  - macrophage-targeted-immunocytokine-leverages-myeloid-nk
first_introduced: "von Locquenghien et al. 2025 Cell"
date_updated: 2026-05-27
related_concepts:
  - trem2-tumor-associated-macrophage
  - mmp14-protease-activated-il2-prodrug
---

## Definition

Tumor-associated macrophages co-express TREM2 (myeloid checkpoint receptor) and MMP14 (membrane-type matrix metalloproteinase) at significantly higher levels than other immune cells, with strong positive correlation in weighted co-expression analyses of both human and murine tumors. Immunofluorescence confirms co-localised expression within tumor tissue and minimal overlap in adjacent healthy tissue.

## Intuition

If both the therapeutic target (TREM2) and the activation switch (MMP14) are uniquely present on the same TAM, then a single bifunctional molecule can simultaneously achieve binding and protease-restricted unmasking on that cell — a clean substrate for trans-acting protease-activated immunocytokines.

## Formal notation

- Co-expression: significant weighted-correlation (pink-coded in lollipop plot, Figure 3C) in human and murine tumors
- Validated against: ~13.8 M-cell single-cell atlas (PBMCs, healthy tissues, tumor-adjacent, tumors)
- Tissue confirmation: immunofluorescence on matched human lung tumor vs tumor-adjacent

## Comparison

- vs MMP9-TREM2: weaker correlation
- vs MMP19-TREM2 / ADAM9-TREM2 / cathepsin-TREM2: weaker correlations
- vs MMP14 alone: TAM enrichment shared with cancer-associated fibroblasts, but combined TREM2-MMP14 is TAM-restricted

## When to use

- As biomarker pair for TAM-restricted drug design (MiTE-class therapeutics)
- For patient stratification: tumors with high TREM2 + MMP14 likely respond to MiTE-class agents
- For interpreting TAM heterogeneity studies (which subsets co-express both?)

## Known limitations

- CAFs also express MMP14 — single-marker MMP14 is insufficient for TAM specificity
- TREM2 expression within TAMs is heterogeneous (TREM2⁺ "lipid-associated" vs TREM2⁻ subsets)
- Correlations are at the population level; cell-resolution co-expression on the same TAM not exhaustively quantified

## Open problems

- Whether MMP14-TREM2 co-expression is functionally coupled or independently regulated
- Stability across tumor types and treatment courses
- Single-cell prevalence: what fraction of TAMs co-express both vs only one?

## Key papers

- [[papers/macrophage-targeted-immunocytokine-leverages-myeloid-nk]] — establishes the co-expression and exploits it therapeutically

## My understanding

This is the empirical justification that makes MiTEs work: the same cell that you want to reprogram also activates the cytokine arm of the same molecule. It is also a useful concept for thinking about other dual-functional myeloid-targeted designs — wherever a target receptor and a TAM-restricted enzyme co-occur, the same prodrug logic may apply.
