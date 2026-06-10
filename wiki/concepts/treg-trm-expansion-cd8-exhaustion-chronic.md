---
title: "Treg/Trm expansion with CD8 exhaustion as a shared signature of chronic skin inflammation"
aliases:
  - shared immune composition shift in chronic rash
tags: [immunology, skin, scrna-seq, treg, trm, cd8-exhaustion, inflammation]
maturity: active
key_papers:
  - classification-human-chronic-inflammatory-skin-disease
first_introduced: "Liu et al. 2022, Science Immunology"
date_updated: 2026-06-10
related_concepts: [tissue-resident-memory-cd8-t-cell-trm, cd8-t-cell-exhaustion-texterm, trm1-th2-th17-molecular-classification-inflammatory]
---

## Definition

A stereotyped shift in CD45+ immune cell composition shared across diverse chronic inflammatory skin diseases (AD, PV, LP, BP and indeterminate rashes): proliferation-driven expansion of all regulatory T (Treg) and tissue-resident memory T (Trm) cell classes together with universal exhaustion of cytotoxic CD8+ T cells, accompanied by a relative attenuation of antigen-presenting cells.

## Intuition

Regardless of the specific TH2/TH17 polarization that distinguishes disease types, the inflamed skin compartment converges on the same coarse architecture — more residents and regulators, exhausted killers — suggesting a common chronic-inflammation end state on top of disease-specific transcriptional programs.

## Formal notation

Weighted Gaussian linear model on log cluster proportions vs disease status; 27 of 41 clusters significantly altered. Representative effects: CTLex +80.4% (4.5→8.2%), Treg classes 2.19–3.13× expansion, Trm1 +71.4%, Trm2 +108.7%.

## Variants

- Disease-resolved version: CTLex and NK cells more elevated in PV than AD.

## Comparison

Distinct from the cancer-context terminal-exhaustion program in [[cd8-t-cell-exhaustion-texterm]]; here exhaustion is a shared, non-discriminating feature rather than a tumor-driven trajectory.

## When to use

When interpreting bulk compositional shifts of skin immune infiltrates or designing experiments to separate shared inflammatory architecture from disease-specific signatures.

## Known limitations

- Compositional estimates depend on CD45+ sorting and dissociation; absolute frequencies of rare populations (APCs, B/plasma cells) are underpowered.

## Open problems

- Whether Treg expansion reflects failed regulation (qualitative dysfunction) versus successful but insufficient control.

## Key papers

- [[papers/classification-human-chronic-inflammatory-skin-disease]] — quantifies the shared compositional shift across rash types.

## My understanding

The compositional convergence is a useful null model: it argues that what differentiates rash types lives in cell-type-restricted transcriptional state (Trm1 DEGs), not in coarse cell-proportion shifts.
