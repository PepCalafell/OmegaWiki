---
title: "MMP14-protease-activated IL-2 prodrug (TAM-restricted cytokine unmasking)"
aliases:
  - "MMP14-cleavable IL-2 prodrug"
  - "protease-activated IL-2 prodrug"
  - "TAM-protease-activated IL-2"
tags:
  - prodrug
  - protease-activation
  - IL-2
  - MMP14
  - tumor-microenvironment
  - cancer-immunotherapy
maturity: emerging
key_papers:
  - macrophage-targeted-immunocytokine-leverages-myeloid-nk
first_introduced: "von Locquenghien et al. 2025 Cell"
date_updated: 2026-05-27
related_concepts:
  - masked-antibody-tme-conditional
  - myeloid-targeted-immunocytokine-mite
  - trans-acting-immunocytokine
  - switchable-cytokine-mimic-signalling-timing
---

## Definition

A cytokine prodrug strategy in which an active IL-2 (typically an IL-2Rβ-biased superkine) is rendered inert by an attached blocking domain (extracellular IL-2Rβ or anti-IL-2 scFv) joined via a peptide linker selectively cleaved by the TAM-specific matrix metalloproteinase MMP14. Activation occurs only at the tumor site where MMP14 is enriched, drastically reducing systemic IL-2 toxicity while preserving on-target activity.

## Intuition

Active IL-2 in circulation triggers cytokine storms (IFN-γ, IL-2, IL-6) and hepatotoxicity (ALT/AST). Masking IL-2 with a cleavable IL-2Rβ blocker turns IL-2 "off" in the periphery and "on" in tumors, exploiting the fact that MMP14 is highly TAM-restricted among immune cells and is among the most reliably tumor-enriched proteases.

## Variants

- Mono-cleavage / single-mask designs (MiTE-76, MiTE-95, MiTE-144)
- Dual-cleavage / dual-mask designs (MiTE-208) — lower background, lower potency
- Alternative cytokines: IL-15, IL-12 in conceptually similar prodrug formats (referenced but not validated in this paper)
- Other masking strategies: anti-cytokine scFv, anti-cytokine antibody mimetic, pH-responsive cytokine variants (alternative to protease-based)

## Comparison

- vs anti-PD-L1-IL-15 (unmasked tumor-targeted ICK): MiTE adds TAM-protease-restricted activation
- vs αRSV-IL-2SK (masked, non-targeting control): MiTE adds TAM-targeting (TREM2) for synergy
- vs WT IL-2 (aldesleukin): cleaved IL-2SK has ~270-fold higher IL-2Rβ affinity (KD 1.26 nM vs 280 nM)
- vs T-cell-targeted αPD-1-IL-2 / αTIM3-IL-2: protease-restricted vs receptor-restricted localisation

## When to use

- Solid tumors with documented MMP14-high TAM infiltration
- ICK programmes where IL-2 systemic toxicity is the limiting factor
- Designs where decoupling biodistribution (target) from activation (protease) is desirable

## Known limitations

- MMP14 also expressed by cancer-associated fibroblasts — off-target activation in fibrotic stroma possible
- Linker substrate specificity is imperfect (some activity on MMP3/7/10/11)
- Long-term ADA formation against masked vs unmasked IL-2 unknown
- Tumor-type generalisation untested beyond MC38, MCA205, RCC PDTFs

## Open problems

- Whether tumors evolve resistance by downregulating MMP14
- Optimal masking design (IL-2Rβ extracellular vs anti-IL-2 scFv vs engineered peptide)
- Half-life optimisation while preserving tumor selectivity

## Key papers

- [[papers/macrophage-targeted-immunocytokine-leverages-myeloid-nk]] — first MMP14-cleavable IL-2 prodrug demonstrated in vivo with safety + efficacy

## My understanding

The conceptual payload here is decoupling "where the molecule goes" (TREM2 targeting) from "where it activates" (MMP14 cleavage). Most prior TME-conditional designs anchor activation to the antibody target itself; protease-restricted activation is a more general mechanism that could be ported to other TAM-restricted enzymes (cathepsins, ADAM proteases) or to non-IL-2 cytokines.
