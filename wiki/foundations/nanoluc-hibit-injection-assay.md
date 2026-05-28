---
title: "NanoLuc HiBiT split-luciferase injection assay"
slug: nanoluc-hibit-injection-assay
domain: methods
status: mainstream
aliases:
  - HiBiT injection assay
  - NanoLuc HiBiT
  - split-luciferase translocation assay
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

A reporter assay that detects bacterial effector translocation into host cells using
split NanoLuc luciferase. An 11-amino-acid HiBiT tag is fused to the effector's C
terminus in bacteria; host cells stably express the complementary LgBiT fragment, so
luminescence is reconstituted only when the tagged effector is injected into the host
cytosol.

## Intuition

Light = the effector reached the host cytoplasm. The small HiBiT tag minimally
perturbs secretion.

## Formal notation

Specific injection is scored as luminescence fold-change in wild-type vs a
T3SS-defective control (e.g. ΔsctV) host bacterium, tested by Wilcoxon test across
biological/technical replicates.

## Key variants

Heterologous host delivery (e.g. Salmonella Typhimurium expressing candidate effectors)
vs native-strain delivery; CyaA and TEM-β-lactamase reporters are alternative
translocation assays.

## Known limitations

Missing chaperones/cofactors in heterologous hosts can cause false negatives; tag
placement can affect some effectors.

## Relevance to active research

Used to confirm specific T3SS-dependent injection of 32 commensal candidate effectors
into HeLa cells, validating bona fide effector identity.
