---
title: "4-octyl itaconate (4-OI) — cell-permeable itaconate derivative; TET2 / Nrf2 modulator"
slug: 4-octyl-itaconate-tet2-inhibitor
domain: "pharmacology / immunology"
status: mainstream
aliases:
  - "4-octyl itaconate"
  - "4-OI"
  - "4-OctylIT"
  - "4OI"
  - "octyl itaconate"
  - "cell-permeable itaconate"
  - "TET2 cysteine modifier"
  - "Nrf2 activator itaconate"
first_introduced: "Mills et al. 2018 (Nature) — Nrf2; Chen et al. 2022 (Nat Metab) — TET2"
date_updated: 2026-05-11
source_url: "https://pubchem.ncbi.nlm.nih.gov/compound/118903093"
---

## Definition

4-octyl itaconate (4-OI) is a cell-permeable ester derivative of the macrophage-derived metabolite itaconate. It hydrolyzes intracellularly into itaconate-like reactive species that covalently modify cysteine residues on multiple targets. In macrophages, it acts as both an Nrf2 activator (via KEAP1 cysteine modification) and a TET2 active-site cysteine modifier — the latter inhibiting TET2-mediated 5mC → 5hmC oxidation.

## Intuition

Itaconate is produced from cis-aconitate by IRG1/ACOD1 during inflammation and acts as a built-in negative regulator of inflammation. 4-OI is the engineered ester that allows experimental delivery without TCA-cycle entry confounders. Its TET2 inhibition is the most relevant property in the Calafell 2024 paper, where 4-OI is used as a positive control for "block active demethylation."

## Formal notation

- Chemical formula: C₁₃H₂₂O₄, MW ~ 242.31 Da
- Covalent target: cysteines on TET2 catalytic domain (Cys1135, Cys1232, others); KEAP1; GAPDH; ALDOA
- Typical in vitro doses: 100-250 μM (3-24 h)
- Hydrolyzes to itaconate equivalents intracellularly

## Key variants

- Dimethyl itaconate (DMI) — earlier-generation cell-permeable analog
- Itaconate itself (poorly permeant)
- 4-OI is currently the preferred experimental tool

## Known limitations

- Multiple off-target cysteine modifications make mechanism-specific interpretation challenging.
- Nrf2 activation can confound inflammatory readouts independent of TET2 inhibition.
- High doses (>250 μM) cause cytotoxicity.

## Open problems

- TET-isoform selectivity (TET1 vs TET2 vs TET3) not fully characterized.
- In vivo pharmacology limited.
- Clean genetic TET2 KO is the gold-standard orthogonal validation.

## Relevance to active research

Used in Calafell-Segura et al. 2024 ([[papers/nf-kb-tet2-promote-macrophage-reprogramming]]) as the positive-control TET2 inhibitor to demonstrate that active TET2-mediated demethylation is necessary for cluster C2 hypomethylation and downstream proinflammatory gene expression in mMAC1. The TET2-inhibition phenotype phenocopies p65-inhibition (BAY11-7082) at the methylation readout but is mechanistically distinct (cysteine-modified TET2 vs blocked NF-κB activation).
