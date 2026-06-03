---
title: "Opal multiplex IHC (Vectra Polaris)"
slug: opal-polaris-multiplex-ihc
domain: molecular imaging
status: mainstream
aliases: ["Opal", "Opal Polaris", "Opal multiplex", "Vectra Polaris", "Opal TSA", "tyramide signal amplification"]
first_introduced: "2014"
date_updated: 2026-06-03
source_url: "https://www.akoyabio.com/phenoimager/opal-kits/"
---

## Definition

Opal multiplex immunohistochemistry uses tyramide signal amplification (TSA) to detect multiple protein markers on a single tissue section. For each marker, a primary antibody is bound, followed by anti-IgG-HRP polymer, which catalyses covalent deposition of an Opal fluorophore; antibodies are then stripped and the cycle repeats for the next marker. Whole-slide multispectral scanning (e.g. Vectra Polaris) then resolves the spectrally distinct Opal dyes.

## Intuition

It enables several proteins (e.g. CD8, PD-1, PanCK, PD-L1) to be visualised together with high sensitivity (via TSA amplification) across an entire tissue section, allowing identification of marker-defined cell types and their spatial co-localisation (e.g. CD8+PD-1+ T cells next to PanCK+PD-L1+ tumour cells).

## Formal notation

Not applicable. Output is a multispectral whole-slide image; downstream cell phenotyping yields marker-positive cell calls and spatial coordinates.

## Key variants

- Manual Opal staining
- Automated Opal (e.g. Leica BOND)
- Variable panel sizes (typically 6–8 markers per round)

## Known limitations

- Limited number of simultaneous markers compared to highly multiplexed imaging (CODEX, CosMx)
- Co-localisation indicates proximity, not direct interaction (lower resolution than PLA)
- Spectral unmixing and tyramide deposition require careful optimisation

## Open problems

- Expanding marker multiplexing while preserving epitopes
- Quantitative interaction inference from co-localisation

## Relevance to active research

Used as a protein-level orthogonal validation of ligand–receptor and checkpoint interactions (e.g. PD-1/PD-L1) nominated by spatial transcriptomics, complementing nano-scale PLA validation.
