---
title: "cGAS-STING pathway: canonical and non-canonical outputs"
aliases:
  - cGAS-STING signaling
  - canonical STING-IRF3-IFN
  - non-canonical STING outputs
  - STING-induced autophagy
  - STING-NF-κB cell-type-dependent
tags:
  - innate-immunity
  - cgas-sting
  - type-i-ifn
  - nf-kb
  - autophagy
  - programmed-cell-death
  - sasp
maturity: stable
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2008"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

The cGAS-STING pathway converts cytosolic dsDNA into a branched signaling output: (canonical) STING → TBK1 → IRF3 → type I IFN/ISGs; (non-canonical) STING → IKK/IKKε → NF-κB → IL-1β/IL-6/TNFα; plus autophagy (primordial, IFN-independent), metabolic reprogramming, and programmed cell death (apoptosis, ferroptosis, pyroptosis).

## Intuition

A single "stress sensor" that can produce qualitatively different downstream programmes depending on (a) cell type, (b) acute vs chronic activation, (c) ligand-occupancy modular motifs in the STING C-terminal tail (CTT), and (d) post-translational/trafficking state. The same upstream stimulus (cytosolic DNA) can therefore yield antiviral immunity, anti-tumor immunity, immune evasion, T-cell death, or SASP-driven pro-tumor inflammation.

## Variants

- IRF3-dominant output: classic antiviral / antitumor type I IFN programme
- NF-κB-dominant output: pro-inflammatory cytokines, can be pro-tumor in CIN-high contexts
- Autophagy-only output: evolutionarily ancient, IFN-independent, restricts the IFN response itself via STING degradation
- Cell-death output: signal-strength-dependent pro-apoptotic mode in T cells and tumor cells

## When to use

When interpreting STING-pathway perturbations: the readout must be parsed across all output arms, not just type I IFN. Apparent "STING activation" without IRF3-driven ISGs is common and can indicate the non-canonical or autophagy-only arm.

## Open problems

- What dictates the relative weighting of IRF3 vs NF-κB vs autophagy outputs in a given cell?
- Can therapeutic agents bias the output toward canonical IRF3 while sparing the pro-tumor NF-κB arm?

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]] — review charting the divergent STING outputs across the TME

## My understanding

The branching of outputs is the core reason direct STING agonists have failed in the clinic: a single small molecule cannot select which arm to engage in which cell type. Next-generation strategies focus on indirect activation (via ENPP1/TREX1) and cell-targeted delivery to bias the output without changing STING itself.
