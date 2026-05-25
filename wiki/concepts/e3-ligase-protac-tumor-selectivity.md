---
title: "Tumor-type-enriched E3 ubiquitin ligases for PROTAC selectivity"
aliases:
  - PROTAC E3 ligase selectivity
  - tumor-selective E3 ligases
  - E3 ligase pan-cancer atlas
  - PROTAC handle E3 selection
  - tissue-restricted E3 ligases
  - cancer-enriched E3 ubiquitin ligases
  - PROTAC design selectivity
  - E3 ligase tumor specificity
  - PROTAC degrader tissue selectivity
  - context-restricted E3 recruiters
tags: [protac, e3-ligase, ubiquitin-proteasome, drug-design, selectivity]
maturity: emerging
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: ""
date_updated: 2026-05-25
related_concepts: []
---

## Definition
A drug-design concept in which proteolysis-targeting chimeras (PROTACs) achieve tumour-type-restricted protein degradation by recruiting E3 ubiquitin ligases whose expression is selectively elevated in a target cancer type, rather than the broadly expressed CRBN / VHL that dominate current PROTAC design.

## Intuition
Universal E3 recruiters give broad activity but limit tumour selectivity and force on-target toxicity wherever the substrate is expressed. Tumour-type-enriched E3 ligases (e.g., HERC5 in esophageal cancer, RNF5 in liver cancer) provide differential degradation handles that could narrow the therapeutic window.

## Formal notation
- E3 ligase: ~600 human E3 ligases catalyse ubiquitin transfer
- PROTAC: small bifunctional molecule = E3 ligand + linker + target ligand → ternary complex → ubiquitin-mediated degradation
- Tumour-selectivity: differential abundance of E3 across cancer types as a proxy for selective recruitment

## Variants
- Tumour-type-enriched E3 ligases (HERC5, RNF5)
- Tissue-restricted E3 ligases (e.g., MDM2, IAPs in specific cohorts)

## Comparison
- vs **CRBN / VHL PROTACs**: broadly expressed E3 recruiters; achievable but not tumour-selective.
- vs **molecular glue degraders**: alternative degrader chemistry; same E3-selectivity question applies.

## When to use
- PROTAC design programs that require tumour selectivity (e.g., for substrates expressed in essential normal tissues).
- Pan-cancer drug-design screens where E3 expression context is a covariate.

## Known limitations
- Expression of an E3 ligase does not guarantee functional capacity to ubiquitylate a chosen substrate.
- Compound chemistry for non-CRBN/VHL ligases is far less mature.

## Open problems
- Demonstrate tumour-selective degradation in vivo using a HERC5- or RNF5-recruiting PROTAC.
- Chemoproteomics-driven discovery of small-molecule ligands for novel E3s.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
A speculative but valuable section of TPCPA. Expression-level enrichment is necessary but far from sufficient for tumour-selective PROTAC activity, yet the framework is correct: pan-cancer atlases should serve PROTAC chemistry directly.
