---
title: "PAK2 and PKCα as signaling regulators of immunosuppressive macrophages"
aliases:
  - PAK2/PKCα immunosuppressive macrophage axis
tags:
  - macrophage
  - immunosuppression
  - kinase
  - phosphoproteomics
  - TAM
maturity: emerging
key_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
first_introduced: "Totu, Bossart et al. 2025 NAR Molecular Medicine"
date_updated: 2026-06-02
related_concepts:
  - tumor-associated-macrophage-immunosuppression
  - kinase-activity-footprint-inference-phosphoproteomics
  - m1-m2-polarization-paradigm
---

## Definition

The hypothesis — derived from unbiased phosphoproteomic footprinting of primary human macrophages — that the kinases PAK2 and PKCα are central regulators of the signaling state of in vitro immunosuppressive (M2-polarized) macrophages, with a broader supporting cast of PKACα, PDPK1, and LRRK2. It reframes immunosuppressive polarization, historically described mostly at the transcriptomic level, in terms of specific kinase activities.

## Intuition

Proinflammatory (M1) macrophage signaling (IFN-γ/JAK–STAT, p38, JNK, NF-κB) is well mapped; the kinase wiring of immunosuppressive states is not. By reading which kinases' substrate footprints are enriched in M2a/M2c phosphoproteomes — and corroborating with activation-loop phosphosites — PAK2 and PKCα emerge as nodes that could be therapeutically nudged to revert protumoral macrophages.

## Formal notation

- PAK2: two activation-segment phosphosites (e.g. T169) upregulated in M2a; high network centrality
- PKCα ([[foundations/pkc-alpha-prkca]]): activation-loop T497 phosphorylated higher in both M2a and M2c; highest centrality node in the M2a network
- Supporting kinases: PKACα ([[foundations/pkac-alpha-prkaca]]) T198 (M2c), PDPK1 ([[foundations/pdpk1-pdk1-kinase]]) T513, LRRK2 ([[foundations/lrrk2-kinase]])
- Substrate relationships: PDPK1 and PAK2 are known substrates/partners of PKCα; PKACα and LRRK2 can be phosphorylated by PDPK1 and PAK2 respectively

## Variants

- M2a (IL-4/IL-13) vs M2c (IL-10) state-specific kinase emphasis
- Footprint-inferred vs activation-loop-evidenced kinase activity

## Comparison

vs RIP1/PI3Kγ as previously highlighted immunosuppressive-macrophage kinases (Wang 2018; Kaneda 2016): PAK2/PKCα are nominated here by unbiased MS rather than targeted assays. vs the [[m1-m2-polarization-paradigm]]: this is a signaling-level, not marker-level, characterization of the M2 pole.

## When to use

- Generating candidate kinase targets for macrophage repolarization in cancer
- Interpreting M2a/M2c phosphoproteomic signatures mechanistically

## Known limitations

- Kinase activities are inferred (footprinting), not directly measured for most kinases
- In vitro polarized macrophages may not equal in vivo TAMs
- PAK2/PKCα had not previously been defined as central immunosuppressive regulators — validation pending

## Open problems

- Causal tests (inhibition/knockdown) of PAK2 and PKCα in macrophage polarization
- Whether these kinases are tractable, selective targets in the tumor microenvironment

## Key papers

- [[papers/delineation-signaling-routes-underlie-differences-macrophage]] — nominates PAK2 and PKCα (with PKACα, PDPK1, LRRK2) as central kinases of immunosuppressive human macrophages via integrated (phospho)proteomics and network analysis.

## My understanding

A signaling-resolution complement to the marker- and transcriptome-level TAM literature in this vault. The strongest evidence is the activation-loop phosphorylation of PKCα (T497) and PKACα (T198); PAK2's centrality is suggestive. For thesis use, this is a source of mechanistic hypotheses about how immunosuppressive macrophages are wired, to be cross-checked against the hypoxia/TAM concepts.
