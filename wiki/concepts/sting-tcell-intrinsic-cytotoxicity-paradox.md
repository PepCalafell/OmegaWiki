---
title: "STING T cell-intrinsic cytotoxicity paradox"
aliases:
  - STING T cell death
  - T cell-intrinsic STING toxicity
  - SAVI T cell paradox
tags:
  - cgas-sting
  - t-cell
  - apoptosis
  - er-stress
  - nf-kb
maturity: stable
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2017"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

While extrinsic STING activation (DCs, macrophages, ECs, NK cells) supports T cell responses, T-cell-intrinsic STING signaling is cytotoxic and impairs proliferation, memory formation, and effector function. Observed across species, in SAVI patients, and across tested human STING agonists.

## Intuition

A core mechanistic explanation for first-generation STING-agonist clinical failures. Effective antitumor immunity requires T cells; STING agonists that reach systemic T cells kill the very effectors they were meant to enable. The TME thus has an inverse-dose-response window: enough STING to activate DCs/ECs/NK, not so much that T cells die.

## Variants

- Apoptotic pathway engagement via IRF3/STAT1 pro-apoptotic mediators
- ER stress and calcium homeostasis disruption
- NF-κB-driven cell death and impaired proliferation (interferon-independent)
- TH9 differentiation skewing via STING-NF-κB-mTOR in CD4 T cells
- Glycolysis suppression — STING inhibits HK2-dependent glycolysis, preventing T-cell expansion

## When to use

When designing CAR-T or TIL-based therapies combined with STING agonism — must stagger dosing (STING agonist before T cell infusion) or use cell-type-restricted delivery (ADCs to myeloid CCR2, EC-targeted nanoparticles) or engineer STING-resistant T cells.

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]]

## Open problems

- Whether IRF3 vs NF-κB dominates T-cell killing — selective targeting could decouple cytotoxicity from useful immune activation
- Engineering of STING-knockout or STING-attenuated CAR-T cells
- Why NK cells are resistant: low intrinsic STING + blunted IRF3 response

## My understanding

The single most actionable mechanistic insight from the past 5 years of STING tumor immunology. Any clinical STING strategy that ignores T-cell-intrinsic toxicity is likely to fail; the corollary is that NK-cell-centric STING strategies have a structurally wider therapeutic window.
