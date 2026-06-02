---
title: "Chemokine-defined interstitial macrophage division of labor (CD206hi vs CD206lo IMs vs recMacs)"
aliases:
  - CD206hi vs CD206lo IM division of labor
  - interstitial macrophage division of labor
  - chemokine-defined IM subsets
  - IMck subsets
tags:
  - macrophage
  - interstitial-macrophage
  - chemokine
  - tumor-microenvironment
  - lung-cancer
maturity: emerging
key_papers:
  - chemokine-defined-macrophage-niches-establish-spatial
first_introduced: "2024"
date_updated: 2026-06-02
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tissue-resident-macrophage-tumor-niche
  - anatomical-niche-predicts-macrophage-function
---

## Definition

Lung interstitial macrophages (IMs) are not a uniform population but partition into functionally opposed, chemokine-defined subsets that establish a division of labor in tumor immunity. CD206hi (Folr2⁺Cd163⁺Mmp9⁺) IMs express antitumorigenic chemokines (CXCL13, CXCL9, CXCL10) and support lymphocyte recruitment / TLS formation, whereas CD206lo (Tmem119⁺Mmp12⁺Ccr2⁺) IMs and Ly6c2⁺Fn1⁺Vcan⁺ recruited macrophages (recMacs) express protumorigenic programs (Ccl2; and for recMacs Spp1, Vegfa, Arg1, Cd274/PD-L1).

## Intuition

The same broad surface markers (CD11c, CD11b, CD64, CD88, CD206, MHCII) are shared across IMs and recMacs, so canonical flow gating cannot resolve function. scRNA-seq reveals ≥10 chemokine-expressing IM subsets (IMck0–IMck9) — e.g. IMck7 (Cxcl9/Cxcl10), IMck8 (Cxcl13), IMck1 (Ccl2/Ccl7/Ccl12) — whose chemokine output, not surface phenotype, predicts whether the cell organizes protective lymphoid architecture or fuels a protumor myeloid loop.

## Formal notation

IM compartment = {CD206hi IM (Cxcl13⁺ / Cxcl9⁺ / Cxcl10⁺ subsets), CD206lo IM (Ccl2⁺)} ; recruited compartment = recMac (Ly6c2⁺Fn1⁺Vcan⁺, Ccl2⁺).

## Variants

- IMck0–IMck9 chemokine-defined subsets (Li et al., Nat. Immunol. 2024).
- CD206 (Mrc1) is shown here to be neither macrophage-restricted nor predictive of tumor-promoting function despite "M2-like" usage.

## Comparison

Refines the simple M1/M2 and "CD206 = pro-tumor M2" framing: CD206hi IMs are antitumor here, while protumor activity tracks with recMac lineage and Ccl2 expression. Complements [[macrophage-ontogeny-resident-vs-monocyte-derived]] by adding chemokine-subset granularity within the resident compartment.

## When to use

When interpreting macrophage heterogeneity in lung/solid tumors where chemokine output and lineage — not CD206 or Trem2 surface level — determine pro- vs antitumor function.

## Known limitations

- No current genetic tool (except Ccl24Cre) isolates a single chemokine-defined IM subset; subsets are studied as the aggregate CD206hi compartment.
- Defined primarily in mouse lung cancer models.

## Open problems

- Functional dissection of individual IMck subsets (Cxcl13⁺ vs Cxcl9⁺ vs Cxcl10⁺).
- Whether the same division of labor holds in human lung tumors at subset resolution.

## Key papers

- [[chemokine-defined-macrophage-niches-establish-spatial]]

## My understanding

This is the organizing concept of the paper: macrophage "identity" useful for tumor immunity is a chemokine-program identity nested inside lineage (IM vs recMac), and spatial niche reinforces it. It reframes CD206 from a pro-tumor marker into a near-neutral one.
