---
title: "NanoBiT split luciferase (LgBiT / SmBiT)"
slug: nanobit-split-luciferase
domain: "biochemistry / methods"
status: mainstream
aliases:
  - "NanoBiT"
  - "LgBiT/SmBiT"
  - "split NanoLuc"
first_introduced: "Dixon et al. 2016, ACS Chem. Biol."
date_updated: 2026-06-10
source_url: "https://doi.org/10.1021/acschembio.5b00753"
---

## Definition

A structural complementation reporter derived from NanoLuc luciferase, split into a large fragment (LgBiT, ~18 kDa) and a small peptide fragment (SmBiT, 11 aa). The fragments have deliberately weak intrinsic affinity, so luminescence is reconstituted only when LgBiT and SmBiT are brought together by a partner interaction — making it a tunable readout of protein proximity/association.

## Intuition

Tag two proteins with the two NanoLuc pieces; light is produced only when they come together. Because SmBiT binding is weak and reversible, the system reports dynamic association/dissociation, and the SmBiT peptide can itself be caged or grafted into an effector.

## Formal notation

LgBiT + SmBiT ⇌ reconstituted NanoLuc → luminescence. Luminescence ∝ fraction of complemented complex.

## Key variants

- SmBiT (low-affinity, dynamic) vs HiBiT (high-affinity, quantitative tagging)
- Furimazine substrate variants

## Known limitations

- Substrate consumption and signal decay over long time courses.
- Background from spontaneous fragment complementation at high concentrations.

## Open problems

- Engineering fast, reversible reconstitution without sacrificing dynamic range.

## Relevance to active research

In [[design-facilitated-dissociation-enables-timing-cytokine]], NanoBiT is used two ways: (1) tagging a designed host and target with LgBiT/SmBiT to show that facilitated dissociation rapidly breaks an otherwise stable split-enzyme complex; (2) caging the SmBiT peptide inside an effector so that target binding uncages it and reconstitutes luciferase — the basis of the rapid SARS-CoV-2 "AScov" biosensor.
