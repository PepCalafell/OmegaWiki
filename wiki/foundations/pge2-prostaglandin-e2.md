---
title: "PGE2 — Prostaglandin E2"
slug: pge2-prostaglandin-e2
domain: lipid mediator / signalling
status: mainstream
aliases:
  - "PGE2"
  - "prostaglandin E2"
  - "dinoprostone"
  - "PGE-2"
  - "prostanoid E2"
  - "5Z,11alpha,13E,15S-dihydroxy-9-oxoprosta-5,13-dien-1-oate"
first_introduced: "Bergström & Samuelsson 1962"
date_updated: 2026-05-26
source_url: ""
---

## Definition

Prostaglandin E2 (PGE2) is a 20-carbon lipid mediator produced from arachidonic acid via the sequential action of COX1/COX2 and prostaglandin E synthase (PGES). PGE2 signals through four G-protein-coupled EP receptors (EP1–EP4) with distinct downstream couplings (Gq, Gs, Gi), giving rise to context-dependent biological effects spanning inflammation, fever, pain, vasodilation, mucosal protection, T-cell modulation, and efferocytosis-driven resolution.

## Intuition

PGE2 is the textbook "inflammatory mediator" (drives pain, fever, vasodilation) but is also a critical *pro-resolution* signal at tissues with apoptotic cell burden: efferocytosing macrophages secrete PGE2 that autocrinely / paracrinely induces TGF-β1, IL-10, and continued efferocytosis. The same molecule reads as inflammatory or resolving depending on receptor (EP1/3 vs EP2/4) and cellular context.

## Formal notation

- Synthesis: arachidonic acid → (COX1/COX2) PGH2 → (mPGES1, mPGES2, cPGES) PGE2
- Receptors and signaling:
  - EP1 (Gq): Ca²⁺/PKC, smooth muscle
  - EP2 (Gs): cAMP/PKA/CREB
  - EP3 (Gi): vasoconstriction, gastric protection
  - EP4 (Gs): cAMP/PKA/CREB, anti-inflammatory in macrophages
- Degradation: 15-PGDH oxidation; ABCC4 efflux
- Resolution context: EP2/EP4 signalling on macrophages induces TGF-β1 expression via p-CREB1
- Pharmacology: NS-398 (blocks COX2 synthesis); EP receptor selective antagonists in development

## Variants

- mPGES1 (inducible, microsomal) — co-regulated with COX2 in inflammation
- mPGES2, cPGES — constitutive

## Known limitations

- Context dependence (inflammatory vs resolving) makes therapeutic targeting hard
- COX2 inhibitor cardiovascular risk attributed in part to PGI2/PGE2 imbalance
- ELISA cross-reactivity with related prostanoids

## Open problems

- The differential roles of EP1-EP4 in distinct macrophage states (tissue-resident vs MoDM)
- Whether spatial concentration gradients of PGE2 within a plaque dictate resolution outcomes

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): PGE2 is the obligate intermediate between AC-induced COX2 activation and TGF-β1 induction. The EP2/EP4–p-CREB1 axis mediating this induction is DNMT3A-dependent — PGE2 signalling fails to induce TGF-β1 in DNMT3A-KO macrophages.
